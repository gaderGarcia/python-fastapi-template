install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
lint:
	#pylint
test:
	#test
build:
	#build container
deploy:
	#deploy commands
all: install format lint test build deploy