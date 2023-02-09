from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField


class Contacts(Document):
    fullname = StringField()
    email = EmailField()
    phone = StringField()
    notified = BooleanField()
