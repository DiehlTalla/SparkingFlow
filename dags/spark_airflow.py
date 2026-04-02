from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

with DAG(
    dag_id="sparking_flow",
    default_args={
        "owner": "Deffo Talla",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    start = PythonOperator(
        task_id="start",
        python_callable=lambda: print("Jobs started")
    )

    python_job = SparkSubmitOperator(
        task_id="python_job",
        conn_id="spark_conn",
        application="/opt/airflow/jobs/python/wordcountjob.py",
        dag=dag
    )

    java_job = SparkSubmitOperator(
        task_id="java_job",
        conn_id="spark_conn",
        application="/opt/airflow/jobs/java/spark-job/target/spark-job-1.0-SNAPSHOT.jar",

        java_class = "airscholar.spark",
        dag=dag
    )

    end = PythonOperator(
        task_id="end",
        python_callable=lambda: print("Jobs completed successfully"),
        dag=dag
    )

    start >> [python_job, java_job] >> end