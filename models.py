from mongoengine import Document, CASCADE
from mongoengine.fields import ListField, StringField, DateField, ReferenceField


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = DateField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=20))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()