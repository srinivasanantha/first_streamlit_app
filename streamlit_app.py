import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Put the picklist widget for customers to pickup fruits from list
fruits_selected=streamlit.multiselect("Pick the Fruits from List:", list( my_fruit_list.index),['Avocado', 'Strawberries'] )
fruits_to_show=my_fruit_list.loc[fruits_selected]
#Display the Fruits list on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
streamlit.title( "First Streamlit program with Github testing 1111...")
streamlit.text( "Check this line for any errors")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json() )
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json() )
streamlit.dataframe(fruityvice_normalized)
