import pandas as pd
import numpy as np
import requests
import json
import os
import pprint
from states import us_states

json_files = [file for file in os.listdir() if file.endswith("json")]
json_files

def DS_Data(state):
    if f"{state}.json" not in json_files:
        url = "https://www.datastro.eu/api/records/1.0/search/"
        payload  = {"dataset": "imageserver",
                    "rows": "9999",
                    "sort": "limitingmag",
                    "facet": "limitingmag",
                    "facet": "localdate",
                    "facet": "utdate",
                    "facet": "sqmreading",
                    "facet": "sqmserial",
                    "facet": "cloudcover",
                    "facet": "constellation",
                    "facet": "country",
                    "facet": "filename",
                    "refine.country": state
               }
        r = requests.get(url, params=payload)
        d = r.json()

        records = [
            {
                "Country": record["fields"]["country"],
                "Limiting Magnitude": record["fields"]["limitingmag"],
                "Date": record["fields"]["localdate"],
                "Coordinates": record["fields"]["coord"]} for record in d["records"]]
    
        with open(f"{state}.json", "w+") as f:
            f.write(json.dumps(records))

for state in us_states:
    try:
        result = DS_Data(state)
    except:
        pass