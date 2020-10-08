import pandas as pd
import numpy as np
import plotly.express as px
from fbprophet import Prophet

def get_search_terms(search):
    '''
    Parameters
    ----------
    search: pandas DataFrame
        Contains info about all search terms

    Returns
    -------
    numpy array:
        List of search terms used in all campaigns
    '''
    return search.term.unique()

def search_term_data(term, search, search_details):
    '''
    Parameters
    ----------
    term: string
        Search term used in one / many campaigns
    search: pandas DataFrame
        Contains info about all search terms
    search_details: pandas DataFrame
        Contains info about details for each search session

    Returns
    -------
    pandas DataFrame:
        Data about search results for specified search term
    '''
    search_term_ids = search[search.term == term].id.unique()
    data = search_details[search_details.search_id.isin(search_term_ids)]
    data = data.groupby(data.date).sum().reset_index()
    data['date']=pd.to_datetime(data['date'])
    data = data.sort_values(by=['date'], ascending=False)
    data = data.drop(['search_id', 'conversions_rate', 'advertised_asin_units', 'advertised_brand_units'], axis=1)
    return data

def plot_search_charts(term, search, search_details):
    '''
    Parameters
    ----------
    term: string
        Search term used in one / many campaigns
    search: pandas DataFrame
        Contains info about all search terms
    search_details: pandas DataFrame
        Contains info about details for each search session
    Returns
    -------
        graphs showing impressions, cliks and sales over time for the specified search term 
    '''
    # getting the data
    data = search_term_data(term, search, search_details)

    # plotting impressions
    impressions = px.line(data, x='date', y='impressions', title=f'Numper of impressions for search term: {term}')
    impressions.update_xaxes(rangeslider_visible=True)
    impressions.show()

    # plotting clicks
    clicks = px.line(data, x='date', y='clicks', title=f'Numper of clicks for search term: {term}')
    clicks.update_xaxes(rangeslider_visible=True)
    clicks.show()

    # plotting sales
    sales = px.line(data, x='date', y=['spend', 'sales'], title=f'Total sales for search term: {term}')
    sales.update_xaxes(rangeslider_visible=True)
    sales.show()

if __name__ == '__main__':

    #import search data
    search = pd.read_csv('data/AMSSearch.csv')
    search_details = pd.read_csv('data/AMSSearchDetail.csv')
    term = 'hand sanitizer'


    # print campaigns with zero results
    all_terms = get_search_terms(search)
    term_data = search_term_data(term, search, search_details)
    plot_search_charts(term, search, search_details)


    


