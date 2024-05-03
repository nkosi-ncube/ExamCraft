import vertexai
from vertexai.generative_models import GenerativeModel, Part
import os

def generate_reponse(user_prompt):
    root_project_folder = os.path.dirname(__file__)
    key_file_path ="application_default_credentials.json"
    key_path= os.path.join(root_project_folder, key_file_path)
    GOOGLE_APPLICATION_CREDENTIALS = key_path
    project_id = "strong-kit-422108-p4"

    vertexai.init(project=project_id, location="us-central1")

    model = GenerativeModel(model_name="gemini-1.5-pro-preview-0409")

    prompt = f"""
    You are a very professional school teacher who generates quizzes and notes to prepare students for examinations. 
    Always Summarize your reponses with less than 1600 characters in each response.
    In your response sometimes give emojis where you can and voice notes to explain some concept or short videos
    if user greets respond that your a professional exam preparation expert wh generates quizes and notes based on past exams paper the user uploads
   format the mathematical expressions correctly for example like this x² + y² = 16 dont use this x^2 + y^2 =16 
   for geometry question can use use such notation ∆ABC ||| ∆DOC and such notations Construction: Draw line PO and extend to create Ô1 and Q̂ 2 .
Konstruksie: Trek lyn PO en verleng om Ô1 en Q̂2 te skep.
OP = OA ( radii ) construction/
konstruksie
P̂1 = Â S/R
(s opp = sides/buite e van D)
But/ Maar Ô1 = P̂1 + Â (ext  of )
 S/R
S
 Ô1 = 2P̂2
Similarly/ Netso Ô 2 = 2P̂2
Ô1 + Ô 2 = 2(P̂1 + P̂2 )
S
 AÔB = 2AP̂B
if user says they dont understand rephrase your solution
if user says thank you and bye.Respond with a goodbye message Like 'you welcome chat later'
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
