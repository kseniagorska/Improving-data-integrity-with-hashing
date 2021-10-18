# Improving Data Integrity with Hashing
################################################################################
# An application that uses the hashlib library and Streamlit to hash any text input.

# Importing required libraries
import hashlib
import streamlit as st


# Creating a function to hash an input value.

def hash_data(data):

    # Instantiating an instance of hashlib's `sha256` function
    sha = hashlib.sha256()

    # Using the `encode` function to encode the string version of the data that
    # was passed in as a parameter to the function
    encoded_data = str(data).encode()

    # Calling the hashing instance and the `update` function. Pass it the encoded
    # data as a parameter
    sha.update(encoded_data)

    # Returning the unique hash of the data using the `hexidigest` function
    return sha.hexdigest()

################################################################################
# Streamlit Code

# Create the application header using a markdown string
st.markdown("# Create a Unique Hash of Data")

################################################################################

# Adding a Streamlit `text_area` component to accept data from the user.
input_data = str(st.text_area("Enter Data")).encode()

# Using the Streamlit `write` function to display the length (`len) of the input
# data back to the user
st.write(f"Input Length: {len(input_data)}")

################################################################################

# Adding a Streamlit `button` named “Hash Text”. When the button is clicked, use
# the `hash_data` function to first generate a hash of the user's text and then
# display that hash on the page.


# Add a Streamlit `button` named “Hash Text”
if st.button("Hash Text"):

    # Generate a hash of the user input using the `hash_data` function
    input_hash = hash_data(input_data)

    # Use the Streamlit `write` function to display the unique hash of the data
    st.write(f"Output Hash (fingerprint): {input_hash}")

    # Use the Streamlit `write` function to display the length of the output
    # hash.
    st.write(f"Output Length: {len(input_hash)}")
################################################################################

