""" This module parses the data. """


class ParserOff:
    """  """

    def delete_fr(self, req):
        """ Delete 'fr:' and return only categories data into list_categories. """
        list_categories = []
        for var in req:
            try:
                cat = var['categories']
                list_categories.append(cat.replace('fr:', ''))
            except:
                pass
        return list_categories

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
        """  """
        new_list = list(set(req))
        return new_list

