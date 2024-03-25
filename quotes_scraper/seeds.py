import connect
import json
from models import Author, Quote

def load_from_authors_json(filepath):
    with open(filepath, 'r') as fl:
        authors_data = json.load(fl)
    return authors_data

def load_from_qoutes_json(filepath):
    with open(filepath, 'r') as fl:
        qoutes_data = json.load(fl)
    return qoutes_data

def save_authors_to_db(authors_data):
    for author_data in authors_data:
        author = Author(
            fullname = author_data["fullname"],
            born_date = author_data["born_date"],
            born_location = author_data["born_location"],
            description = author_data["description"]
            )
        author.save()

def save_quotes_to_db(quotes_data):
    for quote_data in quotes_data:
        author_fullname = quote_data['author']
        author = Author.objects(fullname=author_fullname).first()
        if author:
            quote = Quote(
                tags=quote_data['tags'],
                author=author_fullname,  # Передаємо повне ім'я автора як рядок
                quote=quote_data['quote']
            )
            quote.save()


if __name__ == "__main__":
    authors_data = load_from_authors_json('authors.json')
    save_authors_to_db(authors_data)

    quotes_data = load_from_qoutes_json('quotes.json')
    save_quotes_to_db(quotes_data)