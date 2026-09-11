from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv(override=True)

## Fetch Secrets
google_api_key = os.getenv('GOOGLE_API_KEY')
google_api_url = os.getenv('GEMINI_BASE_URL')
open_api_key = os.getenv('OPENAI_API_KEY')
open_api_url = os.getenv('OPENAI_BASE_URL')
groq_api_url = os.getenv('GROK_BASE_URL')
groq_api_key = os.getenv('GROQ_API_KEY')

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

gemini = OpenAI(api_key=google_api_key, base_url=google_api_url)
openAI = OpenAI(api_key=open_api_key , base_url=open_api_url)
groq = OpenAI(api_key=groq_api_key , base_url=groq_api_url)


MODEL_NAME = ["gemini-3.5-flash","gpt-5.6-luna","openai/gpt-oss-20b"]

def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openAI.chat.completions.create(model=MODEL_NAME[1], messages=messages, tools=tools,reasoning_effort="none")
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openAI.chat.completions.create(model=MODEL_NAME[1], messages=messages, tools=tools, reasoning_effort="none")
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base(),server_name="0.0.0.0",server_port=int(os.environ.get("PORT", 7860)))