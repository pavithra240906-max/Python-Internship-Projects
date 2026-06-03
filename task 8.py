import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 6):

    url = base_url.format(page)

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"\nScraping Page {page}...\n")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        image = book.find("img")["src"]

        image_url = "http://books.toscrape.com/" + image.replace("../", "")

        book_data = {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "image_url": image_url
        }

        all_books.append(book_data)

        print(book_data)

with open("advanced_books.csv", "w", newline="", encoding="utf-8") as file:

    fieldnames = [
        "title",
        "price",
        "rating",
        "availability",
        "image_url"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(all_books)

with open("advanced_books.json", "w", encoding="utf-8") as file:

    json.dump(all_books, file, indent=4)

print("\nAdvanced scraping completed!")

print("Data saved to advanced_books.csv and advanced_books.json")