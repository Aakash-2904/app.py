import streamlit as st
import json
import requests

# Set the title of the Streamlit app (which is also the tab title)
st.set_page_config(page_title="Your Roll Number")

# Application title
st.title("API Input")

# Input JSON
json_input = st.text_area("API Input", '{"data":["M","1","334","4","B"]}', height=100)

# Submit button
if st.button("Submit"):
    try:
        # Parse the JSON input
        parsed_input = json.loads(json_input)
        
        # Call the backend API
        response = requests.post('YOUR_BACKEND_API_ENDPOINT/bfhl', json=parsed_input)
        data = response.json()

        # Store the response in session state
        st.session_state.response = data
        st.success("Valid JSON submitted!")

    except json.JSONDecodeError:
        st.error("Invalid JSON format")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

# Display the multi-select dropdown if a response is available
if "response" in st.session_state:
    st.subheader("Multi Filter")

    options = ['Alphabets', 'Numbers', 'Highest Lowercase Alphabet']
    selected_options = st.multiselect("", options, default="Numbers")

    # Filter and display the response based on selected options
    filtered_data = []
    if 'Alphabets' in selected_options:
        filtered_data.extend(st.session_state.response.get('alphabets', []))
    if 'Numbers' in selected_options:
        filtered_data.extend(st.session_state.response.get('numbers', []))
    if 'Highest Lowercase Alphabet' in selected_options:
        filtered_data.extend(st.session_state.response.get('highestLowercase', []))

    # Display the filtered response
    if filtered_data:
        st.subheader("Filtered Response")
        st.write(", ".join(map(str, filtered_data)))
