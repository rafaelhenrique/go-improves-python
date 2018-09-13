
clean:
	@echo "--> Cleaning C files"
	@rm -rf *.c *.h *.so
	@echo "--> Cleaning pyc files"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".benchmarks" -type d | xargs rm -rf

benchmark:
	@LD_LIBRARY_PATH="." pytest --benchmark-only

test:
	@LD_LIBRARY_PATH="." pytest --benchmark-skip

