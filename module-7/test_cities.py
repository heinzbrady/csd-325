import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("santiago", "chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")

    def test_city_country_population_language(self):
        result = city_country("santiago", "chile", 5000000, "spanish")
        self.assertEqual(result, "Santiago, Chile - population 5000000, Spanish")


if __name__ == "__main__":
    unittest.main()