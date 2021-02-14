"""  """

from researches.controllers.openfoodfacts_api import ApiOff

off_api = ApiOff()

# CONSTANTS
PAGE = 1
PAGE_SIZE = 2

print(PAGE)
print(PAGE_SIZE)


def test_openfoodfacts_api():
    """ Test controllers result for page 1 with 2 product."""
    req = off_api.api_connection(PAGE, PAGE_SIZE)
    result = [{
        'stores_tags': ['carrefour', 'auchan', 'leclerc'],
        'code': '3274080005003', 'nutriments':
            {'sugars_unit': 'g', 'nitrate_100g': '0.001',
             'sodium_100g': '0.011', 'energy_100g': 0,
             'ph_unit': 'g', 'carbohydrates_100g': 0,
             'energy-kcal_value': 0, 'chloride_unit': 'mg',
             'salt': '0.0275', 'bicarbonate_label': 'Bicarbonate',
             'silica_label': 'Silice', 'energy': 0,
             'bicarbonate_unit': 'mg', 'fat': 0, 'energy-kj': 0,
             'sodium': '0.011', 'chloride': '5e-06',
             'energy-kj_unit': 'kJ', 'potassium': '1.5e-06',
             'magnesium_100g': '2.5e-05', 'carbohydrates_unit': 'g',
             'energy-kj_100g': 0, 'chloride_value': '0.005',
             'nitrate_label': 'Nitrate', 'calcium_100g': '3.9e-05',
             'salt_value': '0.0275', 'nutrition-score-fr_100g': 0,
             'sulfate_unit': 'mg', 'sodium_value': '0.011',
             'calcium_value': '0.039', 'ph_label': 'pH',
             'sulfate_100g': '0.006', 'bicarbonate': '0.00029', 'sodium_unit': 'g', 'nutrition-score-fr': 0,
             'magnesium_unit': 'mg', 'proteins_unit': 'g', 'fat_100g': 0, 'ph': '7.7', 'fat_value': 0,
             'nitrate': '0.001', 'fluoride_unit': 'mg', 'nova-group_100g': 1, 'nova-group': 1, 'sugars': 0,
             'fluoride': '3e-07', 'fruits-vegetables-nuts-estimate-from-ingredients_100g': 0,
             'chloride_label': 'Chlorure', 'fiber_100g': 0, 'magnesium_value': '0.025', 'saturated-fat_value': 0,
             'potassium_label': 'Potassium', 'carbohydrates_value': 0, 'ph_serving': '7.7', 'energy-kcal': 0,
             'chloride_100g': '5e-06', 'magnesium_label': 'Magnésium', 'silica_100g': '2.6e-05',
             'potassium_value': '0.0015', 'energy-kj_value': 0, 'calcium_label': 'Calcium', 'sugars_value': 0,
             'bicarbonate_value': '0.29', 'sulfate_label': 'Sulfate', 'silica_unit': 'mg', 'salt_100g': '0.0275',
             'fiber_value': 0, 'ph_value': '7.7', 'saturated-fat_100g': 0, 'silica_value': '0.026',
             'ph_100g': '7.7', 'fiber_unit': 'g', 'salt_unit': 'g', 'saturated-fat': 0, 'calcium_unit': 'mg',
             'sugars_100g': 0, 'energy-kcal_100g': 0, 'potassium_unit': 'mg', 'silica': '2.6e-05',
             'sulfate_value': 6, 'fluoride_value': '0.0003', 'calcium': '3.9e-05', 'bicarbonate_100g': '0.00029',
             'fluoride_label': 'Fluor', 'energy_unit': 'kJ', 'magnesium': '2.5e-05', 'fiber': 0,
             'energy_value': 0, 'nitrate_value': 1, 'energy-kcal_unit': 'kcal', 'potassium_100g': '1.5e-06',
             'nitrate_unit': 'mg', 'fat_unit': 'g', 'carbohydrates': 0, 'proteins_value': 0, 'sulfate': '0.006',
             'nova-group_serving': 1, 'proteins': 0, 'saturated-fat_unit': 'g', 'fluoride_100g': '3e-07',
             'proteins_100g': 0}, 'categories': 'Boissons,Eaux,Eaux de sources', 'product_name': 'Eau de source',
        'ingredients_text_fr': 'Eau de source.', 'nutrition_grades_tags': ['a'],
        'url': 'https://fr.openfoodfacts.org/produit/3274080005003/eau-de-source-cristaline',
        'image_front_url': 'https://static.openfoodfacts.org/images/products/327/408/000/5003/front_fr.626.400.jpg'},
        {
            'image_front_url': 'https://static.openfoodfacts.org/images/products/301/762/042/2003/front_fr.236.400.jpg',
            'url': 'https://fr.openfoodfacts.org/produit/3017620422003/nutella-pate-a-tartiner-aux-noisettes-et-au-cacao-ferrero',
            'nutrition_grades_tags': ['e'],
            'ingredients_text_fr': 'Sucre, huile de palme, _noisettes_ 13%, _lait_ écrémé en poudre 8,7%, cacao maigre 7,4%, émulsifiants: lécithines [_soja_] ; vanilline. Sans gluten',
            'stores_tags': ['bi1', 'magasins-u', 'carrefour', 'franprix', 'auchan'], 'code': '3017620422003',
            'product_name': 'Nutella pate a tartiner aux noisettes et au cacao',
            'categories': 'Produits à tartiner,Petit-déjeuners,Aides culinaires,Produits à tartiner sucrés,Aides à la pâtisserie,Pâtes à tartiner,Pâtes à tartiner aux noisettes,Pâtes à tartiner au chocolat,Pâtes à tartiner aux noisettes et au cacao,Aide culinaire sucrée',
            'nutriments': {'energy': 2252, 'carbon-footprint-from-known-ingredients_serving': '5.07',
                           'energy-kj_value': 2252, 'sugars_value': '56.3', 'salt': '0.107', 'energy_100g': 2252,
                           'carbohydrates_100g': '57.5', 'energy-kcal_value': 539, 'energy-kcal': 539,
                           'sugars_unit': 'g', 'salt_serving': '0.016', 'sodium_100g': '0.0428',
                           'carbohydrates_value': '57.5', 'energy-kj_100g': 2252, 'carbohydrates_unit': 'g',
                           'sugars_100g': '56.3', 'sugars_serving': '8.44', 'energy-kcal_100g': 539,
                           'salt_unit': 'g', 'saturated-fat': '10.6', 'energy_serving': 338, 'sodium': '0.0428',
                           'saturated-fat_100g': '10.6', 'energy-kj_unit': 'kJ', 'fat': '30.9', 'energy-kj': 2252,
                           'salt_100g': '0.107', 'sodium_unit': 'g', 'nutrition-score-fr': 26,
                           'proteins_unit': 'g', 'energy-kcal_unit': 'kcal', 'fat_100g': '30.9',
                           'energy_value': 2252, 'energy_unit': 'kJ', 'sodium_value': '0.0428',
                           'carbohydrates_serving': '8.62', 'energy-kj_serving': 338, 'salt_value': '0.107',
                           'nutrition-score-fr_100g': 26, 'proteins_serving': '0.945',
                           'energy-kcal_serving': '80.8', 'sodium_serving': '0.00642', 'nova-group': 4,
                           'sugars': '56.3', 'saturated-fat_serving': '1.59',
                           'fruits-vegetables-nuts-estimate-from-ingredients_100g': 13,
                           'saturated-fat_value': '10.6', 'proteins': '6.3', 'saturated-fat_unit': 'g',
                           'proteins_100g': '6.3', 'nova-group_100g': 4, 'fat_serving': '4.63',
                           'nova-group_serving': 4, 'carbon-footprint-from-known-ingredients_product': 135,
                           'fat_unit': 'g', 'fat_value': '30.9', 'carbohydrates': '57.5',
                           'proteins_value': '6.3'}}]
    assert req == result


