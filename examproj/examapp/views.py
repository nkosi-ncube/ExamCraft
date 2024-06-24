import os
import tempfile
import mimetypes
import PyPDF2
from google.cloud import storage
from google.oauth2 import service_account
import requests
from twilio.rest import Client
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import boto3
import time
import google.generativeai as genai
from .caller import make_call

# Initialize GenerativeAI with your API key
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the GenerativeModel with Gemini-Pro
model = genai.GenerativeModel('gemini-pro')

# Function to handle file download
def download_file(url, destination_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination_file, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download file from {url}")

# Function to upload file to cloud storage
def upload_to_cloud_storage(file_path, bucket_name, blob_name):
    credentials = service_account.Credentials.from_service_account_file("creds.json")
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

# Function to generate response from PDF
def generate_response_from_pdf(pdf_file_path):
    pdf_text = extract_text_from_pdf(pdf_file_path)
    response = model.generate_content(pdf_text)
    return response.text

# Function to handle image upload
def handle_image_upload(file_url, file_name):
    download_file(file_url, file_name)
    mime_type, _ = mimetypes.guess_type(file_name)
    if not mime_type or not mime_type.startswith('image'):
        return None
    return file_name

# Function to generate response from image
def generate_response_from_image(image_file_path):
    # Placeholder function for generating response from image
    return "Response from image"

# Function to send WhatsApp message
def send_whatsapp_message(from_number, to_number, message):
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message_parts = [message[i:i+1599] for i in range(0, len(message), 1600)]
    for i, part in enumerate(message_parts, start=1):
        print(f"Message part {i}: {len(part)} characters")
        part_message = f"{part} ({i}/{len(message_parts)})"
        client.messages.create(
            body=part_message,
            from_=f'whatsapp:{from_number}',
            to=to_number
        )

# @csrf_exempt
# def home(request):
#     load_dotenv()
#     TWILID_PHONE_NUMBER = os.environ.get("TWILID_PHONE_NUMBER")
#     if request.method == "POST":
#         message = request.POST
#         if message['MessageType'] == "document":
#             file_url = message.get("MediaUrl0")
#             file_name = "temp.pdf"
#             temp_file_path = os.path.join(tempfile.gettempdir(), file_name)
#             download_file(file_url, temp_file_path)
#             upload_to_cloud_storage(temp_file_path, "examcraft", file_name)
#             ai_response = generate_response_from_pdf(temp_file_path)
#             send_whatsapp_message(TWILID_PHONE_NUMBER, message["From"], ai_response)
#         elif message['MessageType'] == "image":
#             file_url = message.get("MediaUrl0")
#             file_name = "temp_image.jpg"
#             temp_file_path = os.path.join(tempfile.gettempdir(), file_name)
#             image_file_name = handle_image_upload(file_url, temp_file_path)
#             if image_file_name:
#                 upload_to_cloud_storage(temp_file_path, "examcraft", file_name)
#                 ai_response = generate_response_from_image(temp_file_path)
#                 send_whatsapp_message(TWILID_PHONE_NUMBER, message["From"], ai_response)
#         else:
#             # Message type is not "document" or "image"
#             the_Message = message["Body"]
#             if the_Message.lower() not in ["hie", "hey", "hello", "hy", ""]:
#                 send_whatsapp_message(TWILID_PHONE_NUMBER, message["From"], "Please wait while I generate a response ...")
#                 ai_response = generate_reponse(the_Message)
#                 send_whatsapp_message(TWILID_PHONE_NUMBER, message["From"], ai_response)
#     return render(request, 'home.html')




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
import boto3
import time
# Configure GenerativeAI with your API key
GOOGLE_API_KEY = "
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
        print(the_Message)
        if the_Message.lower() in ["hie","hey","hello","hy"]:
            print("i get in here")
            print("i just got updated")
            s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
            bucket_name = 'whatsapp-music-downloader'
            # print("please wait while song gets uplaoded to AWS S3 BUCKET")
            # s3.upload_file(output_path, bucket_name, filename, ExtraArgs={'ContentType': 'audio/mpeg'})
            # print("Song uploaded to S3 bucket successfully.")

            # print(f"File {filename} uploaded to S3 bucket {bucket_name}.")
            # print(f"bucket url: https://{bucket_name}.s3.amazonaws.com/{filename}") 
            client.messages.create(                 
                from_=f'whatsapp:{TWILID_PHONE_NUMBER}',
                body="A video to explain what is ExamCraft will be sent shortly.",
                to=the_number)
            time.sleep(3)
            bucket_url_path = f"https://{bucket_name}.s3.amazonaws.com/ExamCraft.mp4"
            print(bucket_url_path)
            client.messages.create(                 
                from_=f'whatsapp:{TWILID_PHONE_NUMBER}',
                media_url=bucket_url_path,
                to=the_number
    )
            time.sleep(5)
        elif the_Message not in ["hie","hey","hello","hy",""]:
            
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, f"Please wait while i generate a response ...")
            ai_response = generate_reponse(the_Message)
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, ai_response)
        elif message['MessageType'] == "document":
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
        elif the_Message.has(' i do not understand'):
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, "Please give me your number for calls so i can call you.TYPE LIK THIS : phone +2760567334")
        elif the_Message.has("phone"):
            send_whatsapp_message(TWILID_PHONE_NUMBER, the_number, "You will receive a call from a +13 number to further explain")
            make_phone_call(the_Messag.strip()[5:])

        
        
       

    return render(request, 'home.html')


def make_phone_call(phone_number):
    make_call(phone_number)

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
    
   

