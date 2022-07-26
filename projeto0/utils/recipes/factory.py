# from inspect import signature
from random import randint
from string import digits

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'id': None,
        'tittle': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'slug': 'receita-qualquer',
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'preparation_steps_is_html': False,
        'created_at': fake.date_time(),
        'is_published': True,
        'cover': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        'category': 1,
        'author': 1

    }


def make_category():
    return {'name': fake.word()}


def make_user():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
