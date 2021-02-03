"""  """

from researches.api.openfoodfacts_api import ApiOff

off_api = ApiOff()

# CONSTANTS
PAGE = 1
PAGE_SIZE = 2

print(PAGE)
print(PAGE_SIZE)


def test_openfoodfacts_api():
    """ Test api result for page 1 with 2 product."""
    req = off_api.api_connection(PAGE, PAGE_SIZE)
    result = [{'nutrition_grades_tags': ['a'],
               'url': 'https://fr.openfoodfacts.org/produit/3274080005003/'
                      'eau-de-source-cristaline',
               'stores_tags': ['carrefour', 'auchan', 'leclerc'],
               'categories': 'Boissons,Eaux,Eaux de sources',
               'product_name': 'Eau de source',
               'ingredients_text_fr': 'Eau de source.',
               'code': '3274080005003'},
              {'ingredients_text_fr': "céréales 50,7% (farine de blé 35%, "
                                      "farine de blé complète 15,7%), sucre, "
                                      "huiles végétales (palme, colza), cacao "
                                      "maigre en poudre 4,5%, sirop de glucose,"
                                      " amidon de blé, poudre à lever "
                                      "(carbonate acide d'ammonium, carbonate "
                                      "acide de sodium, diphpsphate disodique), "
                                      "émulsifiant (lécithine de soja, lécithine "
                                      "de tournesol), sel, lait écrémé en poudre, "
                                      "lactose et protéines de lait, arômes.",
               'code': '7622210449283',
               'product_name': 'prince',
               'url': 'https://fr.openfoodfacts.org/produit/7622210449283/prince-lu',
               'stores_tags': ['carrefour-market', 'magasins-u', 'auchan',
                               'intermarche', 'carrefour', 'casino', 'leclerc',
                               'cora', 'bi1'],
               'categories': 'Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,'
                             'Biscuits au chocolat',
               'nutrition_grades_tags': ['d']}]
    assert req == result
