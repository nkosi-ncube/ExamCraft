import requests
import os
from dotenv import load_dotenv

def get_requests(user_input):
    load_dotenv()
    api_url = ''.format()
    response = requests.get(api_url, headers={'X-Api-Key': os.environ.get('GOOGLE_API_KEY')})
    if response.status_code == requests.codes.ok:
        
        print(response.text)
        # print(response.text)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    print(get_requests("what is java?"))


