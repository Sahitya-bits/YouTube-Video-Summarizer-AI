import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """Act as an expert note-taker. Create structured, in-depth notes from the following video transcript. 
Don't use more than 300-350 words.
Use this format:

**1. Summary:** A concise overview paragraph.

**2. Main Themes:** For each major topic:
*   A short paragraph explaining the concept.
*   A bulleted list of key facts, examples, and actionable steps.

**3. Key Takeaways:** A final bulleted list of the most critical points.

---
The transcript is as follows :
"""

def fetch_transcript(url: str) -> str:
    """Gets the transcript of the video on the basis of its youtube id."""
    try:
        video_id = url.split("=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        final_transcript = ""
        for i in transcript:
            final_transcript += (" " + i["text"])
        return final_transcript
    
    except Exception as e:
        raise e

def fetch_response(prompt: str, transcript: str) -> str:
    """Gets the response from the AI as per your prompt and transcript.
    
    Args:
        prompt (str): The input provided to AI model to guide its response.
        transcript (str): The text version of spoken content within a video.
    
    Returns:
        str: response from the AI model.
    """
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt+transcript)
    return response.text

st.title("YouTube Video to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube video link here : ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes"):
    transcript = fetch_transcript(youtube_link)
    if transcript:
        summary = fetch_response(prompt, transcript)
        st.markdown("# Detailed Notes:")
        st.write(summary)