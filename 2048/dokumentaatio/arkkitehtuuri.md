# Arkkitehtuurikuvaus

## Rakenne

Entities-kansio sisältää User-luokan, joka vastaa käyttäjän tietojen säilytämisestä ohjelman suorituksen aikana. Repositories-kansio sisältää UserRepository-luokan, joka vastaa käyttäjän tietojen hakemisesta ja talletamisesta SQLite-tietokantaan. Luokka display vastaa peliruudun piirtämisestä, GameLogic pelin sisäisen logiikan päivittämiseestä ja GameLoop peliloopin ja käyttäjän syötteiden käsittelystä.

## Luokkakaavio

Sovelluksen luokkarakenne selviää seuraavasta kuvaajasta. Riippuvuudet GameLogic ja Display injektoidaan uokalle GameLoop. Luokilla GameLogic ja UserRepository on riippuvuus luokkaan User.

![class diagram](kuvat/classdiagram.png)

## Käyttöliittymä

Pelin käyttöliittymä sisältää peliruudukon sekä pelaajan pisteet ja ennätyspistemäärän.

## Pelin tilan päivittyminen

Kun pelaaja painaa jotain nuolinäppäimistä liikuttaakseen pelilaattoja, toimii sovelluslogiikka seuraavalla tavalla:

```mermaid
sequenceDiagram
    actor Player
    participant GameLoop
    participant GameLogic
    Player->>GameLoop: press down right key button
    GameLoop->>GameLogic: update_grid('right')
    activate GameLogic
    GameLogic->>GameLogic: move_and_merge_tiles(np.rot90(self.grid, k=2))
    GameLogic->>GameLogic: new_grid
    GameLogic->>GameLogic: add_tile()
    opt not free_spaces
    GameLogic->>GameLogic: change_state("GAMEOVER")
    end
    deactivate GameLogic
    GameLoop->>GameLogic: update_points()
    GameLoop->>GameLogic: check_victory()
    activate GameLogic
    opt 2048 in grid
    GameLogic->>GameLogic: change_state("WIN")
    end
    deactivate GameLogic

```

## Tietojen pysyväistallennus

Luokka UserRepository vastaa pelaajan tietojen tallettamisesta SQLite-tietokantaan. Tietokannassa on yksi tietokantataulu, users, joka sisältää pelaajan käyttäjänimen ja ennätyspistemäärän.
