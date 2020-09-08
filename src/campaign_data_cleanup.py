import pandas as pd
import numpy as np



def campaigns_cleanup(campaign, campaign_details):
    '''
    Parameters
    ----------
    campaign_data : pandas DataFrame
        Contains info about ad campaitgns
    campaign_details_data : pandas DataFrame
        Contains info about ad campaitgns details

    Returns
    -------
    pandas DataFrame
        combined data about campaigns, campaigns with zero impression are removed
    '''

    # remove campaigns with zero ads impressions
    campaign_results = campaign_details.groupby(campaign_details.campaign).sum()
    campaign_results = campaign_results.reset_index()
    empty_campaigns = campaign_results[campaign_results.impressions ==0].campaign.values
    for campaign in empty_campaigns:
        campaign_results = campaign_results[campaign_results.campaign != campaign]
    
    # drop columns with unnesessary information
    campaign_results = campaign_results[['campaign', 'impressions', 'clics', 'spend', 'sales', 'orders', 'units']]

    # add info from campaign table
    campaign_results = campaign_results.join(campaign.set_index('id'), on='campaign')
    campaign_results = campaign_results.drop(columns = ['currency', 'end_date'])

    return campaign_results


def zero_sales_campaigns(campaign_results):
    '''
    Parameters
    ----------
    campaign_results : pandas DataFrame
        preprocessed data about campaigns with campaigns_cleanup function 

    Returns
    -------
    pandas DataFrame
        campaigns ids with zero sales
    '''
    # campaigns with no sales
    bad_campaigns = campaign_results[campaign_results.sales == 0].campaign.values

    return bad_campaigns


if __name__ == '__main__':

    #import campaign data
    campaign = pd.read_csv('data/AMSCampaign.csv')
    campaign_details = pd.read_csv('data/AMSCampaignDetail.csv')

    # print campaigns with zero results
    campaign_results = campaigns_cleanup(campaign, campaign_details)
    bad_campaigns = zero_sales_campaigns(campaign_results)
    for camp in bad_campaigns:
        print(campaign_details[campaign_details.campaign == camp].sum())
            
    
