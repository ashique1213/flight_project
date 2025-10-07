# Flight Routes System (Django Machine Test)

## Overview

A simple Django web application to manage and analyze airport flight routes.
This project is designed as a **machine test** covering:

1. Adding Airports
2. Adding Routes
3. Finding the **Nth Left/Right Node** in a route
4. Displaying the **Longest Route**
5. Displaying the **Shortest Route** between two airports

---

## Tech Stack

* Python 3.10+
* Django 4.x
* SQLite (default)
* HTML (no CSS required)

---

## Setup Instructions

### 1️ Clone or Create Project

```bash
django-admin startproject flight_project
cd flight_project
python manage.py startapp flights
```

Copy all provided code files into the `flights/` app.

---

### 2️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 3️ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 4️ Run Server

```bash
python manage.py runserver
```

Then open the app in your browser:
 [http://127.0.0.1:8000/)

---

## URL Endpoints

| URL                     | Description                              |
| ----------------------- | ---------------------------------------- |
| `/`             | Home page with links to all features     |
| `/add-airport/` | Add new airports                         |
| `/add-route/`   | Add new flight routes                    |
| `/nth-node/`    | Find Nth Left or Right Node in routes    |
| `/longest/`     | Show route with longest duration         |
| `/shortest/`    | Show shortest route between two airports |

---

## Features Summary

### 1. Add Airport

Add airports with their **code** and **name**.

### 2. Add Route

Define routes between airports with **position** (order in path) and **duration (hours)**.

### 3. Find Nth Left or Right Node

Search from a starting airport to find the route **N steps left or right** based on position order.

### 4. Longest Route

Displays the route with the **maximum duration**.

### 5. Shortest Route Between Two Airports

Finds and displays the route with the **shortest duration** between selected airports.

---

## Test Data


## Optional — Load Test Data Quickly

Run this in Django shell:

```bash
python manage.py shell
```

Paste:

```python
from flights.models import Airport, Route

airports = [
    ('DEL', 'Indira Gandhi International Airport'),
    ('BOM', 'Chhatrapati Shivaji International Airport'),
    ('BLR', 'Kempegowda International Airport'),
    ('DXB', 'Dubai International Airport'),
    ('DOH', 'Hamad International Airport'),
    ('LHR', 'London Heathrow Airport'),
    ('JFK', 'John F. Kennedy International Airport'),
    ('SIN', 'Singapore Changi Airport'),
    ('SYD', 'Sydney Kingsford Smith Airport'),
    ('HKG', 'Hong Kong International Airport'),
]

for code, name in airports:
    Airport.objects.get_or_create(code=code, name=name)

routes = [
    ('DEL', 'DXB', 1, 3.8),
    ('DXB', 'LHR', 2, 7.0),
    ('LHR', 'JFK', 3, 7.5),
    ('JFK', 'SYD', 4, 20.0),
    ('DEL', 'BOM', 5, 2.0),
    ('BOM', 'BLR', 6, 1.5),
    ('BLR', 'SIN', 7, 5.0),
    ('SIN', 'HKG', 8, 3.5),
    ('HKG', 'DOH', 9, 8.0),
    ('DOH', 'DXB', 10, 1.0),
]

for src, dest, pos, dur in routes:
    Route.objects.get_or_create(
        source=Airport.objects.get(code=src),
        destination=Airport.objects.get(code=dest),
        position=pos,
        duration=dur
    )

print("Test data added successfully!")
```

---

## Example Test Cases

1️⃣ **Find Nth Node:**
Start Airport: `DXB`, Direction: Right, N = 2
➡️ Result → `LHR → JFK (7.5 hrs)`

2️⃣ **Longest Route:**
➡️ `JFK → SYD (20.0 hrs)`

3️⃣ **Shortest Route (Between DOH and DXB):**
➡️ `DOH → DXB (1.0 hrs)`
