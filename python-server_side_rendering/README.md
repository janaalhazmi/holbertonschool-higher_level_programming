Server-Side Rendering

📖 Description

This project explores Server-Side Rendering (SSR) using Python and Flask.

Server-Side Rendering is a web development approach where web pages are generated on the server and delivered to the client as fully rendered HTML. Unlike Client-Side Rendering, where JavaScript is responsible for building the page in the browser, SSR allows the server to prepare the content before sending it to the client.

Throughout this project, we work with Flask, Jinja templates, and different data sources to build dynamic and maintainable web applications.

🎯 Learning Objectives

By completing this project, you will learn how to:

* Understand Server-Side Rendering and its role in web development.
* Distinguish between Server-Side Rendering and Client-Side Rendering.
* Build web applications using Flask.
* Create dynamic web pages using the Jinja templating engine.
* Work with HTML templates and dynamic data.
* Read and process data from JSON files.
* Read and process data from CSV files.
* Work with SQLite databases.
* Handle dynamic content and user input.
* Build structured and maintainable server-rendered applications.
* Understand how templates and backend data work together.

🛠️ Technologies

* Python 3
* Flask
* Jinja2
* HTML
* JSON
* CSV
* SQLite
* Git
* Linux / Unix

🧠 Core Concepts

Server-Side Rendering

With SSR, the server generates the HTML page before sending it to the browser.

Client
   ↓
HTTP Request
   ↓
Flask Server
   ↓
Data + Template
   ↓
Rendered HTML
   ↓
Client

Templating

Templates allow HTML pages to contain dynamic values that are filled in by the server.

Template + Data
      ↓
   Jinja
      ↓
Rendered HTML

Data Sources

The application can work with multiple types of data sources:

JSON
CSV
SQLite

This allows applications to separate their presentation layer from their data.

🚀 Getting Started

Clone the repository and navigate to the project directory:

git clone <repository-url>
cd python-server_side_rendering

Make sure Python 3 is installed:

python3 --version

For Flask-based tasks, install Flask if necessary:

pip3 install Flask

Run the required Python files using:

python3 <filename>

📁 Project Structure

The project progressively introduces different components of server-side web development.

A typical structure may look like:

python-server_side_rendering/
│
├── templates/
│   └── *.html
│
├── *.py
├── *.json
├── *.csv
├── *.db
└── README.md

🌐 Why Server-Side Rendering?

SSR provides several advantages:

* SEO-friendly: Search engines can receive fully rendered HTML.
* Initial page rendering: The browser receives ready-to-display content.
* Performance: Less client-side work may be required to display initial content.
* Maintainability: Templates and backend logic can be separated.
* Flexibility: Data can be loaded from different backend sources before rendering.

📚 Resources

* MDN Web Docs — Server-Side Web Development
* Flask Documentation
* Jinja2 Documentation
* Python JSON Documentation
* Python CSV Documentation
* Python SQLite Documentation

👩‍💻 Author

Jana Alhazmi

Holberton School — Higher Level Programming
