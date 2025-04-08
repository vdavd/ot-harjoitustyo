## Viikko 3

- Sovellus alustettu
- Kun sovelluksen käynnistää, käyttäjä näkee 4x4-pelilaudan, jossa on 2 laattaa (arvoltaan 2 tai 4) satunnaisissa paikoissa.
- Sovelluksen rakenne jakautuu tällä hetkellä kolmeen luokkaan:
  - GameLogic, joka käsittelee pelin sisäistä logiikkaa ja muutoksia taulukkoon, jossa pelin tilaa säilytetään.
  - Display, joka on vastuussa peliruudun piirtämisestä.
  - GameLoop, joka on vastuussa peliloopista ja kutsuu GameLogic- ja Display-luokkien metodeita.
- Sovellukseen lisätty testi, joka tarkistaa, että pelin alkutila generoidaan oikein.
- Invoke-tehtävät sovelluksen käynnistämiselle, testaamiselle ja coverage-raportin generoimiselle.

## Viikko 4

- Sovelluslogiikkaa laajennettu:
- Pelaaja voi liikuttaa pelilaudan laattoja vasemmalle, oikealle, ylös tai alas nuolinäppäimillä.
- Toisiinsa törmäävät samanarvoiset laatat yhdistyvät uudeksi laataksi, jonka arvo vastaa laattojen summaa.
- Jokaisen siirron jälkeen satunnaiseen kohtaan pelilautaa ilmestyy uusi laatta, jonka arvo on 2 tai 4.
- Uusi yksikkötesti, joka tarkistaa, että laattojen siirtely ja yhdistyminen toimii oikein
- Pylint konfiguroitu sovellukseen
- Invoke-tehtävä linttaamiselle
- Automaattinen formatointi otettu käyttöön
- Invoke-tehtävä automaattiselle fromatoinnille
