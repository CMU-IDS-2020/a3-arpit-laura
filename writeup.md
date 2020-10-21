# Impact of COVID19 on Property Rates in Bay Area

![alt text](https://github.com/CMU-IDS-2020/a3-arpit-laura/blob/master/Streamlit%20screenshot.png)

Analyzing the impact (if any) of COVID-19 on housing prices in the San Francisco Bay Area

## Project Goals

In the news recently, there have been many reports of unusual fluctuations in housing prices, as people’s lifestyles have been completely upended.  We were specifically interested in the Bay Area because we both are looking to find jobs and live in the area after graduation.  Our thinking was that any trends could help us to make more informed housing decisions, as the COVID-19 pandemic persists. 

## Design

To perform our exploratory data analysis, we first gathered all the relevant data.  For COVID-19 information by county, we used data from Johns Hopkins University, as they are a reputable source.  For property rates, and neighborhood score, we set up a web crawler to gather data from realtor.com and aeavibes.com.  After collection, we cleaned and organized all the datasets.  For the design, we then sketched out a model of what we wanted the visualization to look like.  We wanted to show historical data from the inception of our COVID-19 data (March 22, 2020) through the present.  We decided to use the map feature with bars in Streamlit to show the median property values by county.  An identical map would be juxtaposed with the neighborhood scores by county, as we understand that properties in nicer neighborhoods generally have higher value.  A bar chart below the map visualizations would show the COVID data (including number of confirmed cases, active cases, and deaths) by county selected.  A sidebar would allow the user to select the month, number of bedrooms for the houses, mean or median aggregation type, and the type of neighborhood score that they want to show.

## Development

For the development process, we first came to an agreement on the overarching question that we wanted to answer. We then drew out a concept for the structure and graphics that would best capture what we wanted to show. For the work breakdown, Laura focused on the COVID-19 data, and Arpit focused on housing data and neighborhood rates.  In the data, we found unusual fluctuations in certain counties.  In Cupertino County, median price/square footage was $1,368 in February, 2020.  At this time, there were no confirmed COVID-19 cases. 2 months later, in April, the $/sqft more than doubled ($2,926).  There were more than 2,000 confirmed cases by this time. After that spike in April, the housing rates dropped back down over the summer months.  If we were to explore this topic further, we could look at housing rates in rural vs. urban areas, as many companies normalize remote work, leading people to factor in job proximity less in housing decisions. 
Laura - I do not have a technical background, and am fairly new to coding.  In total, I spent about 35 hours on this assignment. Setting up and installing the environment took up a large chunk of time.  Creating the visualizations also took a while, as I am still working to understand and learn python syntax and core functionality.  I tried to figure things out on my own by Googling, and looking back, I wish I had used the office hours sooner in the process, as the TA’s were very helpful.
Arpit - 

