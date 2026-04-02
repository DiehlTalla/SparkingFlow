FROM apache/airflow:2.7.1-python3.11

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-11-jdk \
        gcc \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

USER airflow

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.11.txt" \
    -r /requirements.txt

# Recréer le binaire airflow s'il a été supprimé
RUN python -c "import airflow" && \
    echo '#!/usr/bin/env python' > /home/airflow/.local/bin/airflow && \
    echo 'from airflow.__main__ import main' >> /home/airflow/.local/bin/airflow && \
    echo 'main()' >> /home/airflow/.local/bin/airflow && \
    chmod +x /home/airflow/.local/bin/airflow

USER root
RUN ln -sf /home/airflow/.local/bin/airflow /usr/local/bin/airflow

USER airflow

WORKDIR /opt/airflow