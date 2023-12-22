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
	
```
## Käyttöliittymä

Käyttöliittymä koostuu kahdesta eri näkymästä. Varsinainen graaphinen pelinäkymä, sekä terminaalin highscore näkymä. Käyttölittymä on eristetty varsinaisesta sovelluslogiikasta

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