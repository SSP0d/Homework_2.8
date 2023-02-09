import redis
from redis_lru import RedisLRU

from models import Authors, Quotes
import connect

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def inpup_check(command) -> dict:
    args = command.split(':')
    key = args[0] if len(command.split(':')) > 1 else command.strip()
    value = args[-1].strip().split(',') if len(command.split(':')) > 1 else ''
    return {key: value}


@cache
def find_quotes_to_name(name):
    author_name = ''
    all_quotes = []
    quotes = Quotes.objects()
    for quote in quotes:
        if quote.author.fullname.lower() == name.lower()\
                or quote.author.fullname.lower().startswith(name.lower()):
            author_name = quote.author.fullname
            all_quotes.append(quote.quote)
    return f'All quotes by "{author_name}": {", ".join(el for el in all_quotes)}'


@cache
def find_quote_to_tag(tag_to_search) -> list:
    all_quotes = []
    quotes = Quotes.objects()
    for quote in quotes:
        for tag in quote.tags:
            if tag.startswith(tag_to_search):
                all_quotes.append(f'Quote by "{quote.author.fullname}" with tag "{tag}": {quote.quote}')
    return all_quotes


def main():
    while True:
        command: str = input("Enter query(command:values): ")

        if command.lower() == 'exit':
            break

        else:
            commands = inpup_check(command)

            if 'name' in commands:
                for name in commands['name']:
                    print(find_quotes_to_name(name))

            if 'tag' in commands:
                for value in commands['tag']:
                    print(f'{",".join([el for el in find_quote_to_tag(value)])}')

            if 'tags' in commands:
                for value in commands['tags']:
                    print(f'{",".join([el for el in find_quote_to_tag(value)])}')


if __name__ == '__main__':
    main()
