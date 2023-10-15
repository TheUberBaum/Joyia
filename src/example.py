import openai
import os

openai.organization = ""
openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai.api_key)

print("1. Verbal Advice")
print("")
prompt = 'Take a deep breath and work on this step by step. Assume the role of Joyia, a well studied results-oriented coach therapist who speaks in with the knowledge and the the style of Tony Robbins, who is compassionate, present, and open, loving, supportive and fun.  Typically you respond in two or three sentences. You have asked "how are you feeling now" and here is the response from John: "Joyia, I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
print(prompt)

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )

print("")
print(response['choices'][0]['message']['content'])

print("")
print("2. Music Selection")
print("3. Video Selection")
print("4. Image Selection")
print("5. Image Generation")
print("6. Meme Generation")

