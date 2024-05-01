# ExamCraft: AI-Powered Study Companion

## Overview

ExamCraft is an innovative AI-powered study companion designed to enhance exam preparation methods by analyzing past exam papers, generating personalized study materials, and delivering them to users via messaging platforms like WhatsApp. This README provides guidance on how to implement the project using various technologies, including Natural Language Processing (NLP), Machine Learning (ML), messaging platforms integration, web development with Streamlit, and PDF analysis.

## Technologies and Resources

### Natural Language Processing (NLP)

- **NLTK**: [NLTK Documentation](https://www.nltk.org/)
- **spaCy**: [spaCy Documentation](https://spacy.io/)
- **Hugging Face Transformers**: [Hugging Face Transformers](https://huggingface.co/transformers/)

### Machine Learning (ML)

- **TensorFlow**: [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- **PyTorch**: [PyTorch Tutorials](https://pytorch.org/tutorials/)
- **OpenAI GPT Models**: [OpenAI GPT Models](https://openai.com/gpt)

### Messaging Platforms Integration

- **Twilio WhatsApp API**: [Twilio WhatsApp API Docs](https://www.twilio.com/docs/whatsapp)

### Web Development (Streamlit)

- **Streamlit Documentation**: [Streamlit Documentation](https://docs.streamlit.io/)
- **Streamlit Gallery**: [Streamlit Gallery](https://streamlit.io/gallery)

### PDF Analysis

- **PyPDF2**: [PyPDF2 GitHub](https://github.com/mstamy2/PyPDF2)
- **pdfminer.six**: [pdfminer.six GitHub](https://github.com/pdfminer/pdfminer.six)

## Implementation Steps

1. **Upload Exam Paper via Streamlit UI**: Develop a Streamlit web application where users can upload exam papers in PDF format.

2. **NLP Analysis**: Analyze the uploaded exam paper text using NLP techniques to extract key concepts and structures.

3. **ML Study Materials Generation**: Utilize ML algorithms to generate personalized study materials (quizzes, notes) based on the NLP analysis.

4. **WhatsApp Integration**: Integrate with the Twilio WhatsApp API to send the generated study materials to users via WhatsApp messages.

5. **PDF Analysis for Diagrams**: Utilize PDF analysis libraries to handle questions with diagrams by extracting text from PDF files. Further enhancements can include image processing techniques to handle diagrams.

## Project Structure

- `nlp_analysis.py`: Contains code for NLP analysis of exam papers.
- `ml_generation.py`: Contains code for ML-based generation of study materials.
- `whatsapp_integration.py`: Contains code for integrating with the Twilio WhatsApp API.
- `streamlit_app.py`: Contains code for the Streamlit web application.
- `pdf_analysis.py`: Contains code for PDF analysis to handle questions with diagrams.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit web application using `streamlit run streamlit_app.py`.
4. Follow the on-screen instructions to upload an exam paper and receive personalized study materials via WhatsApp.

