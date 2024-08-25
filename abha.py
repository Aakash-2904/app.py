import streamlit as st
import json

# Helper function to process the input data
def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase_alphabet = [max([ch for ch in alphabets if ch.islower()], default='')] if alphabets else []
    
    return {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your actual user_id
        "email": "john@xyz.com",  # Replace with your actual email
        "roll_number": "ABCD123",  # Replace with your actual roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

# Streamlit application
def main():
    st.title("Bajaj Finserv Health Challenge")

    # Input section
    st.header("Input JSON")
    json_input = st.text_area("Enter JSON here", height=100)
    
    if st.button("Submit"):
        try:
            # Parse the JSON input
            data = json.loads(json_input).get("data", [])
            
            # Process the data
            response = process_data(data)
            
            # Display the response
            st.json(response)
            
            # Multi-select dropdown for filtering response
            options = st.multiselect("Select what to display", ["numbers", "alphabets", "highest_lowercase_alphabet"])
            
            st.header("Filtered Response")
            if "numbers" in options:
                st.write(f"Numbers: {response['numbers']}")
            if "alphabets" in options:
                st.write(f"Alphabets: {response['alphabets']}")
            if "highest_lowercase_alphabet" in options:
                st.write(f"Highest Lowercase Alphabet: {response['highest_lowercase_alphabet']}")

        except json.JSONDecodeError:
            st.error("Invalid JSON format. Please enter valid JSON.")

    # GET operation simulation
    st.header("GET Operation")
    if st.button("Get operation_code"):
        st.json({"operation_code": 1})

if __name__ == '__main__':
    main()
