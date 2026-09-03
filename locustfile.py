from locust import HttpUser, task
import locust.stats

locust.stats.PERCENTILES_TO_REPORT = [0.50, 0.90, 0.95, 0.99]
locust.stats.PERCENTILES_TO_CHART = [0.50, 0.90, 0.95, 0.99]


class BenchmarkUser(HttpUser):
    @task
    def index(self):
        self.client.get("/files/file_1kb.txt")
