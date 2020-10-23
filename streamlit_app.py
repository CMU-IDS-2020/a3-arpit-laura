import streamlit as st
import numpy as np
import math
import pandas as pd
import pydeck as pdk
import altair as alt

#Declaring functions Get Data and Map
@st.cache
def get_data(data_link):
    return pd.read_csv(data_link)

def map1(data, lat, long, zoom):
    st.write(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state={
                "latitude": lat,
                "longitude": long,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "ColumnLayer",
                    data=data,
                    get_position=["Long", "Lat"],
                    get_elevation="Rate_dollar_sqft",
                    get_elevation_weight=0.8,
                    elevation_scale=2,
                    elevation_range=[0, 100],
                    get_fill_color = ["Rate_dollar_sqft",140],
                    radius=350,
                    pickable=True,
                    extruded=True
                )
            ],
            tooltip={
                'html': '<b>Rate per sqft:</b> {Rate_dollar_sqft}',
                'style': {
                    'color': 'white'
                }
            }
        ))

def map2(data, lat, long, zoom):
    st.write(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state={
                "latitude": lat,
                "longitude": long,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "ColumnLayer",
                    data=data,
                    get_position=["Long", "Lat"],
                    get_elevation=score_type_map_norm[score_selected],
                    get_elevation_weight=1,
                    elevation_scale=100,
                    elevation_range=[0, 100],
                    get_fill_color = [score_type_map[score_selected],140],
                    radius=350,
                    pickable=True,
                    extruded=True
                )
            ],
            tooltip={
                'html': '<b>Score:</b> {' + score_type_map[score_selected] + '}',
                'style': {
                    'color': 'white'
                }
            }
        ))
    
def preprocess(data):
    data.fillna(0, inplace=True)
    if data['Rate_dollar_sqft'] == '-':
        data['Rate_dollar_sqft'] = data['Amount_dollar']/data['Area']
    return data

def norm(df):
    df = df.add_suffix("_norm")    
    df_norm = abs(((df - df.mean()) / (df.max() - df.min()))*1000)
    return df_norm

def preprocess_2(data):
    data.fillna(0, inplace=True)
    

#Links to all datasets on Github
COVID19_CA_data_link = 'https://raw.githubusercontent.com/CMU-IDS-2020/a3-arpit-laura/master/COVID19_CA.csv'
Property_History_data_link = 'https://raw.githubusercontent.com/CMU-IDS-2020/a3-arpit-laura/master/Property_History.csv'
Property_Rates_data_link = 'https://raw.githubusercontent.com/CMU-IDS-2020/a3-arpit-laura/master/Property_Rates.csv'
ZIP_County_data_link = 'https://raw.githubusercontent.com/CMU-IDS-2020/a3-arpit-laura/master/ZIP_County.csv'
neighbourhood_scores_data_link = 'https://raw.githubusercontent.com/CMU-IDS-2020/a3-arpit-laura/master/neighbourhood_scores.csv'

#Storing CSV data in dataframe
df_Property_Rates = get_data(Property_Rates_data_link)
df_ZIP_County = get_data(ZIP_County_data_link)
df_COVID_CA = pd.read_csv(COVID19_CA_data_link, index_col=0)
df_Property_History = pd.read_csv(Property_History_data_link)
df_Neighborhood_Score = pd.read_csv(neighbourhood_scores_data_link)

#Merging Property Rates and ZIP dataset to get lat long for properties
zip_codes = pd.merge(df_Property_History, df_ZIP_County, on='Zip_Code')
zip_codes['Lat'] = zip_codes['Lat'].astype('float')
zip_codes['Long'] = zip_codes['Long'].astype('float')
zip_codes['Beds'] = zip_codes['Beds'].apply(lambda x: 1 if 'Studio' in x else float(x))
no_of_bed_rooms = list(zip_codes['Beds'].unique())
no_of_bed_rooms.sort()


#Placing items on Sidebar

#Month slider
#st.sidebar.markdown("Select the month of 2020")
month_selected = st.sidebar.slider('Select the month of 2020', 1, 9)

#Beds slider
beds_selected = st.sidebar.slider('Select # of bedrooms', int(min(no_of_bed_rooms)), int(max(no_of_bed_rooms)))
    
#Check box for mean and median
stat_selected = st.sidebar.radio('Select aggreation type on the map', ('Mean','Median'), index=0)

#Filters for Neighbourhood Scores
score_selected = st.sidebar.radio('Select the neighbourhood score type', ('Livelihood Score', 'School Test Score', 'Total Crime', 'Overall User Rating', 'Cost of Living', 'Median HH Income', 'Income Per Capita', 'Unemployment Rate', 'Median Home Value', 'Median Rent Price', 'Home Ownership'), index=0)

score_type_map = {'Livelihood Score':'liv_score' , 'School Test Score':'School_test_scores', 'Total Crime':'Total_Crime', 'Overall User Rating':'Overall_user_rating', 'Cost of Living':'Cost_of_living_city', 'Median HH Income':'Median_household_income', 'Income Per Capita':'Income_per_capita', 'Unemployment Rate':'Unemployment_rate', 'Median Home Value':'Median_home_value', 'Median Rent Price':'Median_rent_price', 'Home Ownership':'Home_ownership'}

score_type_map_norm = {'Livelihood Score':'liv_score_norm' , 'School Test Score':'School_test_scores_norm', 'Total Crime':'Total_Crime_norm', 'Overall User Rating':'Overall_user_rating_norm', 'Cost of Living':'Cost_of_living_city_norm', 'Median HH Income':'Median_household_income_norm', 'Income Per Capita':'Income_per_capita_norm', 'Unemployment Rate':'Unemployment_rate_norm', 'Median Home Value':'Median_home_value_norm', 'Median Rent Price':'Median_rent_price_norm', 'Home Ownership':'Home_ownership_norm'}

#Filter for county
county_selected = st.sidebar.selectbox('Select the county for COVID19 statistics', ('San Francisco', 'San Mateo', 'Santa Clara', 'Alameda'), index=0)

#Placing Title (Row 1)
row1_1 = st.beta_columns((1))
st.title("Impact of COVID19 on Property Rates in Bay Area")
st.write('Interactive Data Science')
st.write('Laura Howard, Arpit Kumar')
st.write('October, 22, 2020')
st.subheader("Property Rates vs Neighborhood Scores")

#Placing Maps (Row 2)
row2_1, row2_2, row2_3 = st.beta_columns((10,1,10))

with row2_1:
    try:
        #data filtered by beds
        data = zip_codes[zip_codes['Beds'] <= beds_selected]

        #data filtered by month
        data['Month'] = pd.DatetimeIndex(data['Date']).month
        data['year'] = pd.DatetimeIndex(data['Date']).year
        data['Amount_dollar'] = data.Amount_dollar.apply(lambda x: 0 if x == '-' else x)
        data.Amount_dollar = data.Amount_dollar.astype('int')
        data = data[data['year'] == 2020]
        data = data.apply(preprocess, axis = 1)
        data['Rate_dollar_sqft'] = data['Rate_dollar_sqft'].astype('float')

        if stat_selected == 'Mean':
            data = data[data['year'] == 2020].groupby(['Zip_Code','year','Month','Lat','Long'])['Rate_dollar_sqft'].mean().reset_index()
        else:
            data = data[data['year'] == 2020].groupby(['Zip_Code','year','Month','Lat','Long'])['Rate_dollar_sqft'].median().reset_index()

        property_rates = data[data['Month']==month_selected]
        map1(property_rates[['Rate_dollar_sqft','Lat','Long']], 37.224371, -121.905867 , 8)
        
        if property_rates.size == 0:
            st.write('No data was found for the selected filters')
    
    except Exception as e:
        st.write('No data was found for the selected filters')
        pass
    
with row2_3:
    score_on_map = pd.merge(df_Neighborhood_Score, property_rates, on='Zip_Code')
    score_on_map = score_on_map.fillna(0)
    score_on_map['Total_Crime'] = score_on_map['Total_Crime'].astype('int')
    score_on_map['Zip_Code'] = score_on_map['Zip_Code'].astype('str')
    df_Neighborhood_Score_norm = score_on_map.drop(['Zip_Code', 'Chance_of_being_a_victim','City', 'year', 'Month', 'Lat', 'Long', 'Rate_dollar_sqft'], axis=1).apply(norm,axis=1)

    try:
        score_on_map = score_on_map.join(df_Neighborhood_Score_norm)
        map2(score_on_map[['Lat','Long',score_type_map[score_selected], score_type_map_norm[score_selected]]], 37.224371, -121.905867, 8)
    
    except:
        map2(score_on_map[['Lat','Long']], 37.224371, -121.905867, 8)
        st.write('No data was found for the selected filters')
        pass
    
#Placing Graph (Row 3)
row3_1 = st.beta_columns((1))
st.subheader("COVID statistics in " + county_selected + " County")

#create map to get the last date of each month
last_date_map = {
    'Jan':31,
    'Feb':29,
    'Mar':31,
    'Apr':30,
    'May':31,
    'Jun':30,
    'Jul':31,
    'Aug':31,
    'Sep':30,
    'Oct':31
}

df_COVID_CA['Last_Update'] = pd.to_datetime(df_COVID_CA['Last_Update'], format='%d-%m-%Y')
df_COVID_CA['date'] = df_COVID_CA['Last_Update'].dt.strftime('%d').astype(int)
df_COVID_CA['month'] = df_COVID_CA['Last_Update'].dt.strftime('%b')
df_COVID_CA['last_date'] = df_COVID_CA['month'].map(last_date_map)

#select only last date of the month
df_COVID_CA = df_COVID_CA[df_COVID_CA['date']==df_COVID_CA['last_date']]

#filter on Santa Clara county
sc_data = df_COVID_CA[df_COVID_CA["County"] == county_selected]

month_map = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug',
            9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
sc_dt_data = sc_data[sc_data['month']== month_map[month_selected]]

#bar chart (altair)
con = int(sc_dt_data['Confirmed'])
dth = int(sc_dt_data['Deaths'])
act = int(sc_dt_data['Active'])

data = [['Confirmed',con],['Deaths',dth],['Active',act]]
chart_data = pd.DataFrame(data, columns = ['Metric', 'Number of Cases']) 

if sc_dt_data.count()[0] > 0:
    bars = alt.Chart(chart_data).mark_bar().encode(
    x=alt.X('Number of Cases:Q', scale=alt.Scale(domain=(0, 20000))),
    y='Metric:O'
).properties(width = 600, height=200).configure_mark(
    color='deeppink'
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3,
    color='black'
).encode(
    text='Number of Cases'
)

st.write(bars)

st.write(chart_data)

#Raw Datasets (Row 4)
row4_1 = st.beta_columns((1))
if st.checkbox ("Show Raw COVID Data"):
    st.write(df_COVID_CA)
