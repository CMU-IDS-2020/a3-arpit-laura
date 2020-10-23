# Impact of COVID19 on Property Rates in Bay Area

![alt text](https://github.com/CMU-IDS-2020/a3-arpit-laura/blob/master/Streamlit%20screenshot1.png)

## Analyzing the impact (if any) of COVID-19 on housing prices in the San Francisco Bay Area

## Project Goals

In the news recently, there have been many reports of unusual fluctuations in housing prices as people’s lifestyles have been completely upended due to the COVID-19 pandemic.  We were both specifically interested in the Bay Area because we both are looking to find jobs and live in the area after graduation.  To narrow our data down, we looked specifically at Santa Clara county, which consists of major cities like Cupertino, Palo Alto, San Jose, Mountain View, and Santa Clara.   We believe that any trends we can identify can help us to make more informed housing decisions as the COVID-19 pandemic persists.

## Design

To perform our exploratory data analysis, we first gathered all the relevant data.  For COVID-19 information by county, we used data from Johns Hopkins University, as they are a reputable source.  We set up a web crawler for property rates and neighborhood score to gather data from realtor.com and areavibes.com.  After collection, we cleaned and organized all the datasets.  We then sketched out a model of what we wanted the visualization to look like for the design.  We wanted to show historical data from the inception of our COVID-19 data (March 22, 2020) through the present. 

We initially designed a sketch which involved multiple bar charts, and filters to demonstrate the visual interaction and facilitate EDA. After analyzing the data we gathered, we understood our strategy of using multiple bar graphs won’t provide the desired interactivity and exploration to the user. Hence, we decided to use the map feature with bars in Streamlit to show the county’s median or mean property values.  An identical map was juxtaposed with the neighborhood scores by county, as we understand that properties in more superior neighborhoods generally have a higher value.  A bar chart below the map visualizations would show the COVID data (including the number of confirmed cases, active cases, and deaths) by county selected.  A sidebar would allow the user to choose the month, the number of bedrooms for the houses, mean or median aggregation type, and the type of neighborhood score that the user wants to see.


![alt text](https://github.com/CMU-IDS-2020/a3-arpit-laura/blob/master/Data%20sketch.png)

## Development

For the development process, we first came to an agreement on the overarching question that we wanted to answer. We then drew out a concept for the structure and graphics that would best capture what we wanted to show. For the work breakdown, Laura focused on the COVID-19 data, and Arpit focused on housing data and neighborhood rates.  In the data, we did find some unusual fluctuations in certain cities.  In Cupertino, median price/square footage was $1,368 in February, 2020.  At this time, there were no confirmed COVID-19 cases. 2 months later, in April, the $/sqft more than doubled ($2,926).  There were more than 2,000 confirmed cases by this time. After that spike in April, the housing rates dropped back down over the summer months.  If we were to explore this topic further, we could look at housing rates in rural vs. urban areas, as many companies normalize remote work, leading people to factor in job proximity less in housing decisions. 

Laura - I do not have a technical background, and am fairly new to coding.  In total, I spent about 35 hours on this assignment. Setting up and installing the environment took up a large chunk of time as I had to troubleshoot a variety of issues.  Creating the visualizations also took a while, as I am still working to understand and learn python syntax and core functionality.  I mostly tried to figure things out on my own by Googling, and looking back, I wish I had used the office hours sooner in the process, as the TA’s were very helpful.

Arpit - With a limited background in coding languages such as VBA, Java, Python, etc, I spent around 30 hours on the assignment. 
