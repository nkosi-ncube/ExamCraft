# ExamCraft: AI-Powered Study Companion

## Overview

Welcome to ExamCraft!

ExamCraft is your ultimate AI-powered study companion, designed to transform how you prepare for exams. Our innovative platform takes the stress out of studying by analyzing past exam papers and generating personalized study materials that cater specifically to your needs.

Here’s how ExamCraft works:

Smart Analysis: ExamCraft uses advanced Natural Language Processing (NLP) technology from spaCy and Hugging Face Transformers to thoroughly analyze past exam papers. This helps us understand the types of questions that frequently appear and the key topics you need to focus on.

Customized Learning: Once the analysis is complete, our system leverages powerful Machine Learning models from Google GenerativeAI and Vertex AI to create personalized study materials just for you. This ensures that you’re studying the right material and can maximize your efficiency.

Convenient Delivery: We understand the importance of convenience in today’s fast-paced world. That’s why ExamCraft delivers all your study resources directly to your WhatsApp. This way, you can study anytime, anywhere, right from your phone.

AI Assistance: Sometimes, text explanations might not be enough. If you ever find yourself stuck or needing more detailed help, simply request a call from our AI assistant. Our AI will call you and provide a comprehensive explanation, ensuring you fully understand the topic.

With ExamCraft, you’re not just studying harder; you’re studying smarter. Let us help you take your exam preparation to the next level. Transform your study experience with ExamCraft and ace your exams like never before!

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
