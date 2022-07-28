from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewsTeste(RecipeTestBase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        self.make_recipe()
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertEqual(response, 200)

    def test_recipe_home_view_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(
            response, 'recipes/pages/home.html', secure=True)

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Not Found', response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        self.assertEqual(len(response_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        # Test recipe is_publishd False dont show

        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'not found', response.content.decode('utf-8').lower()
        )
