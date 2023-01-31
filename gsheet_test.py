# streamlit_app.py

import streamlit as st
###from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

# Create a connection object.
connection = connect(":memory:")
cursor = connection.cursor()

# Perform SQL query on the Google Sheet.
### Uses st.cache to only rerun when the query changes or after 10 min.

sheet_url = st.secrets["public_gsheets_url"]
query = "SELECT * FROM sheet_url"

# Print results.
for row in cursor.execute(query):
    print(row)

