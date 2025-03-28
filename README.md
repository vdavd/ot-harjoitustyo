# Ohjelmistotekniikka, harjoitustyö

Klassikkopeli "2048" pygamella toteutettuna Aineopintojen harjoitustyö: ohjelmistotekniikka -kurssia varten.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/vdavd/ot-harjoitustyo/blob/master/2048/dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet:

```bash
poetry install
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
