import streamlit
import pandas
streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast menu")
streamlit.text("Omega 3 & Blueberry oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothy")
streamlit.text("Hard boiled free-range egg ")
streamlit.header("Build your own Smoothie")


my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)                              
fruits_selected=streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index),['Apple','Avocado'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit you like information about?', 'watermelon')
streamlit.write('The user entered ',  fruit_choice )

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

