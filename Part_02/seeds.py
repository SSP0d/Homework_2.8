from random import randint

from faker import Faker

from models import Contacts


fake = Faker('uk_UA')


def create_data():
    for _ in range(30):
        record = Contacts(
            fullname=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            notified=False,
            notification_priority=bool(randint(0, 1))

        )
        record.save()
