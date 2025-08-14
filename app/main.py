from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def home():
    pod_name = os.getenv("HOSTNAME", "unknown")
    return {
        "message": "Hello from Kubernetes!",
        "pod": pod_name,
        "host": socket.gethostname()
    }
