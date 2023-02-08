import json
from random import choice

from models import Authors, Quotes


def json_load(filename):
    with open(filename, 'r', encoding='utf-8') as fd:
        data = json.load(fd)
        return data


def add_authors(filename):
    data: dict = json_load(filename)
    for el in data:
        record = Authors(
            fullname=el['fullname'],
            born_date=el['born_date'],
            born_location=el['born_location'],
            description=el['description']
        )
        record.save()


def add_quotes(filename):
    authors = Authors.objects()
    data: dict = json_load(filename)
    for el in data:
        record = Quotes(
            tags=el['tags'],
            author=choice(authors).id,
            quote=el['quote']
        )
        record.save()


if __name__ == '__main__':
    add_authors('authors.json')
    add_quotes('qoutes.json')
