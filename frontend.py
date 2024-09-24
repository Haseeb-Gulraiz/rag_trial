import streamlit as st
import requests

# Set the Flask API URL
API_URL = "http://127.0.0.1:5000/ask"

# Streamlit app title
st.title("Helpful Assistant")

# Input for user query
user_query = st.text_input("Ask about vegetables")

# Button to submit the query
if st.button("Submit"):
    if user_query:
        try:
            # Make a request to the Flask API
            response = requests.post(API_URL, json={"query": user_query})
            
            if response.status_code == 200:
                # Extract and display the response from the API
                api_response = response.json().get("response", "No response received")
                st.write("**Response:**")
                st.write(api_response)
            else:
                st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Failed to connect to the API: {e}")
    else:
        st.warning("Please enter a query.")