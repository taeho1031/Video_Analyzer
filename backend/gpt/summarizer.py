import os
from openai import OpenAI
from dotenv import load_dotenv

# Retrieve API key from environment variable
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with the API key
client = OpenAI(api_key=api_key)

def summarize_transcript(transcript, detail):
    detail = int(detail)
    token_limit = 100 + int((detail / 100) * (1000 - 100))
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Please summarize the following YouTube video transcript with a detail level of {detail} (where 1 is the most general and 100 is the most detailed) strictly between {token_limit - 20} to {token_limit} words: {transcript}"},
                #{"role": "system", "content": f"say nothing but just print this number: {token_limit-20}"},
    ],
            max_tokens = token_limit
        )
        summary = response.choices[0].message.content
        return summary

    except Exception as e:
        raise e