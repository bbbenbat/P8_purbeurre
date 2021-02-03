"""  """

from researches.api import openfoodfacts_api
from researches.api import save_data_api

api_off = openfoodfacts_api.ApiOff()



product = api_off.api_connection(5, 200)
data_db = save_data_api.SaveDataApi()
data_db.save_products(product)
