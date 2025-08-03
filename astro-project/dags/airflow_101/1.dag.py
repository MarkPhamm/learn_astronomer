from airflow.decorators import dag, task
from pendulum import datetime
from datetime import timedelta

@dag(
    start_date=datetime(2024, 11, 6), # date after which the DAG can be scheduled, set to None by default
    schedule=None, # see: https://www.astronomer.io/docs/learn/scheduling-in-airflow for options
    catchup=False, # if True, the DAG will run all missed runs
    tags=["airflow_101"], # add tags in the UI 
    description="This is a simple DAG that prints 'Hello World'", # add description in the UI
    default_args={
        "retries": 0, # number of retries if the task fails
        "retry_delay": timedelta(seconds=10), # delay between retries
    }
)
def example_dag():
    @task
    def my_task():
        print("Hello World")    
    my_task()

example_dag()