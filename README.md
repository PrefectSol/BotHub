# BotHub v1.0

A simple server for local self-written games and bots in the form of modules with Docker and Web-implementation

## Install

```bash
git clone https://github.com/PrefectSol/BotHub.git
cd BotHub
make build
```

## Run host

```bash
make host
```
 - The file `host-config.json` is used for configuration

## Run client
```bash
make client
```
 - The file `client-config.json` is used for configuration


## Custom bots
 - For create bot for game you need write some file `bot.py` thats realize abstract class `Bot`

## Custom games
 - For add new game you need add new project in `hub/` with your class implementation of the abstract class `Game`

## Clear solution
```bash
make clear
```