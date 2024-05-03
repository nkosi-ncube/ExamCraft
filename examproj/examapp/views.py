from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
from twilio.rest import Client
from examapp import *
from .whatsapp_intergration import get_requests
from twilio.twiml.messaging_response import MessagingResponse
import PyPDF2
import google.generativeai as genai
from .ai import generate_reponse
import requests
from google.cloud import storage
from google.oauth2 import service_account
# Configure GenerativeAI with your API key
GOOGLE_API_KEY = "AIzaSyCHSc9DMrXir-k0pH1ojSpYMloLcwyDDW8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeModel with Gemini-Pro
model = genai.GenerativeModel('gemini-pro')



def download_file(url, destination_file):
    """Downloads a file from a URL....."""
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    response = requests.get(url, auth=(account_sid, auth_token))
    print(response)
    if response.status_code == 200:
        with open(destination_file, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download file from {url}")

@csrf_exempt
def home(request):
    load_dotenv()
    
    TWILID_PHONE_NUMBER = os.environ.get("TWILID_PHONE_NUMBER")
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    
    if request.method == "POST":
        message = request.POST
        print(message)
        Name = message["ProfileName"]
        the_number = message["From"]
        the_Message = message["Body"]
        if the_Message in ["hie","hey","hello","hy"]:
             client.messages.create(                 
                from_=f'whatsapp:{TWILID_PHONE_NUMBER}',
                media_url="https://youtu.be/lVaDO4AE5JY",
                to=the_number
    )
        elif the_Message not in ["hie","hey","hello","hy"]:
            
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, f"Please wait while i generate a response ...")
            ai_response = generate_reponse(the_Message)
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, ai_response)
        else:
            file_url = request.POST.get("MediaUrl0")
            print(file_url)
            file_name = "nkosi.pdf"

            # Find the root project folder
            root_project_folder = os.path.dirname(__file__)

            # Construct the full path to the PDF file
            temp_file = os.path.join(root_project_folder, file_name)
            print(temp_file)
            download_file(file_url, temp_file)

            file_name = "file.pdf"
            key_file_path ="creds.json"
            key_path= os.path.join(root_project_folder, key_file_path)
            
            print(key_path)
            # Initialize the storage client with explicit credentials
            credentials = service_account.Credentials.from_service_account_file(key_path)
            storage_client = storage.Client(credentials=credentials)
          
            bucket = storage_client.bucket("examcraft")
            blob = bucket.blob(file_name)
            current_dir = os.path.abspath(__file__)
            print(current_dir)
            blob.upload_from_filename(temp_file)
            print(f"File {file_url} uploaded succesfully!!")
            
       

    return render(request, 'home.html')

def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def generate_content_from_pdf(pdf_text):
    response = model.generate_content(pdf_text)
    return response.text

def send_whatsapp_message(from_number, to_number, message):
    client = Client(os.environ.get("ACCOUNT_SID"), os.environ.get("AUTH_TOKEN"))
    message_parts = [message[i:i+1599] for i in range(0, len(message), 1600)]

    # Send each message part
    for i, part in enumerate(message_parts, start=1):
        print(f"Message part {i}: {len(part)} characters")
        # Append part number to the message
        part_message = f"{part} ({i}/{len(message_parts)})"

        client.messages.create(
        body=part_message,
        from_=f'whatsapp:{from_number}',
        to=to_number
    )
    
   

