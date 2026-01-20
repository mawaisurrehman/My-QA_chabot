import os
import gradio as gr
from groq import Groq, GroqError

# Get API key from environment variable
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("⚠️ Please set the GROQ_API_KEY environment variable!")

# Initialize Groq client
client = Groq(api_key=API_KEY)

def groq_response(prompt):
    try:
        if not prompt.strip():
            return "⚠️ Please enter a valid prompt."

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Supported Groq model
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message.content

    except GroqError as e:
        return f"⚠️ Groq API Error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"

# Gradio interface
iface = gr.Interface(
    fn=groq_response,
    inputs=gr.Textbox(lines=5, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Groq AI Response"),
    title="Groq AI Assistant",
    description="Ask anything using a supported Groq model. API key is kept secret."
)

iface.launch()
