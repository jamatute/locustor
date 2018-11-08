import requests
from locust import HttpLocust, TaskSet
from locust import task


class Tasks(TaskSet):
    swagger_file = '/swagger.json'
    host = 'http://pre-saigon-int.lowi.es:8080/bundle'

    @task
    def index(self):
        urls = self._get_urls()
        for url in urls:
            self.client.get(url)

    def _get_urls(self):
        # import ipdb; ipdb.set_trace()
        r = requests.get(self.host + self.swagger_file)
        result = r.json()
        paths = list(result.get('paths').keys())
        for path in paths:
            if 'id' in path:
                paths.remove(path)
        return paths


class WebsiteUser(HttpLocust):
    host = 'http://pre-saigon-int.lowi.es:8080/bundle'
    task_set = Tasks
    min_wait = 5000
    max_wait = 9000
