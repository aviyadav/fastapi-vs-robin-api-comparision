# File name : locustfile.py

from locust import HttpUser, task, between

class LocalApiUser(HttpUser):
    # Minimal wait time between tasks to allow max throughput controlled by the CLI
    wait_time = between(0.1, 0.5)

    @task
    def test_get(self):
        """GET request script"""
        self.client.get("/health")

    @task
    def test_post(self):
        """POST request script"""
        headers = {"Content-Type": "application/json"}
        payload = {"status": "testing"}
        self.client.post("/post", json=payload, headers=headers)