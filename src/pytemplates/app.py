import os
import socket

import fastapi

import pytemplates
from pytemplates.core.module1 import greet
from pytemplates.core.module2 import wish_farewell

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return greet(user="PyTemplates User")


@app.get("/hello")
async def hello(user: str):
    return greet(user=user)


@app.get("/goodbye")
async def hello(user: str):
    return wish_farewell(user=user)


@app.get("/whoami")
async def whoami():
    return {
        "host_name": socket.gethostname(),
        "host_ip": socket.gethostbyname(socket.gethostname()),
        "process_id": os.getpid(),
    }


@app.get("/test")
async def test():
    hello = greet(user="PyTemplates User")
    message = f"{hello} PyTemplates has been installed successfully!"
    mypackage_info = f"pytemplates=={pytemplates.__version__}"
    pandas_info = f"fastapi=={fastapi.__version__}"
    goodbye = wish_farewell(user="PyTemplates User")
    final_message = (
        message,
        mypackage_info,
        pandas_info,
        goodbye,
        "Thank you for using PyTemplates!",
    )
    return final_message


if __name__ == "__main__":
    app()
