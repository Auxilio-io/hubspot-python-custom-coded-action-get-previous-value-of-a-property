import requests
import os

def main(event):
    token = os.getenv('YOUR_TOKEN')
    contact_id = event.get('inputFields').get('hs_object_id')

    your_property
  
    try:
        url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}?properties={your_property}&propertiesWithHistory={your_property}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers).json()
        previous_value = response['propertiesWithHistory']['your_property'][1]['value']
    except requests.exceptions.RequestException as e:
        print(f"A Requests error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return {
        "outputFields": {
            "previous_value": previous_value
        }
    }
