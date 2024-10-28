import streamlit as st
import pandas as pd

# Load the property database
properties = pd.read_csv('properties.csv')

st.title('Real Estate Assistant')

# Ask the user for their preferences
location = st.text_input('Where would you like to live?')
budget = st.slider('What is your budget?', 0, 1000000, 500000)
property_type = st.selectbox('What type of property are you looking for?', ['apartment', 'house', 'condo'])
bedrooms = st.slider('How many bedrooms do you need?', 1, 10, 2)
bathrooms = st.slider('How many bathrooms do you need?', 1, 10, 2)
amenities = st.multiselect('What amenities are you interested in?', ['parking', 'garden', 'pool'])
proximity = st.text_input('Do you need to be close to anything in particular (e.g. schools, public transportation)?')

# Filter the properties based on the user's preferences
filtered_properties = properties[
    (properties['location'] == location) &
    (properties['price'] <= budget) &
    (properties['type'] == property_type) &
    (properties['bedrooms'] == bedrooms) &
    (properties['bathrooms'] == bathrooms) &
    (properties['amenities'].apply(lambda x: all(amenity in x for amenity in amenities)))
]

# Show the filtered properties
st.dataframe(filtered_properties)

# Let the user select a property to view
selected_property = st.selectbox('Which property would you like to view?', filtered_properties.index)

# Show the details of the selected property
st.write(properties.loc[selected_property])

# Let the user schedule a viewing
if st.button('Schedule a viewing'):
    st.write('A viewing has been scheduled. A real estate agent will contact you soon.')