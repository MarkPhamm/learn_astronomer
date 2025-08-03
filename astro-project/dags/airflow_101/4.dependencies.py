from airflow.decorators import task, dag
from airflow.models.baseoperator import chain
from pendulum import datetime

@dag(
    start_date=datetime(2024, 11, 6),
    schedule=None,
    catchup=False,
)
def dependencies_dag():
    @task
    def task_1():
        print("Doing Task 1")
    
    @task
    def task_2():
        print("Doing Task 2")

    @task
    def task_3():
        print("Doing Task 3")
    
    @task
    def task_4():
        print("Doing Task 4")
    
    @task
    def task_5():
        print("Doing Task 5")
    
    @task
    def task_6():
        print("Doing Task 6")

    # Call each task once and store the instances
    t1 = task_1()
    t2 = task_2()
    t3 = task_3()
    t4 = task_4()
    t5 = task_5()
    t6 = task_6()   

    # Set up dependencies using the task instances
    chain(t1, [t2, t3], [t4, t5], t6)
    
dependencies_dag()