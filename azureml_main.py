# The script MUST contain a function named azureml_main
# which is the entry point for this module.

import json
import urllib2
from pandas.io.json import json_normalize

def azureml_main():

    data = json.load(urllib2.urlopen("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"))
      
    dataframe = json_normalize(data)

    # Return value must be of a sequence of pandas.DataFrame
    return dataframe,
