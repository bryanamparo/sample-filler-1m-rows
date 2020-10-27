import constants
import random
from datetime import date, timedelta
import pandas as pd

txn_date = date(2020, 9, 1)
datedelta = timedelta(days=1)
province = ''
price = ''
product = ''

date_ctr = 1
super_ctr = 0

col_headers = [
    'Transaction Date',
    'Product',
    'Region',
    'Province',
    'Price',
    'email',
    'COL7',
    'COL8',
    'COL9',
    'COL10',
    'COL11',
    'COL12',
    'COL13',
    'COL14',
    'COL15',
    'COL16',
    'COL17',
    'COL18',
    'COL19',
    'COL20',
    'COL21',
    'COL22',
    'COL23',
    'COL24',
    'COL25',
    'COL26',
    'COL27',
    'COL28',
    'COL29',
    'COL30',
]

# data_frame = pd.DataFrame(columns=col_headers)
data_array = []

while date_ctr < 31:
    ctr = 33334
    print("creating 33334 rows for date ", date_ctr)
    while ctr > 0:
        super_ctr += 1
        ctr -= 1
        region = ''
        if ctr > 10001:
            region = random.choice(constants.REGION)
        else:
            region = 'Luzon'
        province = random.choice(constants.REGION_PROVINCE.get(region))
        email = constants.REGION_EMAIL.get(region)
        product = random.choice(constants.PRODUCTS)
        price = constants.PRICES.get(product)
        tmp_df = {
            'Transaction Date': txn_date,
            'Product': product,
            'Region': region,
            'Province': province,
            'Price': price,
            'email': email,
            'COL6': 'COL6_' + str(super_ctr),
            'COL7': 'COL7_' + str(super_ctr),
            'COL8': 'COL8_' + str(super_ctr),
            'COL9': 'COL9_' + str(super_ctr),
            'COL10': 'COL10_' + str(super_ctr),
            'COL11': 'COL11_' + str(super_ctr),
            'COL12': 'COL12_' + str(super_ctr),
            'COL13': 'COL13_' + str(super_ctr),
            'COL14': 'COL14_' + str(super_ctr),
            'COL15': 'COL15_' + str(super_ctr),
            'COL16': 'COL16_' + str(super_ctr),
            'COL17': 'COL17_' + str(super_ctr),
            'COL18': 'COL18_' + str(super_ctr),
            'COL19': 'COL19_' + str(super_ctr),
            'COL20': 'COL20_' + str(super_ctr),
            'COL21': 'COL21_' + str(super_ctr),
            'COL22': 'COL22_' + str(super_ctr),
            'COL23': 'COL23_' + str(super_ctr),
            'COL24': 'COL24_' + str(super_ctr),
            'COL25': 'COL25_' + str(super_ctr),
            'COL26': 'COL26_' + str(super_ctr),
            'COL27': 'COL27_' + str(super_ctr),
            'COL28': 'COL28_' + str(super_ctr),
            'COL29': 'COL29_' + str(super_ctr),
            'COL30': 'COL30_' + str(super_ctr)
        }
        data_array.append(tmp_df)
        # data_frame.append(tmp_df, ignore_index=True)
        if ctr == 11111:
            print('data for 11111: ', tmp_df)
            # print(data_frame.head())

    print("[DONE] creating 33334 rows for date ", date_ctr)
    date_ctr += 1
    txn_date += datedelta

data_frame = pd.DataFrame(data_array)
data_frame.to_csv('Sample_1Mby30cols_SET_C.csv')
