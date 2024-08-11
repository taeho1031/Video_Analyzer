Video Analyzer
The Video Analyzer is a web application that allows users to extract transcripts from YouTube videos and generate summaries based on adjustable detail levels. This project is built with a Flask backend and a React frontend.

Table of Contents
Features
Requirements
Installation
Usage
Project Structure
Contributing
License
Features
Extracts transcripts from YouTube videos.
Allows users to adjust the level of detail for the generated summary.
Summarizes the transcript based on the chosen detail level.
Requirements
Python 3.x
Node.js and npm
Flask
React
YouTube Transcript API
OpenAI API key (for summarization)
Installation
Backend Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/video-analyzer.git
cd video-analyzer/backend
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the backend directory and add your OpenAI API key:

bash
Copy code
OPENAI_API_KEY=your_openai_api_key
Frontend Setup
Navigate to the frontend directory:

bash
Copy code
cd ../frontend
Install the required npm packages:

bash
Copy code
npm install
Usage
Running the Backend
Navigate to the backend directory:

bash
Copy code
cd backend
Start the Flask server:

bash
Copy code
flask run
Running the Frontend
Navigate to the frontend directory:

bash
Copy code
cd ../frontend
Start the React development server:

bash
Copy code
npm run start
Open your browser and go to http://localhost:3000 to use the application.

Project Structure
plaintext
Copy code
video-analyzer/
│
├── backend/                # Backend directory (Flask API)
│   ├── app.py              # Main application file
│   ├── requirements.txt    # Python dependencies
│   ├── .env                # Environment variables (not included in Git)
│   └── gpt/
│       └── summarizer.py   # GPT-based summarization logic
│
└── frontend/               # Frontend directory (React app)
    ├── public/             # Static files
    ├── src/                # React source files
    ├── package.json        # npm dependencies
    └── README.md           # Frontend README
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.
