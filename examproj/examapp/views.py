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
from google.cloud import storage
# Configure GenerativeAI with your API key
GOOGLE_API_KEY = "AIzaSyCHSc9DMrXir-k0pH1ojSpYMloLcwyDDW8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeModel with Gemini-Pro
model = genai.GenerativeModel('gemini-pro')

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
        if the_Message:
            
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, f"Please wait while i generate a response ...")
            ai_response = generate_reponse(the_Message)
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, ai_response)
        else:
            file_url = request.POST.get("MediaUrlO")
            file_name = "example"
            storage_client = storage.Client()
            bucket = storage_client.bucket("examcraft")
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_url)
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
    client.messages.create(
        body=message,
        from_=f'whatsapp:{from_number}',
        to=to_number
    )

