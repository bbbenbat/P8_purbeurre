""" This module parses the data. """
from collections import OrderedDict


class ParserOff:
    """  """

    def delete_fr(self, req):
        """ Delete 'fr:' and 'en:'. """
        cat_clean = []
        for var in req:
            cat_clean.append(var.replace('fr:', '').replace('en:', ''))
        return cat_clean

    def list_global(self, req):
        """ Split all data into global list. """
        new_list = []
        list_p = req
        for var in list_p:
            var1 = var.split(',')
            new_list += var1
        return new_list

    def delete_whitespace(self, req):
        """ Delete all whitespace (l/r) in a list. """
        list_p = []
        for var in req:
            list_p.append(var.strip())
        return list_p

    def low_case(self, req):
        """ Change all caracters in low-case. """
        list_p = []
        for var in req:
            list_p.append(var.lower())
        return list_p

    def delete_duplicate(self, req):
        """ Delete data duplicated in the list. """
        return list(OrderedDict.fromkeys(req))

    def global_parser(self, req):
        """ Uses all methods of the class. """
        delete_fr = self.delete_fr(req)
        delete_w = self.delete_whitespace(delete_fr)
        low_case = self.low_case(delete_w)
        delete_dup = self.delete_duplicate(low_case)
        return delete_dup


