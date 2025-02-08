FROM locustio/locust:latest
RUN pip3 install locust-plugins
RUN pip3 install 'locust-plugins[resource]'
