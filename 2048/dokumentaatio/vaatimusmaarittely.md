# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on pygamella toteutettu versio klassikkopelistä 2048. Pelissä käyttäjä yhdistelee samanarvoisia kahden potensseja 4x4-ruudukossa pyrkien saavuttamaan 2048-laatan. Sovellus on tarkoitettu viihteeksi ja loogisen ajattelun harjoittamiseen.

## Käyttäjät

Sovelluksessa ei ole erillisiä käyttäjärooleja, sillä kyseessä on yksinpeli.

## Käyttöliittymä

Sovelluksen käyttöliittymä koostuu pelinäkymästä, jossa käyttäjä voi pelata 2048-peliä. Näkymään kuuluu:

- 4x4-peliruudukko (tehty)
- Nykyinen pistemäärä ja mahdollisesti ennätyspistemäärä (tehty ennätyspistemäärää lukkunottamatta)
- Uusi peli -painike
- Pelin ohjeet

## Perusversion tarjoama toiminnallisuus

### Pelin aloitus

- Käyttäjä voi aloittaa uuden pelin, jolloin 4x4-ruudukkoon ilmestyy kaksi laattaa, joiden arvo on 2 tai 4. (tehty)

### Pelimekaniikka

- Käyttäjä voi siirtää siirtää laattoja nuolinäppäimillä ylös, alas tai sivuille. (tehty)
- Jos kaksi samanarvoista laattaa koskettavat siirron yhteydessä, ne yhdistyvät yhdeksi laataksi, jonka arvo on laattojen summa. (tehty)
- Jokaisen siirron jälkeen johonkin ruudukon satunnaiseen soluun ilmestyy uusi laatta (2 tai 4). (tehty)
- Peli päättyy, kun pelaaja ei voi tehdä enää laillisia siirtoja (ruudukko on täynnä, eikä sisällä vierekkäisiä laattoja, joilla on sama arvo). (tehty)
- Peli näyttää pelaajalle voittoilmoituksen, kun 2048-laatta saavutetaan. (tehty)

### Pistelasku

- Käyttäjän pisteet kasvavat yhteenlaskettujen laattojen summan mukaan. (tehty)
- Sovellus näyttää nykyisen pistemäärän ja mahdollisesti korkeimmat saavutetut pisteet. (tehty, mutta piste-ennätystä ei vielä tallenneta)

## Jatkokehitysideoita

Perusversion jälkeen sovellusta voidaan laajentaa seuraavilla toiminnallisuuksilla:

- Käyttäjän kirjautuminen ja pistetilastojen tallentaminen
- Eri pelimuodot (esim. suurempi ruudukko tai rajattu siirtomäärä)
- Animaatiot ja visuaaliset efektit
- Tulostaulukko ja parhaiden pelaajien lista
- Pelin tallennus ja jatkaminen myöhemmin
- Pelin ohjaaminen kosketusnäytöllä ja hiirellä
