import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Put the picklist widget for customers to pickup fruits from list
streamlit.multiselect("Pick the Fruits from List:", list( my_fruit_list.index) )
#Display the Fruits list on the page
streamlit.dataframe(my_fruit_list)
                      
streamlit.title( "First Streamlit program with Github testing 123...")
streamlit.text( "Check this line for any errors")
