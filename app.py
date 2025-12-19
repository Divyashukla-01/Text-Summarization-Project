from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

MODEL = "models/gemini-2.5-flash"

def summarize(text):
    prompt = f"""
Summarize the following text in 3–4 sentences:

{text}
"""
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        input_text = request.form["text"]
        result = summarize(input_text)

    return render_template("index.html", output=result)


if __name__ == "__main__":
    app.run(debug=True)
