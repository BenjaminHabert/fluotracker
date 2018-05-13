extract:
	python fluotracker/extraction/run_extraction.py

install:
	source activate.sh && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

notebook:
	source activate.sh && \
	jupyter notebook
