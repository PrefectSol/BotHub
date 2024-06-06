install: install-hub install-seabattle install-tic-tac-toe

build: build-platform

install-hub:
	@pip install -r requirements.txt

install-seabattle:
	@pip install -r hub/SeaBattle/requirements.txt

install-tic-tac-toe:
	@pip install -r hub/TicTacToe/requirements.txt

build-platform:
	@docker build -t bothub-platform .

# host:
# 	@docker run -p 80:5000 bothub
	
client:
	@python scripts/client.py

clear:
	@python scripts/clear.py

rmdb:
	@sudo rm -rf platform/database/*
	
start:
	@python platform/control/start.py $(filter-out $@,$(MAKECMDGOALS))

stop:
	@python platform/control/stop.py $(filter-out $@,$(MAKECMDGOALS))

status:
	@python platform/control/status.py $(filter-out $@,$(MAKECMDGOALS))

enable-net:
	@python platform/control/enable_net.py $(filter-out $@,$(MAKECMDGOALS))

disable-net:
	@python platform/control/disable_net.py $(filter-out $@,$(MAKECMDGOALS))
