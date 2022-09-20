import requests
import json
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
print(response.status_code)
with open('eng-ipa/data.json','w', encoding="utf-8") as f:
    f.write(str(response.text))
    f.close()

# Open the existing JSON file for loading into a variable
with open('eng-ipa/data.json') as jsondata:
  data = json.load(jsondata)

# Search data based on key and value using filter and list method
print(list(filter(lambda x:x["phonetics"]=="Nikolaos Gkikas",data)))