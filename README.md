# 📝 FastAPI Todo App

This is a simple RESTful API built with **FastAPI** that allows users to create, retrieve, update, and delete todo items. It demonstrates basic CRUD operations and uses Pydantic for data validation.

---

## 🚀 Features

- Get all todos
- Get a single todo by ID
- Create a new todo
- Update an existing todo
- Delete a todo

---

## 📁 Project Structure

```bash
.
├── main.py          # FastAPI app with all endpoints
└── models.py        # Pydantic model for the Todo item
```

---

## 🛠️ Requirements

- Python 3.8+
- FastAPI
- Uvicorn

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install fastapi uvicorn
```

---

## ▶️ Running the App

Use the command below to start the FastAPI server:

```bash
uvicorn main:app --reload
```

- The `--reload` flag enables auto-reloading during development.

Once running, the app will be available at:

```text
http://127.0.0.1:8000
```

---

## 🌐 Accessing the API

You can interact with the API in **3 different ways**:

1. **Basic URL:** `http://127.0.0.1:8000`
2. **Swagger UI (interactive docs):** `http://127.0.0.1:8000/docs`
3. **ReDoc UI (alternative docs):** `http://127.0.0.1:8000/redoc`

Both Swagger and ReDoc provide friendly visual environments for testing the API without needing external tools.

---

## 📮 Using Postman (or Other API Clients)

You can also use **Postman** or similar tools to test the API:

- Set the URL to: `http://127.0.0.1:8000/todos`
- Choose the appropriate HTTP method (GET, POST, PUT, DELETE)
- For POST or PUT requests:
  - Go to the **Body** tab
  - Select **raw**
  - Choose **JSON** format
  - Enter a todo in this format:

```json
{
  "id": 1,
  "item": "Start"
}
```

---

## 🔍 Endpoint Overview

| Method | Path               | Description             |
|--------|--------------------|-------------------------|
| GET    | `/todos`           | Get all todos           |
| GET    | `/todos/{todo_id}` | Get a specific todo     |
| POST   | `/todos`           | Create a new todo       |
| PUT    | `/todos/{todo_id}` | Update an existing todo |
| DELETE | `/todos/{todo_id}` | Delete a todo           |

---

## 🧠 How It Works (Developer Notes)

This app is a basic example of a **Receive/Transmit system** with full CRUD support. Here's how things work:

- `main.py` defines all FastAPI routes.
- `models.py` defines the data structure using Pydantic.
- When you run the app using `uvicorn main:app --reload`, FastAPI launches a web server.
- You can use Postman, or interact directly using Swagger UI and ReDoc (auto-generated).

### Example Workflows:
- **GET** a todo: Append its ID to the URL → `http://127.0.0.1:8000/todos/1`
- **PUT** to update: Include the ID in the path and new data in the body
- **POST** new todos: Use JSON format defined in `models.py`

FastAPI's built-in documentation makes testing and learning super friendly.

---

## 🧱 Note

This version uses an **in-memory list** to store todos — meaning data is lost when the app stops. You can expand this by adding a database like SQLite, PostgreSQL, or MongoDB.

---
