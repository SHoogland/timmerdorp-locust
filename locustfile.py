from locust_plugins.users.resource import HttpUserWithResources
from locust import task

class TestUserWithResources(HttpUserWithResources):
    # these values can be overridden
    # bundle_resource_stats=False
    # default_resource_filter=".*[^(js)]$"
    @task
    def include_resources_default(self):
        self.client.get("/")

    @task
    def include_no_resources(self):
        self.client.get("https://api.timmerdorp.com/1/", include_resources=False)

# from locust_plugins.users import HttpUserWithResources
# from locust import task


# class TestUserWithResources(HttpUserWithResources):
#     # these values can be overridden
#     # bundle_resource_stats=False
#     # default_resource_filter=".*[^(js)]$"
#     @task
#     def include_resources_default(self):
#         self.client.get("/")

# # import time
# # from locust import HttpUser, task, between

# # class QuickstartUser(HttpUser):
# #     wait_time = between(1, 5)

# #     @task
# #     def hello_world(self):
# #         self.client.get("/")

# #     # @task(3)
# #     # def view_items(self):
# #     #     for item_id in range(10):
# #     #         self.client.get(f"/item?id={item_id}", name="/item")
# #     #         time.sleep(1)

# #     # def on_start(self):
# #     #     self.client.post("/login", json={"username":"foo", "password":"bar"})

# import time
# from locust import HttpUser, task, between

# class QuickstartUser(HttpUser):
#     wait_time = between(1, 5)

#     @task
#     def hello_world(self):
#         self.client.get("/hello")
#         self.client.get("/world")

#     @task(3)
#     def view_items(self):
#         for item_id in range(10):
#             self.client.get(f"/item?id={item_id}", name="/item")
#             time.sleep(1)

#     def on_start(self):
#         self.client.post("/login", json={"username":"foo", "password":"bar"})