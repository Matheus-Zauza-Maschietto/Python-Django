from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation(self):
        self.assertEqual(str(self.category), 'Category Testing')

    def test_category_name_max_lenght(self):
        self.category.name = 'a'*66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
