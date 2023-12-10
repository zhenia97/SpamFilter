hello:
	docker compose run -it --rm api echo "Hello world!"
bash:
	docker compose run -it --rm api bash
run-predict:
	docker compose run -it --rm api python src/predict.py "casino free dollars call me"

help:
	@echo 'Usage: make [target]'
	@echo 'Available targets:'
	@echo '  help                              Show this help and exit'
	@echo '  hello                             Check service setup succesfull'
	@echo '  bash                              Go to the application container)'
	@echo '  run-predict "your message here"   Predict spam/not spam for your message'
	@echo ''