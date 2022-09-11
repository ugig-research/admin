import streamlit as st
import pandas as pd
import numpy as np
import json
from api_lib import call_ugig_api


st.title('UGIG Admin')


fetch_collections_body = {
  "operation": "FetchCollections",
  "payload": {}
}
fetch_collections_response = call_ugig_api(json.dumps(fetch_collections_body))
collections_df = pd.DataFrame(fetch_collections_response['collections'])


st.subheader('Collections')
st.write(f"Total Collections:  {fetch_collections_response['count']}")
st.dataframe(collections_df)


fetch_profile_packs_body = {
  "operation": "FetchProfilePacks",
  "payload": {}
}
fetch_profile_packs_response = call_ugig_api(json.dumps(fetch_profile_packs_body))
profile_packs_df = pd.DataFrame(fetch_profile_packs_response['profile_packs'])


st.subheader('Profile Packs')
st.write(f"Total Profile Packs:  {fetch_profile_packs_response['count']}")
st.dataframe(profile_packs_df)