# Environment variables:
#
# * CONNECT_SERVER - The URL for your Posit Connect installation.
#
# * CONNECT_API_KEY - A Posit Connect API key.
#
# Example configuration:
#
#     CONNECT_SERVER="https://connect.companyname.com/"
#     CONNECT_API_KEY="NM6ZI4vluEHsyg5ViV3zK2bhBGqjiayA"

from rsconnect.api import RSConnectServer,RSConnectClient
import pandas as pd
import json
import requests 
import itables
from datetime import datetime

class Client:
    def __init__(self, server, api_key):
        self._server = server
        self._api_key = api_key
        #self._connect_client = RSConnectClient(RSConnectServer(url=self._server,api_key=self._api_key))

    def get_content(self):
        
        headers = { 'Authorization': 'Key ' + self._api_key}
        params = {"include": "owner,tags"}
        response = requests.get(self._server+"__api__/v1/content/", headers=headers, params=params)
        response_df = pd.DataFrame(response.json())
        return response_df


def connect(server,api_key): 
    return Client(server,api_key)


def rsc_table(content):
    if content.empty:
        raise ValueError('data argument missing')
    
    content['Owner'] = (pd.json_normalize(content['owner']))['username']
    content['Updated'] = pd.to_datetime(content['last_deployed_time']).dt.date
    content = content.rename(columns={"name": "Name", "app_mode": "Type"})
    
    itables.show(content[['Name','Owner','Updated','Type']])
