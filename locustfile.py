from locust import HttpUser, task


class BenchmarkUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
