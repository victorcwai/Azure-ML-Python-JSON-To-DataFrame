# Azure-ML-Python-JSON-To-DataFrame

Python Language Modules -> Execute Python Script

    import json
    import urllib2
    from pandas.io.json import json_normalize

    def azureml_main():
    
        # Replace with the URL of your JSON file
        data = json.load(urllib2.urlopen("http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"))

        dataframe = json_normalize(data)

        return dataframe,
