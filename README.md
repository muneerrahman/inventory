# Product Inventory API

A simple API built with **Django REST Framework** to manage products.  

---

## Features
- List all products
- Add a new product
- Update a product
- Delete a product
- Product price cannot be negative

---

## Tech Stack
- Python 3.x
- Django 6.0
- Django REST Framework 3.16
- SQLite (default)

---

## Setup

```bash
git clone https://github.com/muneerrahman/inventory.git
cd inventory
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
Server runs at: http://127.0.0.1:8000/

## API Examples

POST /api/products/

{
  "name": "Laptop",
  "price": 50000.00,
  "stock": 10
}

PUT /api/products/{id}/

{
  "name": "Laptop Pro",
  "price": 55000.00,
  "stock": 8
}
