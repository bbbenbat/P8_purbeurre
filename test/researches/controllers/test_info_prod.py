""" This module test the class InfoProd from info_prod file. """

from researches.controllers import info_prod

info_p = info_prod.InfoProd()


def test_find_product():
    """ This module gives the information for a product. """
    id_product = 10
    req = info_p.find_product(id_product)
    result = (
        {'sugars_unit': 'g', 'fiber_unit': 'g', 'carbohydrates_serving': 8.1,
         'salt_value': 0.12, 'sodium_serving': 0.0072,
         'energy-kj': 2270, 'energy_100g': 2270, 'nova-group_serving': 4, 'proteins_unit': 'g',
         'nutrition-score-fr': 18,
         'energy_unit': 'kJ', 'fat': 32, 'fiber_value': 3.6, 'fat_100g': 32, 'salt_unit': 'g', 'cocoa_value': 6.5,
         'fiber_serving': 0.54, 'carbohydrates_unit': 'g', 'proteins': 8.1, 'sugars_value': 51, 'salt_100g': 0.12,
         'cocoa_label': '0', 'carbohydrates': 54, 'fat_serving': 4.8, 'energy-kj_value': 2270, 'energy-kj_unit': 'kJ',
         'energy_value': 2270, 'sugars': 51, 'cocoa_unit': 'g', 'energy-kj_100g': 2270, 'saturated-fat': 5.7,
         'saturated-fat_value': 5.7, 'saturated-fat_serving': 0.855, 'salt': 0.12, 'sodium_value': 0.048,
         'carbohydrates_value': 54, 'salt_serving': 0.018, 'sodium_unit': 'g', 'energy_serving': 340,
         'saturated-fat_unit': 'g', 'sodium': 0.048, 'fat_unit': 'g', 'proteins_100g': 8.1, 'cocoa': 6.5,
         'carbohydrates_100g': 54, 'proteins_value': 8.1, 'energy-kj_serving': 340, 'nova-group': 4, 'cocoa_100g': 6.5,
         'sugars_serving': 7.65, 'fat_value': 32, 'nutrition-score-fr_100g': 18, 'fiber_100g': 3.6, 'energy': 2270,
         'nova-group_100g': 4, 'sodium_100g': 0.048, 'sugars_100g': 51, 'proteins_serving': 1.22,
         'saturated-fat_100g': 5.7,
         'fruits-vegetables-nuts-estimate-from-ingredients_100g': 18.5, 'fiber': 3.6, 'cocoa_serving': 6.5},
        {'name': 'nocciolata pâte à tartiner au cacao et noisettes',
         'nutriment': "{'sugars_unit': 'g', 'fiber_unit': 'g', 'carbohydrates_serving': 8.1, 'salt_value': 0.12, "
                      "'sodium_serving': 0.0072, 'energy-kj': 2270, 'energy_100g': 2270, 'nova-group_serving': 4, "
                      "'proteins_unit': 'g', 'nutrition-score-fr': 18, 'energy_unit': 'kJ', 'fat': 32, "
                      "'fiber_value': 3.6, 'fat_100g': 32, 'salt_unit': 'g', 'cocoa_value': 6.5, "
                      "'fiber_serving': 0.54, 'carbohydrates_unit': 'g', 'proteins': 8.1, 'sugars_value': 51, "
                      "'salt_100g': 0.12, 'cocoa_label': '0', 'carbohydrates': 54, 'fat_serving': 4.8, "
                      "'energy-kj_value': 2270, 'energy-kj_unit': 'kJ', 'energy_value': 2270, 'sugars': 51, "
                      "'cocoa_unit': 'g', 'energy-kj_100g': 2270, 'saturated-fat': 5.7, 'saturated-fat_value': 5.7, "
                      "'saturated-fat_serving': 0.855, 'salt': 0.12, 'sodium_value': 0.048, "
                      "'carbohydrates_value': 54, 'salt_serving': 0.018, 'sodium_unit': 'g', 'energy_serving': 340, "
                      "'saturated-fat_unit': 'g', 'sodium': 0.048, 'fat_unit': 'g', 'proteins_100g': 8.1, "
                      "'cocoa': 6.5, 'carbohydrates_100g': 54, 'proteins_value': 8.1, 'energy-kj_serving': 340, "
                      "'nova-group': 4, 'cocoa_100g': 6.5, 'sugars_serving': 7.65, 'fat_value': 32, "
                      "'nutrition-score-fr_100g': 18, 'fiber_100g': 3.6, 'energy': 2270, 'nova-group_100g': 4, "
                      "'sodium_100g': 0.048, 'sugars_100g': 51, 'proteins_serving': 1.22, 'saturated-fat_100g': 5.7, "
                      "'fruits-vegetables-nuts-estimate-from-ingredients_100g': 18.5, 'fiber': 3.6, "
                      "'cocoa_serving': 6.5}",
         'nutriscore': 'd',
         'url': 'https://fr.openfoodfacts.org/produit/8001505005592/nocciolata-pate-a-tartiner-au-cacao-et-noisettes-rigoni-di-asiago',
         'url_image': 'https://static.openfoodfacts.org/images/products/800/150/500/5592/front_fr.113.400.jpg',
         'barcode': '8001505005592',
         'ingredient': 'Sucre de canne*,pâte de _noisettes_* 18,5 %, huile de tournesol*, '
                       '_lait_ écrémé en poudre*, cacao maigre en poudre* 6,5 %, beurre de cacao*, '
                       'émulsifiant : lécithine de _soja_*, extrait de vanille*. * Biologique.'})
    assert req == result
