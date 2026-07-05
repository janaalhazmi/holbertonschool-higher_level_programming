#!/usr/bin/python3
"""this the task 02"""
import requests
import csv



def fetch_and_print_posts():
    """the function one"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from the API and save them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        listdata =[]
        for post in data:
            listdata.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(listdata)
