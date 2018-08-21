test: 
	@LD_LIBRARY_PATH="./go_version/" py.test go_version/sum_numbers.py

clean:
	@echo "--> Cleaning pyc files"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".benchmarks" -type d | xargs rm -rf
	@echo ""

