#!/usr/bin/env python3
"""
RESTful API - Task 2: Consuming and processing data from an API using Python

This module defines functions to fetch data
from a RESTful API using the `requests` library,
process the JSON response, display post titles,
and save structured data to a CSV file.
"""


import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a specified base URL and prints their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from a specified base URL and saves them to a CSV file.
    """
    list_dict = []
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            list_dict.append(dict)
    with open("posts.csv", "w") as posts:
        writer = csv.DictWriter(posts, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(list_dict)
