from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTeste(RecipeTestBase):

    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_recipe_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_teste_views_function_is_correct(self):
        view = resolve(reverse('recipes:teste'))
        self.assertIs(view.func, views.teste)

    '''
    OBS: testes que envolver client.get não funcionam, por algum motivo o cliente do django não consegue se conectar ao servidor de desenvolvimento. 
    Problema resolvido, é necesario adicionar dados aos modais de fixtures para que seja retornado algo
    '''

    def test_recipe_home_view_returns_status_code_200_OK(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'), secure=True)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Not Found', response.content.decode('utf-8'))

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']
        self.assertEqual(len(response_recipes), 1)
