env:
	mkdir -p ./dags ./logs ./plugins ./config
	echo -e AIRFLOW_UID=$(id -u) > .env

setup:
	docker compose up -d
	docker exec -rm -i rag_agent psql -u root -ppassword <mydb> < sqls/agent-database.sql
