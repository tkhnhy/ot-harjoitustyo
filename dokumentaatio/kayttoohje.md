# Käyttöohje
## Ohjelman asennus
1. [Lataa uusin release sivulta](https://github.com/tkhnhy/ot-harjoitustyo/releases)

2. Pura tiedosto haluamaasi kansioon

3. Avaa terminaali ja asenna riippuvuudet poetrylla

```sh
poetry install
```

## Ohjelman käyttö

Käynnistä ohjelma komennolla 
```sh
poetry run invoke start
```
### Pelin kulu
- Peli alkaa heti käynnistyskomennon jälkeen
- Ohjaa avaruusalusta WASD-näppäimillä ja ammu painamalla välilyöntiä
- Kun voitat tai häviät pelin, terminaali kysyy kolme merkkiä pitkää pelaajanimeä. Syötä nimi tallentaaksesi pistemäärä 