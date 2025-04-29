# Käyttöohje

Lataa viimesin [release](https://github.com/vdavd/ot-harjoitustyo/releases/tag/viikko5)

## Ohjelman asennus ja käynnistäminen

Asenna riippuvuudet:

```bash
poetry install
```

Alusta tietokanta:

```bash
poetry run invoke init-db
```

Käynnistä sovellus:

```bash
poetry run invoke start
```

## Pelin pelaaminen

- Voit liikuttaa pelilaattoja nuolinäppäimillä.
- Voit käynnistää pelin alusta painamalla R.
- Peli loppuu, kun ruudukko on täynnä, eikä sinulla ole laillisia siirtoja.
- Voitat pelin, kun 2048-laatta on saavutettu

Peli tallentaa ennätyspistemääräsi tietokantaan, kun suljet peliruudun.
