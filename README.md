# Ohjelmistotekniikka, harjoitustyö

Klassikkopeli "2048" pygamella toteutettuna Aineopintojen harjoitustyö: ohjelmistotekniikka -kurssia varten.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/arkkitehtuuri.md)
- [Release](https://github.com/vdavd/ot-harjoitustyo/releases/tag/viikko5)
- [Käyttöohje](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/kayttoohje.md)

## Suorita seuraavat komennot hakemistossa 2048:

## Asennus

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

## Testaus

Suorita testit komennolla:

```bash
poetry run invoke test
```

## Testikattavuus

Generoi testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```

## Linttaus

```bash
poetry run invoke lint
```
