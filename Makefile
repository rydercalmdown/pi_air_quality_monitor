PI_IP_ADDRESS=192.168.1.10
PI_USERNAME=pi

.PHONY: run
run:
	@docker-compose up

.PHONY: install
install:
	@cd scripts && bash install.sh

.PHONY: copy
copy:
	@rsync -a $(shell pwd) --exclude env $(PI_USERNAME)@$(PI_IP_ADDRESS):/home/$(PI_USERNAME)

.PHONY: shell
shell:
	@ssh $(PI_USERNAME)@$(PI_IP_ADDRESS)

.PHONY: build
build:
	@docker-compose build
