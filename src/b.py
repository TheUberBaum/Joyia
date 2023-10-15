from elevenlabslib import *

user = ElevenLabsUser("API_KEY")
voice = user.get_voices_by_name("Rachel")[0]  # This is a list because multiple voices can have the same name

voice.play_preview(playInBackground=False)

voice.generate_play_audio_v2("Test.", playbackOptions=PlaybackOptions(runInBackground=False))

for historyItem in user.get_history_items_paginated():
    if historyItem.text == "Test.":
        # The first items are the newest, so we can stop as soon as we find one.
        historyItem.delete()
        break
