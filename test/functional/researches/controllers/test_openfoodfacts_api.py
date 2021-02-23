""" This module test the class ApiOff from openfoodfacts_api file. """

from researches.controllers.openfoodfacts_api import ApiOff

off_api = ApiOff()

# CONSTANTS
PAGE = 1
PAGE_SIZE = 1


def test_openfoodfacts_api():
    """ Test controllers result for page 1 with 2 product."""
    list_req = []
    api_off = off_api.api_connection(PAGE, PAGE_SIZE)
    for loop in api_off:
        list_req.append(loop['code'])
    result = ['3274080005003', '3017620422003', '7622210449283', '5449000000996', '5449000131805', '3017620425035',
              '3229820129488', '3175680011480', '8000500310427', '3228857000166', '8001505005592', '7613034626844',
              '3228857000852', '3033710065967', '3229820019307', '3046920022651', '3229820100234', '5010477348678',
              '3256540000698', '3175680011534', '3268840001008', '3033710065066', '3046920022606', '3168930010265']
    req = list_req
    assert req == result
