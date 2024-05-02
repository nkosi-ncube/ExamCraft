# ExamCraft: AI-Powered Study Companion

## Overview

ExamCraft is an innovative AI-powered study companion designed to enhance exam preparation methods by analyzing past exam papers, generating personalized study materials, and delivering them to users via messaging platforms like WhatsApp. This README provides guidance on how to implement the project using various technologies, including Natural Language Processing (NLP) with spaCy and Hugging Face Transformers, and Machine Learning (ML) with Google GenerativeAI and Vertex AI.

## Technologies and Resources

### Machine Learning (ML)

- **Google GenerativeAI**: [Google GenerativeAI](https://cloud.google.com/generative-ai/docs)
- **Vertex AI**: [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)

### Messaging Platforms Integration

- **Twilio WhatsApp API**: [Twilio WhatsApp API Docs](https://www.twilio.com/docs/whatsapp)

## Implementation Steps

1. **Receive User Prompt**: Implement a Django web application (`views.py`) where users can input their study prompts.
2. **PDF Retrieval**: Within the Django application, retrieve the relevant PDF document containing exam information.
3. **AI Content Generation**: Utilize the `ai.py` script to generate study materials based on the user prompt and exam document using Google GenerativeAI.
4. **Twilio Integration**: Integrate with the Twilio WhatsApp API to send the generated study materials to users via WhatsApp messages.

## Project Structure

- `README.md`: This document providing an overview of the project.
- `ai.py`: Contains functions for generating study materials using Google GenerativeAI.
- `views.py`: Django view functions for handling user requests and generating study materials.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Directory containing static files (e.g., CSS, JavaScript) for the web interface.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your Google Cloud Storage account and Twilio account, obtaining necessary credentials.
4. Update the environment variables in your Django settings file (`settings.py`) with your Google Cloud Storage and Twilio credentials.
5. Run the Django web application using `python manage.py runserver`.
6. Access the web application through your browser, input the study prompt, and receive study materials via WhatsApp.

### To run on whatsapp 

1. First add the following number :+14155238886 to join the Twilio Sandbox.
2. Secondly send `join master-roll` to the saved number.

