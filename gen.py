from langchain import HuggingFaceHub, PromptTemplate, LLMChain
import re
import os

# Import configuration
from config import model_id, model_kwargs

# Initialize the Falcon-7B-Instruct model
falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                            repo_id=model_id,
                            model_kwargs=model_kwargs)

# Define the Prompt Template
template = """Respond to the following user input:

{question}

Response:"""

prompt = PromptTemplate(template=template, input_variables=['question'])

# Chain the Falcon model with the Prompt Template using LangChain
falcon_chain = LLMChain(llm=falcon_llm, prompt=prompt)

def extract_response(text):
    # Use regex to find the content after "Response:"
    match = re.search(r'Response:(.*)', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()
