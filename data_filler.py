import constants
import random
from dbconn import DBConnection
from datetime import date, timedelta

db_host = 'escdev.eschost2.net'
db_port = 5432
db_username = 'bryan_a'
db_password = 'kdzW8QaGjeE3DKHJaRC55qAmbnQ'
db_database = 'wiser_inv_20200401'

INSERT_SQL = """
    INSERT INTO tmp_txn_sample (txn_date, product, price, province) VALUES
    (%s, %s, %s, %s)
"""

txn_date = date(2020, 9, 2)
datedelta = timedelta(days=1)
province = ''
price = ''
product = ''

ctr = 100
date_ctr = 2

with DBConnection(
    db_host,
    db_port,
    db_username,
    db_password,
    db_database
) as dbconn:
    while date_ctr < 31:
        ctr = 100
        while ctr > 0:
            ctr -= 1
            province = random.choice(constants.PROVINCES)
            product = random.choice(constants.PRODUCTS)
            price = constants.PRICES.get(product)
            dbconn.update_object(
                INSERT_SQL,
                [txn_date, product, price, province]
            )
        date_ctr += 1
        txn_date += datedelta
