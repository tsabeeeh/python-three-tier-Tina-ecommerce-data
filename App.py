import streamlit as st
from Backend import process_request

#(Configuration page) ---
st.set_page_config(
    page_title="E-Commerce",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.title("Query System")
st.markdown("---")
# UI Components ---

# Choose Database
st.sidebar.header("Choose Database")
db_option = st.sidebar.radio(
    " Select the database want to query from:",
    ('MySQL', 'MongoDB')
)

st.header(f" {db_option}")

if db_option == 'MySQL':
    st.info("Enter SQL query :   SELECT Name, Price FROM customers WHERE price > 50)  ")
    query_hint = "SELECT Name, Email, Price FROM customers WHERE product = ' Galaxy Tab A8 ';"
else: # MongoDB
    st.info('Enter Mongo SQL query in JOSN format (Example: {"Name":"omar"})')
    query_hint = '{"Name":"omar"}'

# Enter Query into the box
user_query = st.text_area(
    "Enter Your Query Here",
    value=query_hint,
    height=150
)

if st.button("Eecxute Query"):
   
    result = process_request(db_option, user_query)
    
    st.markdown("---")
    st.subheader("Query Results:")

    st.code(result, language='json' if db_option == 'MongoDB' else 'sql')
    
st.sidebar.markdown("---")
st.sidebar.caption("Tina E-Commerce ")