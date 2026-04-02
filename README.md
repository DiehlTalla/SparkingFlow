# Apache Airflow on Steroids with Java and Python
This project orchestrates Spark jobs written in different programming languages using Apache Airflow, all within a Dockerized environment. The DAG sparking_flow is designed to submit Spark jobs written in Python and Java, ensuring that data processing is handled efficiently and reliably on a daily schedule.
# Project Structure
The DAG sparking_flow includes the following tasks:

- start: A PythonOperator that prints "Jobs started".

- python_job: A SparkSubmitOperator that submits a Python Spark job.

- java_job: A SparkSubmitOperator that submits a Java Spark job.

- end: A PythonOperator that prints "Jobs completed successfully".

  These tasks are executed in a sequence where the start task triggers the Spark jobs in parallel, and upon their completion, the end task is executed.

  # Docker Setup
  To run this project using Docker, follow these steps:

1.Clone this repository to your local machine.

2.Navigate to the directory containing the docker-compose.yml file.

3.Build and run the containers using Docker Compose:

docker-compose up -d --build

4.This command will start the necessary services defined in your docker-compose.yml, such as Airflow webserver, scheduler, Spark master, and worker containers.

# Directory structure for jobs 

Ensure your Spark job files are placed in the following directories and are accessible to the Airflow container:

- Python job: jobs/python/wordcountjob.py

- Java job: jobs/java/spark-job/target/spark-job-1.0-SNAPSHOT.jar
  
These paths should be relative to the mounted Docker volume for Airflow DAGs.

# Usage 
After the Docker environment is set up, the sparking_flow DAG will be available in the Airflow web UI localhost:8080, where it can be triggered manually or run on its daily schedule.

# The DAG will be execute the following steps 

- Print "Jobs started" in the Airflow logs.
- Submit the Python Spark job to the Spark cluster.
- Submit the Java Spark job to the Spark cluster.
- Print "Jobs completed successfully" in the Airflow logs after all jobs have finished.
  
# Note:
You must add the spark cluster url to the spark connection in the configuration on Airflow UI


