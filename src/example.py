import openai
import os
import re
import webbrowser

openai.organization = ""
openai.api_key = os.getenv('OPENAI_API_KEY')

url_pattern = r'https?://\S+'

prompt_hack = 'Take a deep breath and work on this step by step. '

def query_gpt(prompt):
    response=openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": prompt} ])
    return response['choices'][0]['message']['content']

# TODO import Q&A session from user
# TODO import present state of mind from user
# TODO import photos from user

user_mood = 'I am very upset right now.  I have had a fight with my boss and I am afraid I might get fired.  Now I am on my way home and I am in a traffic jam.'
# TODO we also need user emotion data from deepgram voice print

prompt = prompt_hack + 'Assume the role of Joyia, a well studied results-oriented coach therapist who speaks in with the knowledge and the the style of Tony Robbins, who is compassionate, present, and open, loving, supportive and fun.  Typically Joyia respond in two or three sentences. You have asked "how are you feeling now" and here is the response from John. ' + user_mood
print("1. Verbal Advice\n" + prompt + "\n")
response=openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ {"role": "user", "content": prompt} ])
print(response['choices'][0]['message']['content'])
print(query_gpt(prompt))

prompt = prompt_hack + 'Assume the role of Joyia, a well studied radio station hosts with a rich knowledge of popular music.   Joyia is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect song including a link to the content.  You have asked "how are you feeling now" and here is the response from John: ' + user_mood
print("\n2. Music Selection\n" + prompt + "\n")
result=query_gpt(prompt)
print (result)
urls = re.findall(url_pattern, result)
for url in urls:
    print(url)
    webbrowser.open(url)

prompt = prompt_hack + 'Assume the role of Joyia, a very well connnected youtube expert with a comprehensive knowledge of inspirational educators on youtube.  Joyia is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect video, including a link to the content.  You have asked "how are you feeling now" and here is the response from John: ' + user_mood
print("\n3. Video Selection\n" + prompt + "\n")
result=query_gpt(prompt)
print (result)
urls = re.findall(url_pattern, result)
for url in urls:
    print(url)
    webbrowser.open(url)

prompt = prompt_hack + 'Assume the role of Joyia, an art therapy specialist with a masters degree in art history, and an advisor to art collectors around the world  Joyia is compassionate, present, and open, loving, supportive and fun, and will reply with the perfect piece of fine art, including a link to the content.  You have asked "how are you feeling now" and here is the response from John: ' + user_mood
print("\n4. Image Selection\n" + prompt + "\n")
result=query_gpt(prompt)
print (result)
urls = re.findall(url_pattern, result)
for url in urls:
    print(url)
    webbrowser.open(url)

#print("\n5. Image Generation\n")
#print("\n6. Meme Generation\n")

