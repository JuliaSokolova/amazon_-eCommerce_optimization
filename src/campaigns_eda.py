from campaign_data_cleanup import campaigns_cleanup
import pandas as pd
import numpy as np


def results_by_campaig_type(campaign_results):
    '''
    Parameters
    ----------
    campaign_results : pandas DataFrame
        preprocessed data about campaigns with campaigns_cleanup function 

    Returns
    -------
    pandas DataFrame
        campaigns results grouped by the campaign type
    '''
    results_by_type = campaign_results.groupby(campaign_results.type)[
        'impressions', 
        'clics', 
        'spend', 
        'sales', 
        'orders', 
        'units'].sum().reset_index()
    results_by_type['ROI'] = results_by_type.sales / results_by_type.spend
    results_by_type = results_by_type.sort_values(by = 'ROI', ascending = False).reset_index().drop(columns = 'index')
    return results_by_type


    


if __name__ == '__main__':
    #import campaign data
    campaign = pd.read_csv('data/AMSCampaign.csv')
    campaign_details = pd.read_csv('data/AMSCampaignDetail.csv')

    # process the data to get campaigns EDA
    campaign_results = campaigns_cleanup(campaign, campaign_details)
    results_by_type = results_by_campaig_type(campaign_results)


