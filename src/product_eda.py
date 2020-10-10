import pandas as pd
import numpy as np
import plotly.express as px

def get_ads_data(campaign, ad_group, ad_group_details):
    ads_data = ad_group_details.join(ad_group.set_index('id'), on='ad_groups')
    ads_data = ads_data.drop(['name'], axis=1)
    ads_data = ads_data.join(campaign.set_index('id'), on='campaign')
    return ads_data

def get_product_data_by_campaign(name, ads_data, campaign):
    product = ads_data[ads_data.asin == name]
    product = product.groupby(product.campaign)[
        'impressions', 
        'clicks', 
        'spend', 
        'sales', 
        'orders', 
        'units'].sum().reset_index()
    product['ROI'] = product.sales / product.spend
    product = product.join(campaign.set_index('id'), on='campaign').sort_values(by = 'ROI', ascending = False)
    product = product.drop(columns = ['currency'])
    return product

def get_product_data_by_day(name, ads_data):
    # getting data
    product = ads_data[ads_data.asin == name]
    product.date = pd.to_datetime(product.date)
    X = product.groupby(product.date).sum().reset_index()

    # plotting impressions
    impressions = px.line(X, x='date', y='impressions', title=f'Numper of impressions for product: {name}')
    impressions.update_xaxes(rangeslider_visible=True)
    impressions.show()

    # plotting clicks
    clicks = px.line(X, x='date', y='clicks', title=f'Numper of clicks for product: {name}')
    clicks.update_xaxes(rangeslider_visible=True)
    clicks.show()

    # plotting sales
    sales = px.line(X, x='date', y=['spend', 'sales'], title=f'Total sales for product: {name}')
    sales.update_xaxes(rangeslider_visible=True)
    sales.show()





