import requests
from locust import HttpLocust, TaskSet
from locust import task
from requests import ConnectionError


class Tasks(TaskSet):
    swagger_file = '/swagger.json'
    host = 'http://example:8080/example'

    @task
    def index(self):
        urls = self._get_urls()
        for url in urls:
            self.client.get(url)

    def _get_urls(self):
        try:
            r = requests.get(self.host + self.swagger_file)
        except ConnectionError:
            return []

        else:
            result = r.json()
            paths = list(result.get('paths').keys())
            for path in paths:
                if 'id' in path:
                    paths.remove(path)
            return paths


class WebsiteUser(HttpLocust):
    host = 'http://example:8080/example'
    task_set = Tasks
    min_wait = 5000
    max_wait = 9000
