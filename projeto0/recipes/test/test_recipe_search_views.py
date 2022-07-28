
from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeSearchViewsTeste(RecipeTestBase):
    '''
    OBS: testes que envolver client.get não funcionam, por algum motivo o cliente do django não consegue se conectar ao servidor de desenvolvimento.
    Problema resolvido, é necesario adicionar dados aos modais de fixtures para que seja retornado algo
    '''

    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search')+'?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_in_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=Teste'
        response = self.client.get(url)
        self.assertIn(
            'search for &quot;Teste&quot;',
            response.content.decode('utf-8')
        )
