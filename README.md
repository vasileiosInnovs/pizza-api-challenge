# 🍕 Pizza Restaurant API

A simple Flask API for managing restaurants, pizzas, and their relationships. This API allows users to:

* List restaurants and pizzas
* View individual restaurants
* Delete restaurants
* Assign pizzas to restaurants

---

##  Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd <your-project-folder>
   ```

2. **Install dependencies**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set environment variables**
   Create a `.env` file and add:

   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

4. **Run the Flask server**

   ```bash
   flask run
   ```

---

##  Database Migration & Seeding

1. **Initialize migrations**

   ```bash
   flask db init
   ```

2. **Generate migration**

   ```bash
   flask db migrate -m "Initial migration"
   ```

3. **Apply migration**

   ```bash
   flask db upgrade
   ```

4. **Seed the database**

   ```bash
   python seed.py
   ```

---

##  Route Summary

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| GET    | `/restaurants`          | Get all restaurants          |
| GET    | `/restaurants/<int:id>` | Get a specific restaurant    |
| DELETE | `/restaurants/<int:id>` | Delete a restaurant          |
| GET    | `/pizzas`               | Get all pizzas               |
| POST   | `/restaurant-pizzas`    | Link a pizza to a restaurant |

---

##  Example Requests & Responses

### `GET /restaurants`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Flavor St"
  }
]
```

---

### `GET /restaurants/<id>`

**Response:**

```json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Flavor St"
}
```

**Error (if not found):**

```json
{
  "error": "Restaurant not found"
}
```

---

### `DELETE /restaurants/<id>`

**Response:**

```json
{
  "delete_successful": true,
  "message": "Restaurant deleted."
}
```

---

### `GET /pizzas`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  }
]
```

---

### `POST /restaurant-pizzas`

**Request Body (JSON):**

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response (on success):**

```json
{
  "id": 1,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Error (invalid price):**

```json
{
  "error": "Price must be between 1 and 30"
}
```

**Error (invalid IDs):**

```json
{
  "error": "Invalid pizza or restaurant ID"
}
```

---

##  Validation Rules

* `price` must be between **1 and 30**
* `pizza_id` and `restaurant_id` must reference **existing records**

---

##  Postman Usage

* Import the API collection or manually test endpoints using:

  ```
  Base URL: http://localhost:5555
  ```

* Set method (`GET`, `POST`, `DELETE`)

* For `POST /restaurant-pizzas`:

  * Set Body → raw → JSON
  * Example:

    ```json
    {
      "price": 12,
      "pizza_id": 1,
      "restaurant_id": 2
    }
    ```