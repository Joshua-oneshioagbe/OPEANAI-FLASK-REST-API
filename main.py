import os
from flask import Flask, request, jsonify,make_response
from flask_cors import CORS,cross_origin
from dotenv import load_dotenv
import openai

load_dotenv()


app = Flask(__name__)
CORS(app)


openai.api_key =  os.environ.get('OPEN_AI_API_KEY')


@app.route('/', methods=['GET'])
def home():
   return jsonify({'message': 'Hello World'})

@app.route('/api/openai', methods=['POST'])
@cross_origin()
def openai_api():
    data = request.get_json()
    prompt = data['prompt']
   
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_text = response.choices[0].text.strip()
    response_data = {'response': response_text}
    response_json = jsonify(response_data)
    response = make_response(response_json)
    response.headers['Access-Control-Allow-Origin'] = 'https://kenny-bot.vercel.app'








if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
