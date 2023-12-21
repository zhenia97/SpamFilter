ARGS = $(filter-out $@,$(MAKECMDGOALS))

hello:
	docker compose run -it --rm api echo "Hello world!"
bash:
	docker compose run -it --rm api bash
predict:
	docker compose run -it --rm api python src/predict.py "${ARGS}"
mark-spam:
	docker compose run -it --rm api python src/mark-message.py "${ARGS}" --spam
mark-not-spam:
	docker compose run -it --rm api python src/mark-message.py "${ARGS}" --ham
classifiers-test:
	docker compose run -it --rm api python src/classifiers-test.py

help:
	@echo 'Usage: make [target]'
	@echo 'Available targets:'
	@echo '  help                                   Show this help and exit'
	@echo '  hello                                  Check service setup succesfull'
	@echo '  bash                                   Go to the application container'
	@echo '  predict "your message here"            Predict spam/not spam for your message'
	@echo '  mark-spam "your message here"          Mark your message as spam for train dataset'
	@echo '  mark-not-spam "your message here"      Mark your message as not spam for train dataset'
	@echo '  classifiers-test                       Run classifiers accuracy test'
	@echo ''

%:
	@:
