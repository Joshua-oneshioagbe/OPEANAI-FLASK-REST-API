import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
from aicontent import getResponseFromOpenai

load_dotenv()


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["https://kenny-bot.vercel.app", "https://kennybot.up.railway.app"]}})





@app.route('/', methods=['GET'])
def home():
   return jsonify({'message': 'Hello World'})

@app.route('/api/openai', methods=["GET",'POST'])
def openai_api():
    if request.method == 'POST':
        json_data = request.get_json()
        if json_data is not None and 'prompt' in json_data:
            prompt = json_data['prompt']
            response = getResponseFromOpenai(prompt)
            return response
        else:
            return jsonify({'message': 'Invalid request data'})
    else:
        return jsonify({'message': 'my request is not a post'})
       
   





if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
