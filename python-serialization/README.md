Python - Serialization

What is Serialization?

Serialization is the process of converting a Python object into a format that can be stored in a file or transmitted over a network.

Example:

student = {
    "name": "John",
    "age": 20
}

↓

{
    "name": "John",
    "age": 20
}

⸻

What is Deserialization?

Deserialization is the reverse process. It converts a stored JSON representation back into a Python object.

⸻

JSON Functions

Serialization

* json.dumps(obj) → Convert a Python object to a JSON string.
* json.dump(obj, file) → Save a Python object directly to a JSON file.

Deserialization

* json.loads(string) → Convert a JSON string to a Python object.
* json.load(file) → Read a JSON file and return a Python object.

⸻

dump vs dumps

Function	Output
dump()	File
dumps()	String

⸻

load vs loads

Function	Input
load()	File
loads()	String

⸻

Serialization Workflow

Python Object
      │
      ▼
json.dump() / json.dumps()
      │
      ▼
JSON File / JSON String

⸻

Deserialization Workflow

JSON File / JSON String
          │
          ▼
json.load() / json.loads()
          │
          ▼
Python Object

⸻

Why Serialization?

* Store data permanently.
* Exchange data between applications.
* Send data over a network.
* Save application state.

⸻

JSON vs Pickle

JSON	Pickle
Human readable	Binary format
Cross-platform	Python only
Safer	Not safe with untrusted files
Best for APIs	Best for Python objects

⸻

Useful Methods

* __dict__ → Returns the attributes of an object as a dictionary.
* setattr(obj, attr, value) → Dynamically updates an object’s attribute.

⸻

Summary

* Serialization = Python Object → JSON.
* Deserialization = JSON → Python Object.
* Use dump() and load() with files.
* Use dumps() and loads() with strings.
* JSON is the standard format for data exchange between applications.
