from distutils.log import error

from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.tittle = 'a'*70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_title_raises_error_if_description_has_more_than_165_chars(self):
        self.recipe.description = 'a'*170
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_title_raises_error_if_preparation_time_unit_has_more_than_65_chars(self):
        self.recipe.preparation_time_unit = 'a'*70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_title_raises_error_if_servings_unit_has_more_than_65_chars(self):
        self.recipe.servings_unit = 'a'*70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
