install: install-hub install-seabattle install-tic-tac-toe

build: build-platform

install-hub:
	@pip install -r requirements.txt

install-seabattle:
	@pip install -r hub/SeaBattle/requirements.txt

install-tic-tac-toe:
	@pip install -r hub/TicTacToe/requirements.txt

build-platform:
	@docker build -t bothub-platform platform/

host:
	@docker run -p 80:5000 bothub
	
client:
	@python scripts/client.py

clear:
	@python scripts/clear.py
	
start:
	@python platform/control/start.py --config platform/platform-config.json

stop:
	@python platform/control/stop.py --config platform/platform-config.json

status:
	@python platform/control/status.py --config platform/platform-config.json
