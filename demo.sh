docker build --rm -t tl-airflow:local .

docker run -p 8080:8080 tl-airflow:local