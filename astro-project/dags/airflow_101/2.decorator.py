from airflow.decorators import task, dag
from pendulum import datetime

@dag(
    start_date=datetime(2024, 11, 6),
    schedule=None,
    catchup=False,
)
def decorator_dag():
    @task
    def echo_hello_world():
        print("Hello World")
    echo_hello_world()
    
    @task
    def echo_hello_world_2():
        print("Hello World 2")
    echo_hello_world_2()

    @task
    def echo_hello_world_3():
        print("Hello World 3")
    echo_hello_world_3()
    
decorator_dag()

# Decorators: TaskFlow API decorators wrap Python functions to add additional functionality to the function.
# Decorator: A decorator is a special symbol (@) in Python that adds extra features to your function without changing how the function is written
# @dag decorator is used to define a DAG
# @task decorator is used to define a task in a DAG
