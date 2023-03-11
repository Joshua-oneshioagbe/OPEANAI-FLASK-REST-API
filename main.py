import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
from aicontent import getResponseFromOpenai

load_dotenv()


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["https://kenny-bot.vercel.app", "https://kennybot.up.railway.app"]}})


openai.api_key =  os.environ.get('OPEN_AI_API_KEY')


@app.route('/', methods=['GET'])
def home():
   return jsonify({'message': 'Hello World'})

@app.route('/api/openai', methods=['POST'])
def openai_api():
      if request.method == 'POST':
        data = request.get_json()
        prompt = data["prompt"]
        response=getResponseFromOpenai(prompt)
        return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
