from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta, datetime

default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 28),
    "email": ["jeremy.lott@extendhealth.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    "demo",
    description="demo some stuff",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
) as dag:
    first_task = DummyOperator(task_id="first_task")
    final_task = DummyOperator(task_id="final_task")


first_task >> final_task