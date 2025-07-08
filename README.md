<h1 align='center'>YouTube Video to Detailed Notes Converter</h1><br>

<h3>Overview</h3>
This application converts YouTube video transcripts into structured, concise notes using Google's Gemini AI. It's designed for students, researchers, and professionals who want to quickly extract key information from educational or instructional videos.<br>

<h3>Features</h3>

- <b>Automatic Transcript Extraction:</b> Fetches transcripts directly from YouTube videos
- <b>AI-Powered Summarization:</b> Uses Gemini Pro AI to generate structured notes
- <b>User-Friendly Interface:</b> Simple Streamlit web interface
- <b>Quick Insights:</b> Provides summaries, main themes, and key takeaways in a standardized format

<h3>Requirements</h3>

- Python 3.7+
- Google Gemini API key
- YouTube video with available captions

<h3>Installation</h3>

1. Clone the repository
2. Install required packages : `pip install -r requirements.txt`
3. Create a `.env` file in your project directory with your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

<h3>Usage</h3>

1. Run the application : `python -m streamlit run project.py --server.port 8888`
2. Enter a YouTube video URL in the input field
3. Press `Enter` to get the video's thumbnail
4. Click "Get Detailed Notes" button
5. View the structured notes generated from the video transcript

<h3>Output Format</h3>

The AI generates notes in this structured format:
1. Summary: A concise overview paragraph.
2. Main Themes: For each major topic:
   - A short paragraph explaining the concept.
   - A bulleted list of key facts, examples, and actionable steps.
3. Key Takeaways: A final bulleted list of the most critical points.

<h3>Limitations</h3>

- Works only with YouTube videos that have transcripts available in the engligh language with code `en`
- Maximum note length is limited to 300-350 words
- Requires an active internet connection

<h3>License</h3>
This project is open-source and available under the MIT License.
