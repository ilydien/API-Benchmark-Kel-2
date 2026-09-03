from locust import HttpUser, task


class BenchmarkUser(HttpUser):
    @task
    def index(self):
        self.client.get("/files/file_1kb.txt")
