# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module manages all datas' Api (connection to it and download to
 local database."""
import requests
from tqdm import tqdm


class ApiOff:
    """ All API data processing with registration in the database. """

    def api_connection(self, req1, req2):
        """ function for API connexion for the products' data."""
        list_data = []
        PAGE = req1
        API_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"
        ACTION = "process"
        SORT_BY = "unique_scans_n"
        PAGE_SIZE = req2
        JSON = "true"
        FIELDS = "product_name,nutrition_grades_tags,url,code," \
                 "ingredients_text_fr,categories,stores_tags," \
                 "image_front_url,nutriments"
        for var in tqdm(range(PAGE)):
            parameters = {'action': ACTION,
                          'sort_by': SORT_BY,
                          'json': JSON,
                          'page': var,
                          'page_size': PAGE_SIZE,
                          'fields': FIELDS}
            res = requests.get(API_URL, parameters)
            # try:
            # if res.status_code == 200:
            data_api = res.json()
            list_data += (data_api['products'])
        return list_data
