# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class InfoProd from parser_off file. """

from django.test import TestCase

from researches.controllers.parser_off import ParserOff

parser_off = ParserOff()


class test_parser_off_ParserOff(TestCase):
    """ This class processes the data retrieved through the API before it
        is saved to the database """

    def test_parser_off_delete_fr(self):
        """ Delete 'fr:' and return data into list_categories. """
        req0 = ['fr: Purée de petit pois',
                'Petit pote',
                'Pomme de terre', 'La patate']
        req = parser_off.delete_fr(req0)
        result = [' Purée de petit pois', 'Petit pote', 'Pomme de terre',
                  'La patate']
        assert req == result

    def test_parser_off_list_global(self):
        """ Split all data into global list. """
        req0 = ['Boissons,Eaux,Eaux de sources',
                'Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits '
                'au chocolat',
                'Boissons,Boissons gazeuses,Sodas,Sodas au cola,Boissons '
                'avec sucre ajouté']
        req = parser_off.list_global(req0)
        result = ['Boissons', 'Eaux', 'Eaux de sources', 'Snacks',
                  'Snacks sucrés', 'Biscuits et gâteaux', 'Biscuits',
                  'Biscuits au chocolat', 'Boissons', 'Boissons gazeuses',
                  'Sodas', 'Sodas au cola', 'Boissons avec sucre ajouté']
        assert req == result

    def test_parser_off_delete_whitespace(self):
        """ Delete all whitespace (l/r) in a list. """
        req0 = ['Pomme de terre ', ' Petit pois', ' Purée de carottes ',
                'Soupe de légumes']
        req = parser_off.delete_whitespace(req0)
        result = ['Pomme de terre', 'Petit pois', 'Purée de carottes',
                  'Soupe de légumes']
        assert req == result

    def test_parser_off_low_case(self):
        """ Change all caracters in low-case. """
        req0 = ['Pomme de terre', 'Petit pois', 'Purée de carottes',
                'Soupe de légumes']
        req = parser_off.low_case(req0)
        result = ['pomme de terre', 'petit pois', 'purée de carottes',
                  'soupe de légumes']
        assert req == result

    def test_parser_delete_duplicate(self):
        """ Delete data duplicated in the list. """
        req0 = ['purée de pommes de terre', 'purée de carottes',
                'purée de pommes de terre']
        req = parser_off.delete_duplicate(req0)
        result = ['purée de pommes de terre', 'purée de carottes']
        assert req == result
