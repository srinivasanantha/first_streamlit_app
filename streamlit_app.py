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


streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index), ['Avacado', 'Strawberries'] )

streamlit.dataframe(my_fruit_list)
