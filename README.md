
# amazon_-eCommerce_optimization

<p align="center"><img width=80% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/Screen%20Shot%202020-09-15%20at%209.10.33%20AM.png> 

This project includes an analysis of several advertizing campaign results of big consumer brands on amazon.com, with a goal to look for potential ways of optimization to improve ROIs.

Technology I used:
- Prophet time series to forecast potential sales with budget increase and SHAPE values to identify factors affecting campaign’s results.
- Random Forest Regressor from Sklearn to predict factors affecting sales 
- SHapley Additive exPlanations (Shap Values) algorithms for the model interpretation. 




## Project goals:

1. Analyze existing data to find best practices of advertising (slice by company / portfolio / ASIN).
2. Look into ways to optimize campaign with a focus on ROI increase by adjusting:
- Keywords
- Bid management
- Time of day / week
- Placements
- Campaign type
3. Forecast potential sales with a budget increase.

## Data

<p align="center"><img width=80% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/schema.png> 

- MySQL DB in AWS
- 13 tables
- 104 campaigns
- Aug 2019 - Feb 2020


## Campaings EDA

To find best practices, I first calculated the average results of all campaigns:

Impressions: 10M
Clicks: 23K
Spend: $32K
Sales: $92K
ROI: 2.875

### Campaign types

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/campaign_types.png> 

Amazon has 3 types of campaigns: Sponsored brands (SB), Sponsored product (SP), and Sponsored display (SD). 
Keeping in mind that average ROI for all campaigns is 2.875, I looked into ROI by campaign types.
Sponsored brands capmaigns have ROI 7.056!
First recommendation: invest in sponsored brand campaigns.

### Targeting

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/targeting.png> 

When using automated targeting, ROIs go down. 
Second recommendation: use manual targeting.

### Ads placement

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/placement.png>
  
  
For ads placement, there are also things that can be improved.
Furthermore, ROIs are vary for different ad types.


<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/brand_ads.jpg>
  
For brand ads, top search works much worse than other placement: 7.07 vs 12.32 ROIs.
  
<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_ads.jpg>
  
For product ads, top search on first page of results perform the best: 4.317 vs 2.083 on the rest of the search.
The ads on product pages and off-amazon remarketing work terrible: 1.094 and 0.791.

## Search EDA

Let's take a look into keywords analysiz. 
My goal was to analyze into each keyword performance in dynamic. 
For this part, I used plotly library.

### Keyword performance

The charts below shows the performance for search term 'hand sanitizer' across all campaigns.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/search-impressions.png>
 
 <p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/search-clicks.png>

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/search-sales.png>

### Future prognosis 

To extrapolate future sales, I used Prophet time series. 
Below is a graph that predicts sales coming from keyword 'hand soap' for two upcoming months.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/search-sales-prognosis.png>
  
We can also see this search term sales overall trend, and weekly fluctuation component.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/search-forecast-components.png>


## Product analysis

Next, let's see how each product is performing.
Here is a brief overview of one product, hand sanitizer, performance.
First image showes the funnel impressions -> clicks -> orders.
Second showes overall money spent on ads -> sales.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_sales_funnel.png>

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_sales_funnel1.png>

### Product performance by campaign

I first did a high-level analytics of data grouped by campaign.
For example, this is how our ads are performing for product A (hand sanitizer):

<p align="center"><img width=100% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_overview_by_campaign.png>

### Product performance in dynamics

Below are the graphs for impressions, clicks and sales for the product A, hand sanitizer, across all campaigns.
There is also an option to look into each campaign individually.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_impressions.png>

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_clicks.png>
 
<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_sales.png>
  
### Sales prognosis

Using Prophet time series, I build prognosis for each product.
The graph below showes the sales prognosis for hand sanitizer for 2 weeks, and trend components - overal trend and weekly fluctuation.

<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_sales_prognosis.png>
 
<p align="center"><img width=70% src=https://github.com/JuliaSokolova/amazon_-eCommerce_optimization/blob/master/img/product_sales_prognosis_components.png>

### Factors, affecting sales

Finally, I wanted to look into factors affecting sales.
To do that, I built a ML model (I used  Random Forest Regressor from Sklearn), and used SHAP values to visualize features importance.



## Results:

Found ways to increase ROIs by 4x times via campaign and targeting settings modifications


