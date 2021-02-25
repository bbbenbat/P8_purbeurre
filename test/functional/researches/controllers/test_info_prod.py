""" This module test the class InfoProd from info_prod file. """

from researches.controllers import info_prod

info_p = info_prod.InfoProd()


def test_find_product():
    """ This module gives the information for a product. """
    id_product = 2335
    req = info_p.find_product(id_product)
    result = (
        {'energy-kj_value': 851, 'energy_value': 851, 'fat_unit': 'g',
         'salt_100g': 1.3, 'sodium': 0.52, 'energy-kcal_100g': 205,
         'carbohydrates_unit': 'g', 'energy_100g': 851,
         'energy-kj_serving': 1280, 'saturated-fat_100g': 13.2,
         'sodium_serving': 0.78, 'energy_serving': 1280,
         'saturated-fat_serving': 19.8, 'proteins': 8.3,
         'proteins_value': 8.3, 'nutrition-score-fr': 17,
         'fat_serving': 26.7,
         'sugars': 3, 'energy-kcal_value': 205, 'energy': 851,
         'sugars_serving': 4.5, 'energy-kcal_unit': 'kcal',
         'energy_unit': 'kJ', 'salt_value': 1.3, 'carbohydrates': 3,
         'sodium_unit': 'g', 'energy-kj_100g': 851,
         'energy-kcal_serving': 308, 'carbohydrates_100g': 3,
         'sugars_unit': 'g', 'fat': 17.8, 'nutrition-score-fr_100g': 17,
         'energy-kcal': 205, 'saturated-fat_value': 13.2,
         'salt_serving': 1.95, 'fat_100g': 17.8, 'proteins_serving': 12.5,
         'carbohydrates_value': 3, 'sugars_100g': 3,
         'fruits-vegetables-nuts-estimate-from-ingredients_100g': 0,
         'energy-kj_unit': 'kJ', 'salt_unit': 'g', 'proteins_100g': 8.3,
         'sodium_100g': 0.52, 'proteins_unit': 'g', 'sugars_value': 3,
         'salt': 1.3, 'energy-kj': 851, 'nova-group': 4,
         'sodium_value': 0.52,
         'nova-group_100g': 4, 'nova-group_serving': 4,
         'saturated-fat_unit': 'g', 'saturated-fat': 13.2,
         'fat_value': 17.8,
         'carbohydrates_serving': 4.5},
        {'name': 'st môret',
         'nutriment':
             "{'energy-kj_value': "
             "851, "
             "'energy_value': "
             "851, 'fat_unit': "
             "'g', 'salt_100g': "
             "1.3, 'sodium': "
             "0.52, "
             "'energy-kcal_100g': "
             "205, "
             "'carbohydrates_unit': 'g', 'energy_100g': 851, "
             "'energy-kj_serving': 1280, 'saturated-fat_100g': "
             "13.2, 'sodium_serving': 0.78, 'energy_serving': "
             "1280, 'saturated-fat_serving': 19.8, 'proteins': "
             "8.3, 'proteins_value': 8.3, "
             "'nutrition-score-fr': 17, 'fat_serving': 26.7, "
             "'sugars': 3, 'energy-kcal_value': 205, 'energy': "
             "851, 'sugars_serving': 4.5, 'energy-kcal_unit': "
             "'kcal', 'energy_unit': 'kJ', 'salt_value': 1.3, "
             "'carbohydrates': 3, 'sodium_unit': 'g', "
             "'energy-kj_100g': 851, 'energy-kcal_serving': "
             "308, 'carbohydrates_100g': 3, 'sugars_unit': "
             "'g', 'fat': 17.8, 'nutrition-score-fr_100g': 17, "
             "'energy-kcal': 205, 'saturated-fat_value': 13.2, "
             "'salt_serving': 1.95, 'fat_100g': 17.8, "
             "'proteins_serving': 12.5, 'carbohydrates_value': "
             "3, 'sugars_100g': 3, "
             "'fruits-vegetables-nuts-estimate-from-ingredients_100g': "
             "0, 'energy-kj_unit': 'kJ', 'salt_unit': 'g', "
             "'proteins_100g': 8.3, 'sodium_100g': 0.52, "
             "'proteins_unit': 'g', 'sugars_value': 3, 'salt': 1.3, "
             "'energy-kj': 851, 'nova-group': 4, 'sodium_value': 0.52, "
             "'nova-group_100g': 4, 'nova-group_serving': 4, "
             "'saturated-fat_unit': 'g', 'saturated-fat': 13.2, "
             "'fat_value': 17.8, 'carbohydrates_serving': 4.5}",
         'nutriscore': 'd',
         'url': 'https://fr.openfoodfacts.org/produit/3272770098090/st'
                '-moret-le-gout-du-primeur',
         'url_image': 'https://static.openfoodfacts.org/images/products'
                      '/327/277/009/8090/front_fr.141.400.jpg',
         'barcode': '3272770098090',
         'ingredient': '_lait_ et _crème_ pasteurisés ('
                       'Origine: France), protéines du _lait_, '
                       'sel. Fabriqué dans un atelier utilisant des '
                       'fruits à coque et du lait de chèvre'})
    assert req == result
