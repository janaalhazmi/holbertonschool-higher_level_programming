# Python - Object Relational Mapping

## Description

This project introduces Object Relational Mapping (ORM) in Python using both **MySQLdb** and **SQLAlchemy**.

The project demonstrates how Python applications interact with MySQL databases by executing SQL queries directly and by using an ORM to manipulate database objects without writing raw SQL.

---

## Learning Objectives

By completing this project, I learned:

- How to connect Python to a MySQL database.
- How to execute SQL queries using MySQLdb.
- How to retrieve and manipulate database records.
- How to prevent SQL Injection attacks.
- The difference between raw SQL and Object Relational Mapping (ORM).
- How to use SQLAlchemy to create database models.
- How to query, insert, update, and delete records using SQLAlchemy.
- Best practices for database programming in Python.

---

## Requirements

- Ubuntu 24.04 LTS
- Python 3.12
- MySQL 8.0
- MySQLdb (mysqlclient)
- SQLAlchemy
- pycodestyle 2.8.*
- MySQL Server

---

## Project Structure

```
python-object_relational_mapping/
│
├── 0-select_states.py
├── 1-filter_states.py
├── 2-my_filter_states.py
├── 3-my_safe_filter_states.py
├── 4-cities_by_state.py
├── 5-filter_cities.py
├── model_state.py
├── 6-model_state.py
├── 7-model_state_fetch_all.py
├── 8-model_state_fetch_first.py
├── 9-model_state_filter_a.py
├── 10-model_state_my_get.py
├── 11-model_state_insert.py
├── 12-model_state_update_id_2.py
├── 13-model_state_delete_a.py
├── model_city.py
├── 14-model_city_fetch_by_state.py
└── README.md
```

---

## Technologies Used

- Python
- MySQL
- MySQLdb
- SQLAlchemy
- SQL
- Object Relational Mapping (ORM)

---

## Topics Covered

### MySQLdb

- Database connection
- Cursor object
- SQL execution
- Fetching query results
- Closing connections

### SQLAlchemy

- Declarative Base
- Engine
- Session
- Models
- Relationships
- CRUD Operations

---

## Security

One of the objectives of this project is learning how to prevent SQL Injection attacks by using parameterized queries instead of concatenating user input into SQL statements.

---

## Tasks

| Task | Description |
|------|-------------|
| 0 | Get all states |
| 1 | Filter states |
| 2 | Filter states by user input |
| 3 | SQL Injection prevention |
| 4 | Cities by states |
| 5 | All cities by state |
| 6 | First SQLAlchemy model |
| 7 | Fetch all states using SQLAlchemy |
| 8 | Fetch first state |
| 9 | States containing the letter 'a' |
| 10 | Get a specific state |
| 11 | Insert a new state |
| 12 | Update an existing state |
| 13 | Delete states containing 'a' |
| 14 | Display cities by state |

---

## Installation

Install MySQLdb:

```bash
pip3 install mysqlclient
```

Install SQLAlchemy:

```bash
pip3 install SQLAlchemy
```

---

## Example

```bash
python3 0-select_states.py root password hbtn_0e_0_usa
```

---

## Author

**Jana Alhazmi**
