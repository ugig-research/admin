import streamlit as st
import pandas as pd
import numpy as np
import json
from api_lib import call_ugig_api


st.title('UGIG Admin')

fetch_users_body = {
  "operation": "FetchUsers",
  "payload": {}
}
fetch_user_response = call_ugig_api(json.dumps(fetch_users_body))
users_df = pd.DataFrame(fetch_user_response['users'])

st.subheader('Users')
st.write(f"Total Users:  {fetch_user_response['count']}")
st.dataframe(users_df)