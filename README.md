# My-QA_chabot

A small question-answering chatbot using the Groq API and a Gradio web UI.

This project provides a lightweight UI for interacting with a Groq chat model. The main entrypoint is `app.py`, which launches a Gradio interface for sending prompts to the Groq API and displaying responses.

## Key details found in app.py
- Uses the official Groq client: `groq`
- Uses Gradio for the UI: `gradio`
- Requires an environment variable: `GROQ_API_KEY`
- Calls model: `llama-3.1-8b-instant`
- Basic error handling for Groq errors and empty prompts
- Launches a Gradio interface with default settings (`iface.launch()`)

## Requirements
- Python 3.8+ (recommended)
- A valid Groq API key

Install Python dependencies:
```bash
pip install -r requirements.txt
```

requirements.txt is provided in the repository (or see the example file included with this README).

## Configuration

The app expects the Groq API key to be available as an environment variable:

- GROQ_API_KEY — your Groq API key (required)

Example (macOS / Linux):
```bash
export GROQ_API_KEY="sk-..."
python app.py
```

Example (Windows CMD):
```cmd
set GROQ_API_KEY="sk-..."
python app.py
```

You can also use a `.env` file locally with a tool such as `python-dotenv` if you prefer (not required by the current app code).

## Running the app

Run the application with:

```bash
python app.py
```

When you run it, Gradio will start and print a local URL (for example http://127.0.0.1:7860) to access the web UI. The app uses Gradio's default launch options. If you need to expose the interface publicly, modify `app.py` to use `iface.launch(share=True)`.

## Usage

- Open the Gradio URL in your browser.
- Type your question in the textbox and press the button or Enter.
- The response will appear in the output textbox.

Notes from app.py:
- Empty prompts return an immediate warning message: "⚠️ Please enter a valid prompt."
- Groq API errors are returned with a prefixed message: "⚠️ Groq API Error: ..."
- Unexpected exceptions are returned with a prefixed message: "⚠️ Unexpected Error: ..."

## Customization

You can change the model and generation parameters in `app.py`:
- model: currently "llama-3.1-8b-instant"
- temperature: currently `0.7`
- max_tokens: currently `512`

To change the Gradio behavior (port, host, sharing, etc.), modify the `iface.launch()` call, for example:

```python
iface.launch(server_name="0.0.0.0", server_port=8000, share=False)
```

## Security

- Keep your `GROQ_API_KEY` secret. Do NOT commit it to the repository.
- Use environment variables or a secrets manager for production deployment.
- When using `share=True` in Gradio, be aware the interface becomes publicly accessible via a temporary Gradio-hosted URL.

## Development & Testing

- Use a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate   # macOS / Linux
  .\venv\Scripts\activate    # Windows
  pip install -r requirements.txt
  ```

- Start the app:
  ```bash
  export GROQ_API_KEY="sk-..."
  python app.py
  ```

Add tests and CI as needed.

## Project structure (suggested)
- app.py                # main application (already present)
- requirements.txt      # Python dependencies (provided)
- README.md             # this file

## Troubleshooting

- If you see ValueError about `GROQ_API_KEY`, ensure the env var is set and accessible to the process that runs Python.
- If model responses are empty or truncated, consider increasing `max_tokens`.
- If the Groq client throws errors, check your API key, rate limits, and network connectivity.


## ChatBot URL
https://huggingface.co/spaces/awaisjutt23/my-qa-chatbot

## License & Contributing

Contributions are welcome — open issues or pull requests with improvements and tests.
