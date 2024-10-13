# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

# Website Scrapper
class Website:
    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

# Load environment variables in .env
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

## A system prompt: that tells them what task they are performing and what tone they should use
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

## A user prompt: the conversation starter that they should reply to
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "The contents of this website is as follows; \
        please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# Messages to OpenAI
# The API from OpenAI expects to receive messages in a particular structure.
# Many of the other APIs share this structure:
"""
[
    {"role": "system", "content": "system message goes here"},
    {"role": "user", "content": "user message goes here"}
]
"""
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

WEB_URL = "https://www.morningstar.ca/ca/"
summary = summarize(WEB_URL)
print(summary)
