import vertexai
from vertexai.generative_models import GenerativeModel, Part


def generate_reponse(user_prompt):

    project_id = "strong-kit-422108-p4"

    vertexai.init(project=project_id, location="us-central1")

    model = GenerativeModel(model_name="gemini-1.5-pro-preview-0409")

    prompt = f"""

    You are a very professional school teacher who generates quizzes and notes to prepare students for examinations. 
    Summarize with less than 1600 characters in each response
    {user_prompt} from the given document.

    """

    pdf_file_uri = "gs://examcraft/file.pdf"

    pdf_file = Part.from_uri(pdf_file_uri, mime_type="application/pdf")

    contents = [pdf_file, prompt]

    print("Please wait while i generate a response ..... ")

    response = model.generate_content(contents)

    print(response.text)

    return response.text


if __name__ == "__main__":

    generate_reponse(input("Enter your prompt:"))

# import os

# import vertexai

# from vertexai.generative_models import GenerativeModel, Part

# from google.cloud import storage


# def list_files_in_folder(bucket_name, folder_name):

#     """Lists all files in a GCS folder."""

#     print(f"Fetching all pdfs in the folder {bucket_name}/{folder_name}")

#     storage_client = storage.Client()

#     bucket = storage_client.get_bucket(bucket_name)

#     folder_files = bucket.list_blobs(prefix=folder_name)

#     print(f"FILENAME: gs://{bucket_name}/" )

#     return [f"gs://{bucket_name}/{file.name}" for file in folder_files]


# def generate_response(user_prompt, pdf_gcs_uris):

#     project_id = "strong-kit-422108-p4"

#     vertexai.init(project=project_id, location="us-central1")

#     model = GenerativeModel(model_name="gemini-1.5-pro-preview-0409")


#     prompt = f"""

#     You are a very professional school teacher who generates quizzes and notes to prepare students for examinations.

#     {user_prompt} from the given documents.

#     """


#     pdf_files = [Part.from_uri(uri, mime_type="application/pdf") for uri in pdf_gcs_uris]


#     contents = [prompt] + pdf_files


#     print("Please wait while I generate a response...")

#     response = model.generate_content(contents)

#     print(response.text)

#     return response.text


# if __name__ == "__main__":

#     bucket_name = "examcraft"

#     folder_name = "pdf_files"

#     pdf_gcs_uris = list_files_in_folder(bucket_name, folder_name)

#     prompt = input("Enter your prompt: ")

#     generate_response(prompt, pdf_gcs_uris)
