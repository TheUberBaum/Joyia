import openai
import os

openai.organization = ""
openai.api_key = os.getenv('OPENAI_API_KEY')

# TODO import Q&A session from Joyia user
# TODO import present state of mind from Joyia user

print("1. Verbal Advice\n")
prompt = 'Take a deep breath and work on this step by step. Assume the role of Joyia, a well studied results-oriented coach therapist who speaks in with the knowledge and the the style of Tony Robbins, who is compassionate, present, and open, loving, supportive and fun.  Typically you respond in two or three sentences. You have asked "how are you feeling now" and here is the response from John: "Joyia, I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
print(prompt + "\n")

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )

print(response['choices'][0]['message']['content'])
print("\n2. Music Selection\n")

prompt = 'Take a deep breath and work on this step by step. Assume the role of James, a well studied radio station hosts with a rich knowledge of popular music.   James is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect song including a link to the content.  You have asked "how are you feeling now" and here is the response from John: "James, I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
print(prompt + "\n")
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )
print(response['choices'][0]['message']['content'])

print("\n3. Video Selection\n")

prompt = 'Take a deep breath and work on this step by step. Assume the role of Martha, a very well connnected youtube expert with a comprehensive knowledge of inspirational educators on youtube.  Martha is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect video.  You have asked "how are you feeling now" and here is the response from John: "Martha, I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
print(prompt + "\n")
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )
print(response['choices'][0]['message']['content'])

print("\n4. Image Selection\n")

prompt = 'Take a deep breath and work on this step by step. Assume the role of Roxanne, an art therapy specialist with a masters degree in art history, and an advisor to art collectors around the world  Roxanne is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect piece of fine art.  You have asked "how are you feeling now" and here is the response from John: "Martha, I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
print(prompt + "\n")
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
  )

print(response['choices'][0]['message']['content'])
print("\n5. Image Generation\n")

print("\n6. Meme Generation\n")

