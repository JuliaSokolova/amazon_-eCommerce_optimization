#from campaign_data_cleanup import campaigns_cleanup, placement_cleanup

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

def results_by_targeting(campaign_results):
    '''
    Parameters
    ----------
    campaign_results : pandas DataFrame
        preprocessed data about campaigns with campaigns_cleanup function 

    Returns
    -------
    pandas DataFrame
        campaigns results grouped by the targeting type
    '''
    results_by_targeting = campaign_results.groupby(campaign_results.targeting_type)[
        'impressions', 
        'clics', 
        'spend', 
        'sales', 
        'orders', 
        'units'].sum().reset_index()
    results_by_targeting['ROI'] = results_by_targeting.sales / results_by_targeting.spend
    results_by_targeting = results_by_targeting.sort_values(by = 'ROI', ascending = False)[0:2].reset_index().drop(columns = 'index')

    return results_by_targeting

def results_by_daily_budget(campaign_results):
    '''
    Parameters
    ----------
    campaign_results : pandas DataFrame
        preprocessed data about campaigns with campaigns_cleanup function 

    Returns
    -------
    pandas DataFrame
        campaigns results grouped by the targeting type
    '''
    results_by_daily_budget = campaign_results.groupby(campaign_results.daily_budget)[
        'impressions', 
        'clics', 
        'spend', 
        'sales', 
        'orders', 
        'units'].sum().reset_index()
    results_by_daily_budget['ROI'] = results_by_daily_budget.sales / results_by_daily_budget.spend
    results_by_daily_budget = results_by_daily_budget.sort_values(by = 'ROI', ascending = False)
    
    return results_by_daily_budget

def result_by_placement(placement_result):
    '''
    Parameters
    ----------
    placement_result : pandas DataFrame
        preprocessed data about ads placement with placement_result function 

    Returns
    -------
    pandas DataFrame
        campaigns results grouped by the placement type   
    '''
    placements_campaign_type = placement_result.groupby(
        [
        placement_result.type, 
        placement_result.placement_type
        ]
        )['impressions', 
            'clicks', 
            'spend', 
            'sales', 
            'orders', 
            'units'].sum().reset_index()
    placements_campaign_type['ROI'] = placements_campaign_type.sales / placements_campaign_type.spend
    placements_campaign_type = placements_campaign_type.sort_values(by = 'ROI', ascending = False)

    return placements_campaign_type


if __name__ == '__main__':
    #import campaign data
    campaign = pd.read_csv('data/AMSCampaign.csv')
    campaign_details = pd.read_csv('data/AMSCampaignDetail.csv')
    placement = pd.read_csv('data/AMSPlacement.csv')
    placement_detail = pd.read_csv('data/AMSPlacementDetail.csv')

    # process the data to get campaigns EDA
    campaign_results = campaigns_cleanup(campaign, campaign_details)
    placement_result = placement_cleanup(placement, placement_detail, campaign)
    results_type = results_by_campaig_type(campaign_results)
    results_targeting = results_by_targeting(campaign_results)
    results_daily_budget = results_by_daily_budget(campaign_results)
    result_by_placement = result_by_placement(placement_result)

