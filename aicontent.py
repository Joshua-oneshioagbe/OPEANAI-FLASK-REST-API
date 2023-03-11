import os,openai,config

openai.api_key = config.OPENAI_API_KEY

def getResponseFromOpenai(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Generate a detailed product description of the prompt: {prompt}",
      temperature=0.49,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    
    if "choices" in response:
      if len(response["choices"]) > 0:
        if "text" in response["choices"][0]:
          awnser= response["choices"][0]["text"]
        
        else:
           awnser= "No awnser from the Api"
      else:
         awnser="No awnser from the Api response from the api"
    else:
      awnser="Opps no choices in the response"
    
    return awnser
getResponseFromOpenai("who won the last ballon dor")

