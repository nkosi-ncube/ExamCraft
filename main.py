import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import PIL.Image

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


def get_vision_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
    return llm


def get_llm():
    llm = GoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm


def get_template():
    template = """Question: {question}

    Answer: Let's think step by step."""
    return template


def get_prompt(template):
    prompt = PromptTemplate.from_template(template)
    return prompt


def get_image_promt(image_url, text="What's in this image?"):
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": f"{text}",
            },  # You can optionally provide text parts
            {"type": "image_url", "image_url": f"{image_url}"},
        ]
    )
    return message


if __name__ == "__main__":
    img = PIL.Image.open('image.jpeg')
    vision_llm = get_vision_llm()
    llm = get_llm()

    prompt = "What's in this image?"
    message = get_image_promt(image_url="image.jpeg", text=prompt)

    chat = vision_llm.invoke([message])
    print(chat.content)

    template = """Question: {question}

Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm

    question = "Please answer the question from the image"
    print(chain.invoke({"question": question}))