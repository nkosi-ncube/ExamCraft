import requests
from concurrent.futures import ThreadPoolExecutor


def make_call(customer_number):
    # Your Vapi API Authorization token
    auth_token = ''
    # The Phone Number ID, and the Customer details for the call
    phone_number_id = ''
    # customer_number = "+17069141629"
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'assistant': {
            "firstMessage": """Hello there.
I am calling on behalf of SACCC to address the concerns you raised regarding the delay in payments.
First and foremost, we sincerely apologize for the inconvenience this has caused. We understand how frustrating it is, especially for those of you who need transport home or haven’t had a chance to eat all day.
Please know that we are actively working on resolving this issue as quickly as possible. We appreciate your patience and understanding during this time.
We also want to take this opportunity to thank you for the incredible work you have done today. Your dedication and effort have been crucial in making this event a success, and we deeply value your contribution.
Thank you for your continued support. If you have any further concerns or need assistance, please do not hesitate to let us know.
""",
            "model": {
                "provider": "openai",
                "model": "gpt-4-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an assistant.That speaks clearly and fluently to address the concerns  raised regarding the delay in payments."
                    }
                ]
            },
            "numWordsToInterruptAssistant": 1,
            "voice": {
            "provider": "playht",
            "voiceId": "jennifer-playht",
            "speed": 0.9  ,
        },
         "endCallPhrases": [
    "goodbye","that will be all for now","thank you thats"
  ],
        },
        'phoneNumberId': phone_number_id,
        'customer': {
            'number': customer_number,
        },
    }
    response = requests.post(
        'https://api.vapi.ai/call/phone', headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 201:
        print(f'Call to {customer_number} created successfully')
    else:
        print(f'Failed to create call to {customer_number}')
# customers = []
# with ThreadPoolExecutor(max_workers=len(customers)) as executor:
#     executor.map(make_call, customers)

if __name__ == "__main__":
    make_call("+27692150305")
