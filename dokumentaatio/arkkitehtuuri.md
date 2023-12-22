# Arkkitehtuuri

## Rakenne

Sovellus on jaettu kolmeen osaan, sprites sisältää näytöllä näkyvät oliot, interface sisältää käyttöliittymää
koskevan koodin, ja viimeinen osa on varsinainen sovelluslogiikka.

![Pakkausrakenne](./kuvat/package.PNG)

#### Luokkakaavio
```mermaid

flowchart TD;

	main(main)
	ui(ui)
	game_loop(game_loop)
	player(player)
	enemy_spawns(enemy_spawns)
	enemies(enemies)
	highscore(highscore)
	
	main --> ui
	main --> game_loop
	player --> main
	enemy_spawns --> game_loop
	game_loop --> ui
	enemies --> enemy_spawns
	main --> highscore
	highscore --> ui
	
```
## Käyttöliittymä

Käyttöliittymä koostuu kahdesta eri näkymästä. Varsinainen graaphinen pelinäkymä, sekä terminaalin highscore näkymä. Käyttölittymä on eristetty varsinaisesta sovelluslogiikasta

## Sovelluslogiikka
Pääosa sovelluslogiikasta sijaitsee game_loop luokassa, joka hoitaa jokaisella ruudunpäivityksellä tehtävät tapahtumat. Luokka enemy_spawns sisältää tietoja, milloin ja mitä vihollisia ilmestyy näytölle.
```mermaid

flowchart TD;

	game_loop(game_loop)
	enemy_spawns(enemy_spawns)
	arrangements(arrangements)
	sprites(sprites)
	clock(clock)
	event_queue(event_queue)
	
	game_loop --> enemy_spawns
	game_loop --> clock
	game_loop --> event_queue
	game_loop --> sprites
	enemy_spawns --> arrangements
	arrangements --> sprites
	
```
#### Highscore tietojen talletus
Sovelluslogiikan highscores luokka tallentaa pelaajan pistemäärän csv tiedostoon highscore.csv muodossa:
```
WLF,950
JCK,400
```
Nimi ensin ja pistemäärä seuraavaksi.

## Päätoiminnallisuudet

Aluksen ohjaus:

```mermaid
sequenceDiagram
title Siirrä alus vasemmalle

actor User
participant game_loop
participant sprites.player
participant interface.renderer

User->>game_loop: Painaa "a" näppäintä
game_loop->>sprites.player: moveplayer
game_loop->>interface.renderer: render
```

Pisteiden talletus:
```mermaid
sequenceDiagram
title Tallenna pistemäärä

actor User
participant highscore_interface
participant highscores
participant main

User->>highscore_interface: Syöttää nimensä
highscore_interface->>highscores: writescore "nimi, pistemäärä"
main -->> highscores: antaa pistemäärän
```