# Shoot Em' Up Arcade-peli

Shoot Em' Up tyylinen arcade-peli, jossa pelaaja ohjaa avaruusalusta ja väistelee ja ampuu vastaantulevia vihollisia.
Alkuun yhdentyyppisiä vihollisia, mutta myöhemmin mahdollisesti lisää vihollistyyppejä.

Peli on muutaman minuutin kestävä taso, joka etenee omaa tahtiaan, ja jossa pelaajan alus voi liikkua ja ampua vihollisia jotka ilmestyvät näytölle.


## Dokumentaatio

- [Käyttöohje](https://github.com/tkhnhy/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/tkhnhy/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/tkhnhy/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Vaatimusmäärittely](https://github.com/tkhnhy/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/tkhnhy/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)


## Releaset
- [Löydät releaset täältä](https://github.com/tkhnhy/ot-harjoitustyo/releases)
## Ohjelman käyttö

1. Asenna riippuvuudet poetrylla

```sh
poetry install
```

2. Käynnistä ohjelma komennolla 
```sh
poetry run invoke start
```

## Muita komentoja 

- Luo coverage html raportti
```sh
poetry run invoke coverage_report
```
- Pylint arviointi
```sh
poetry run invoke lint
```