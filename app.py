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
response = call_ugig_api(json.dumps(fetch_collections_body))
collections_df = pd.DataFrame(response['collections'])


st.subheader('Collections')
st.write(f"Total Collections:  {response['count']}")
st.dataframe(collections_df)