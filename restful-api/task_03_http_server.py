#!/usr/bin/python3
"""this is document"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class API(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                    }
            datav1 = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(datav1.encode("utf-8"))

        elif self.path == "/info":
            datam1 = {"version": "1.0", "description": "A simple API built with http.server"}
            datamv1 = json.dumps(datam1)
 	    self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(datamv1.encode("utf-8"))
        else:
            self.send_response(404)
 	    self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
    def run(server_class = HTTPServer, handle_class = API):
	server = ("", 8080)
	httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
if __name__ == "__main__":
	run()
