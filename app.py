import streamlit as st
import pandas as pd
import numpy as np
import json
from datetime import datetime as dt
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

accounts_created_df = users_df[['UserCreateDate', 'UserStatus']].copy()
def convert_date_strings(x):
    sub_str = x[0:10]
    format = "%Y-%m-%d"
    date = dt.strptime(sub_str, format)
    return date
accounts_created_df['AccountCreatedDate'] = accounts_created_df['UserCreateDate'].apply(convert_date_strings)

accounts_created_df = accounts_created_df['AccountCreatedDate'].value_counts().rename_axis('Date').reset_index(name='New Users')
st.bar_chart(data=accounts_created_df, x='Date', y='New Users')

