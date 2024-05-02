install-all: install-hub install-seabattle install-tic-tac-toe

install-hub:
	@pip install -r requirements.txt

install-seabattle:
	@pip install -r hub/SeaBattle/requirements.txt

install-tic-tac-toe:
	@pip install -r hub/TicTacToe/requirements.txt

build:
	@docker build -t bothub .

host:
	@docker run -p 80:5000 bothub
	
client:
	@python scripts/client.py

clear:
	@python scripts/clear.py
	