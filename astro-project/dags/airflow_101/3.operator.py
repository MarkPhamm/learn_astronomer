from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pendulum import datetime

@dag(
    start_date=datetime(2024, 11, 6),
    schedule=None,
    catchup=False,
)
def operator_dag():
    bash_task = BashOperator(
        task_id="print_hello_world_bash",
        bash_command="echo 'Hello World from BashOperator'"
    )

    python_task = PythonOperator(
        task_id="print_hello_world_python",
        python_callable=lambda: print("Hello World from PythonOperator")
    )

    bash_task >> python_task

operator_dag()

# Operators: Operators are the building blocks of DAGs. They are used to perform specific tasks.
# BashOperator: Executes a bash command.
# PythonOperator: Executes a Python function.
