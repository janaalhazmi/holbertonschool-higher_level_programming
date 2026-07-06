#!/usr/bin/python3
"""This is for task 2"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):
    """this is class one"""
    def do_GET(self):
        """this is the method"""
        data = {
         "name": "John",
         "age": 30,
         "city": "New York"
        }
        data_2 = {
         "version": "1.0",
         "description": "A simple API built with http.server"
        }
        json2_data = json.dumps(data_2)
        json_data = json.dumps(data)
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('OK'.encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json2_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('Endpoint not found'.encode("utf-8"))
if __name__ == "__main__":
    server = HTTPServer(
              ("",8000),
              MyHandler
             )
    print("Server running on http://localhost:8000")
    server.serve_forever()
