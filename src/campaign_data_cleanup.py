import pandas as pd
import numpy as np



def campaigns_cleanup(campaign, campaign_details):
    '''
    Parameters
    ----------
    campaign: pandas DataFrame
        Contains info about ad campaitgns
    campaign_details: pandas DataFrame
        Contains info about ad campaitgns details

    Returns
    -------
    pandas DataFrame
        combined data about campaigns, campaigns with zero impression are removed
    '''

    # remove campaigns with zero ads impressions
    campaign_results = campaign_details.groupby(campaign_details.campaign).sum().reset_index()
    empty_campaigns = campaign_results[campaign_results.impressions == 0].campaign.values
    for camp in empty_campaigns:
        campaign_results = campaign_results[campaign_results.campaign != camp]
    
    # drop columns with unnesessary information
    campaign_results = campaign_results[['campaign', 'impressions', 'clics', 'spend', 'sales', 'orders', 'units']]
    campaign_results = campaign_results.set_index('campaign')
    campaign = campaign.set_index('id')

    # add info from campaign table
    campaign_results = campaign_results.join(campaign)
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
    
def placement_cleanup(placement, placement_detail, campaign):
    '''
    Parameters
    ----------
    placement: pandas DataFrame
        Contains info about ad placement
    placement_details: pandas DataFrame
        Contains info about ad placement details
    campaign: pandas DataFrame
        Contains info about ad campaitgns

    Returns
    -------
    pandas DataFrame
        combined data about campaigns, placement and placement details
        
    '''
    placement = placement.rename(columns= {"placement": "placement_type"})
    placement_detail = placement_detail.join(placement.set_index('id'), on = 'placement')
    placement_result = placement_detail[[
        'date', 
        'impressions', 
        'clicks', 
        'spend', 
        'sales', 
        'orders', 
        'units', 
        'page_views', 
        'campaign', 
        'placement_type']]
    placement_result = placement_result.join(campaign.set_index('id'), on='campaign')
    placement_result['CpC'] = placement_result.spend / placement_result.clicks
    placement_result['price'] = placement_result.sales / placement_result.units
    placement_result['CTR'] = placement_result.clicks / placement_result.impressions * 100
    placement_result = placement_result.drop(columns = [
        'name', 
        'currency', 
        'attribution_period', 
        'end_date'])

    return placement_result


    
if __name__ == '__main__':

    #import campaign data
    campaign = pd.read_csv('data/AMSCampaign.csv')
    campaign_details = pd.read_csv('data/AMSCampaignDetail.csv')
    placement = pd.read_csv('data/AMSPlacement.csv')
    placement_detail = pd.read_csv('data/AMSPlacementDetail.csv')


    # print campaigns with zero results
    campaign_results = campaigns_cleanup(campaign, campaign_details)
    bad_campaigns = zero_sales_campaigns(campaign_results)
    for camp in bad_campaigns:
        print(campaign_details[campaign_details.campaign == camp].sum())
    placement_result = placement_cleanup(placement, placement_detail, campaign)