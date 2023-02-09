from mongoengine import Document, connect
from mongoengine.fields import StringField, EmailField, BooleanField


connect(host="mongodb://127.0.0.1:27017/mongo_db_hw28")


class Contacts(Document):
    fullname = StringField()
    email = EmailField()
    phone = StringField()
    notified = BooleanField()
    notification_priority = BooleanField()
