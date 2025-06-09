#!/usr/bin/env python3
"""
RESTful API - Task 2: Consuming and processing data from an API using Python

This module defines functions to fetch data
from a RESTful API using the `requests` library,
process the JSON response, display post titles,
and save structured data to a CSV file.

Author: [Your Name Here]
"""


import requests
import csv


def fetch_and_print_posts():
    # - Effectuer une requête GET vers l'API JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # - Afficher le status code (Status Code: 200 par exemple)
    print("Status code:", response.status_code)
    # - Si le status code est 200 :
    if response.status_code == 200:
        # - Parser la réponse en JSON
        data = response.json()
        # - Itérer sur la liste des posts
        for post in data:
            # - Pour chaque post, afficher le titre uniquement
            print(post["title"])


def fetch_and_save_posts():
    list_dict = []
    # - Effectuer une requête GET vers l'API JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    # - Si le status code est 200 :
    if response.status_code == 200:
        # - Parser la réponse en JSON
        data = response.json()
        # - Créer une liste de dictionnaires avec les clés : id, title, body
        for post in data:
            dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            list_dict.append(dict)
    # - Ouvrir un fichier posts.csv en mode écriture
    with open("posts.csv", "w") as posts:
        # - Utiliser csv.DictWriter pour écrire les données
        writer = csv.DictWriter(posts, fieldnames=["id", "title", "body"])
        # - Écrire l'en-tête (fieldnames)
        writer.writeheader()
        # - Écrire les lignes du fichier CSV à partir de la liste
        # de dictionnaires
        writer.writerows(list_dict)
