---
title: "FastAPI"
source: https://en.wikipedia.org/wiki/Uvicorn
domain: uvicorn-asgi
license: CC-BY-SA-4.0
tags: python uvicorn, uvicorn asgi server, asgi worker python
fetched: 2026-07-02
---

# FastAPI

(Redirected from

Uvicorn

)

**FastAPI** is a web framework for building HTTP-based service APIs in Python 3.8+. It uses Pydantic and type hints to validate, serialize and deserialize data. FastAPI also automatically generates OpenAPI documentation for APIs built with it. It was first released in 2018.

## Components

### Pydantic

Pydantic is a data validation library for Python. While writing code in an IDE, Pydantic provides type hints based on annotations. FastAPI extensively utilizes Pydantic models for data validation, serialization, and automatic API documentation. These models are using standard Python type hints, providing a declarative way to specify the structure and types of data for incoming requests (e.g., HTTP bodies) and outgoing responses.

```mw
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.post("/items/")
def create_item(item: Item):
    # The 'item' object is already validated and typed
    return {"message": "Item received", "item_name": item.name}
```

### Starlette

Starlette is a lightweight ASGI framework/toolkit, to support async functionality in Python.

### Uvicorn

Uvicorn is a minimal low-level server/application web server for async frameworks, following the ASGI specification. Technically, it implements a multi-process model with one main process, which is responsible for managing a pool of worker processes and distributing incoming HTTP requests to them. The number of worker processes is pre-configured, but can also be adjusted up or down at runtime.

### OpenAPI integration

FastAPI automatically generates OpenAPI documentation for APIs. This documentation includes both Swagger UI and *ReDoc*, which provide interactive API documentation that you can use to explore and test your endpoints in real time. This is particularly useful for developing, testing, and sharing APIs with other developers or users. Swagger UI is accessible by default at **/docs** and ReDoc at **/redoc** route.

## Features

### Asynchronous operations

FastAPI's architecture inherently supports asynchronous programming. This design allows the single-threaded event loop to handle a large number of concurrent requests efficiently, particularly when dealing with I/O-bound operations like database queries or external API calls. For reference, see async/await pattern.

### Dependency injection

FastAPI incorporates a Dependency Injection (DI) system to manage and provide services to HTTP endpoints. This mechanism allows developers to declare components such as database sessions or authentication logic as function parameters. FastAPI automatically resolves these dependencies for each request, injecting the necessary instances.

```mw
from fastapi import Depends, HTTPException, status
from db import DbSession

# --- Dependency for Database Session ---
def get_db():
    db = DbSession()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(name: str, description: str, db: DbSession = Depends(get_db)):
    new_item = Item(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"message": "Item created successfully!", "item": new_item}

@app.get("/items/{item_id}")
def read_item(item_id: int, db: DbSession = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
```

### WebSockets support

WebSockets allow full-duplex communication between a client and the server. This capability is fundamental for applications requiring continuous data exchange, such as instant messaging platforms, live data dashboards, or multiplayer online games. FastAPI leverages the underlying Starlette implementation, allowing for efficient management of connections and message handling.

```mw
# You must have 'websockets' package installed
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

### Background tasks

FastAPI enables the execution of background tasks after an HTTP response has been sent to the client. This allows the API to immediately respond to user requests while simultaneously processing non-critical or time-consuming operations in the background. Typical applications include sending email notifications, updating caches, or performing data post-processing.

```mw
import time
import shutil
from fastapi import BackgroundTasks, UploadFile, File
from utils import generate_thumbnail

@app.post("/upload-image/")
async def upload_image(
    image: UploadFile = File(...),
    background_tasks: BackgroundTasks
):
    file_location = f"uploaded_images/{image.filename}"
    # Save uploaded image
    with open(image_path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    # Add thumbnail generation as a background task
    background_tasks.add_task(generate_thumbnail, file_location, "200x200")

    return {"message": f"Image '{image.filename}' uploaded. Thumbnail generation started in background."}
```

## Example

The following code shows a simple web application that displays "Hello, World!" when visited:

```mw
# Import FastAPI class from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Define a GET route for the root URL ("/")
@app.get("/")
async def read_root() -> str:
    # Return a plain text response
    return "Hello, World!"
```
