extract:
	python fluotracker/extraction/run_extraction.py

install: venv-fluo requirements.txt
	source activate.sh && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

notebook:
	source activate.sh && \
	jupyter notebook

venv-fluo:
	python3 -m venv venv-fluo
