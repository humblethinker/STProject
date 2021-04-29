import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/account/inbox")
        self.client.get("/account")
        self.client.get("/nc_details")

    def on_start(self):
        self.client.post("/account/login#tab-login", json={"username":"ewfrtrtjje@sammdmk.ac.in", "password":"Abcdefgh"})