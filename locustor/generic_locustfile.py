from locust import HttpLocust, TaskSet
from locust import task


class Tasks(TaskSet):

    @task
    def index(self):
        self.client.get('/')


class WebsiteUser(HttpLocust):
    task_set = Tasks
    min_wait = 5000
    max_wait = 9000
