from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from gpt.summarizer import summarize_transcript

app = Flask(__name__)
CORS(app)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({'error': 'Missing video ID'}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'ko'])
        entries = "\n".join([entry['text'] for entry in transcript])
        return jsonify({'transcript': entries})
     
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    transcript = data.get('transcript')
    detail = data.get('detailLevel')
    if (not transcript) or (not detail):
        return jsonify({'error': 'Missing transcript or detail'}), 400

    try:
        summary = summarize_transcript(transcript, detail)
        return jsonify({'summary': summary})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
