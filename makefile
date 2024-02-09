.ONESHELL:
SHELL = /bin/zsh
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh

setup: setup-airflow setup-docker setup-conda

setup-airflow:
	mkdir -p ./dags ./logs ./plugins ./config
	echo -e AIRFLOW_UID=$(id -u) > .env

setup-docker:
	docker compose up -d

setup-conda:
	conda create --name rag_agent python=3.11 -y
