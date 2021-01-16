"""  """
from off_app.api.parser_off import ParserOff

parser_off = ParserOff()


def test_parser_off_delete_fr():
    """ Delete 'fr:' and return only categories data into list_categories. """
    req0 = [{'categories': 'fr: Purée de petit pois'},
            {'product_name': 'Petit pote'},
            {'categories': 'Pomme de terre', 'product_name': 'La patate'}]
    req = parser_off.delete_fr(req0)
    result = [' Purée de petit pois', 'Pomme de terre']
    assert req == result
