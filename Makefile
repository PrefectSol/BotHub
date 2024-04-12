install-all: install-hub install-seabattle install-tic-tac-toe

install-hub:
	@pip install -r requirments.txt

install-seabattle:
	@pip install -r hub/SeaBattle/requirments.txt

install-tic-tac-toe:
	@pip install -r hub/TicTacToe/requirments.txt

build:
	@docker build -t bothub .

host:
	@docker run -p 80:5000 bothub
	
client:
	@python scripts/client.py

clear:
	@python scripts/clear.py
	