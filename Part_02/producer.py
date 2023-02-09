import pika

from models import Contacts
from seeds import create_data


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sms_list')
    channel.queue_declare(queue='email_list')

    contacts = Contacts.objects()
    for contact in contacts:
        if contact.notification_priority:
            channel.basic_publish(exchange='', routing_key='email_list', body=f'{contact.id}'.encode())
        else:
            channel.basic_publish(exchange='', routing_key='sms_list', body=f'{contact.id}'.encode())

    connection.close()


if __name__ == '__main__':
    create_data()
    main()
