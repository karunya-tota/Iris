import unittest
from recipes_api import *

class TestRecipeAPI(unittest.TestCase):
    """
    Edamam API Test Cases Class
    """
    def test_missing_prefix(self):
        '''
        Tests if the text is processed when the prefix 'Recipe for' is missing
        '''
        text = 'Recipe Tiramisu'
        recipe_name = find_recipe_name(text)
        self.assertIsNone(recipe_name)

        text2 = 'Tiramisu\'s Recipe'
        recipe_name = find_recipe_name(text)
        self.assertIsNone(recipe_name)

    def test_invalid_text(self):
        '''
        Tests if an Invalid Request message is returned for invalid recipe name
        '''
        text = 'Recipe for chickies'
        response = get_recipe(text)
        self.assertEqual(response, "Invalid Request. Check syntax and try again!")

    def test_make_request(self):
        '''
        Tests if a request is successfully made
        '''
        text = 'Recipe for Tiramisu'
        recipe_name = find_recipe_name(text)
        self.assertEqual(recipe_name, 'Tiramisu')

        response = get_recipe(text)
        expected_response = "Recipe:\nIngredients:\n- 4 eggs\n- 4 tablespoons granulated sugar\n- 500 grams of mascarpone\n- 1 cup italian coffee\n- 300 grams of savoiardi (biscuits)\n- 1 bunch bitter cocoa\nCalories: 3474.18\nHealth Labels: Vegetarian, Peanut-Free, Tree-Nut-Free, Soy-Free, Fish-Free, Shellfish-Free"
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
