from django.contrib.auth.models import User
from django.test import TestCase
from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_user(
        self, first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='user@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,)

    def make_recipe(
        self,
        category=None,
        author=None,
        tittle='Recipe Title',
        description='Recipe Description',
        slug='recipe-slug',
        preparation_time=10,
        preparation_time_unit='Minutos',
        servings=5,
        servings_unit='Porções',
        preparation_steps='Recipe Preparation Steps',
        preparation_steps_is_html=False,
        is_published=True,
        cover=r'projeto0/recipes/covers/2022/07/07/MRS_9135.JPG',
    ):
        if category == None:
            category = {}

        if author == None:
            author = {}

        return Recipe.objects.create(
            category=self.make_category(**category),
            author=self.make_user(**author),
            tittle=tittle,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover,
        )
