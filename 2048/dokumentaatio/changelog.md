## Viikko 3

- Sovellus alustettu
- Kun sovelluksen käynnistää, käyttäjä näkee 4x4-pelilaudan, jossa on 2 laattaa (arvoltaan 2 tai 4) satunnaisissa paikoissa.
- Sovelluksen rakenne jakautuu tällä hetkellä kolmeen luokkaan:
  - GameLogic, joka käsittelee pelin sisäistä logiikkaa ja muutoksia taulukkoon, jossa pelin tilaa säilytetään.
  - Display, joka on vastuussa peliruudun piirtämisestä.
  - GameLoop, joka on vastuussa peliloopista ja kutsuu GameLogic- ja Display-luokkien metodeita.
- Sovellukseen lisätty testi, joka tarkistaa, että pelin alkutila generoidaan oikein.
- Invoke-tehtävät sovelluksen käynnistämiselle, testaamiselle ja coverage-raportin generoimiselle.
