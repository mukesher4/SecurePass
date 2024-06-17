FireBaseCredentials: installRequirements
	@echo "Enter Firebase credentials location: "
	@read input; echo $$input > src/credentialsLocation.txt

installRequirements:
	pip install -r src/requirements.txt