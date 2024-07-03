# ExamCraft: AI-Powered Study Companion

## Overview

Welcome to ExamCraft!

ExamCraft is your ultimate AI-powered study companion, designed to transform how you prepare for exams. Our innovative platform takes the stress out of studying by analyzing past exam papers and generating personalized study materials that cater specifically to your needs.

Here’s how ExamCraft works:

- **Smart Analysis**: ExamCraft uses advanced Natural Language Processing (NLP) technology from spaCy and Hugging Face Transformers to thoroughly analyze past exam papers. This helps us understand the types of questions that frequently appear and the key topics you need to focus on.

- **Customized Learning**: Once the analysis is complete, our system leverages powerful Machine Learning models from Google GenerativeAI and Vertex AI to create personalized study materials just for you. This ensures that you’re studying the right material and can maximize your efficiency.

- **Convenient Delivery**: We understand the importance of convenience in today’s fast-paced world. That’s why ExamCraft delivers all your study resources directly to your WhatsApp. This way, you can study anytime, anywhere, right from your phone.

- **AI Assistance**: Sometimes, text explanations might not be enough. If you ever find yourself stuck or needing more detailed help, simply request a call from our AI assistant. Our AI will call you and provide a comprehensive explanation, ensuring you fully understand the topic.

With ExamCraft, you’re not just studying harder; you’re studying smarter. Let us help you take your exam preparation to the next level. Transform your study experience with ExamCraft and ace your exams like never before!

## Future Improvements

### Interactive Features

- **Quizzes and Practice Tests**: Generate quizzes and practice tests based on analyzed past papers, allowing users to test their knowledge and get immediate feedback.

- **Progress Tracking**: Include a dashboard that tracks users’ study progress, highlighting strengths and areas needing improvement.

### Personalization Features

- **Adaptive Learning Pathways**: Develop adaptive learning pathways that adjust based on user performance, ensuring they focus on topics they struggle with the most.

- **Study Schedule Planner**: Integrate a study schedule planner that creates personalized study timetables based on the user’s exam dates and availability.

### Collaborative Features

- **Study Groups**: Allow users to join or form study groups based on similar subjects or exam dates, fostering collaborative learning.

- **Peer-to-Peer Tutoring**: Implement a feature where users can either request help from peers who excel in certain subjects or offer tutoring services themselves.

### Enhanced AI Assistance

- **Voice Interaction**: Introduce voice interaction capabilities so users can ask questions and get explanations in real-time without needing to type.

- **AI-Powered Flashcards**: Generate AI-powered flashcards for key concepts and terms, using spaced repetition to help users memorize information efficiently.

### Content Expansion

- **Video Tutorials**: Offer video tutorials and lectures from experts covering difficult topics, providing an alternative learning method.

- **Resource Library**: Create a resource library with additional study materials like e-books, notes, and reference articles related to the subjects.

### Gamification

- **Achievements and Rewards**: Introduce a gamification system with achievements, badges, and rewards to motivate users and make studying more engaging.

- **Leaderboards**: Implement leaderboards to create a sense of competition and encourage users to stay committed to their study routines.

### Accessibility and Inclusivity

- **Multilingual Support**: Add support for multiple languages to cater to non-native English speakers.

- **Accessibility Options**: Ensure the platform is accessible to users with disabilities, including features like text-to-speech, adjustable font sizes, and high-contrast modes.

### Security and Privacy

- **Data Security**: Implement robust security measures to protect user data and ensure privacy, including encryption and secure login methods.

- **Parental Controls**: Provide parental control options for younger users, allowing parents to monitor and manage their child’s study activities.

Incorporating these features can make ExamCraft even more comprehensive and user-friendly, offering a more holistic approach to exam preparation.

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
