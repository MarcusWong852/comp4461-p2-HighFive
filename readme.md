# Execution

`rasa train` -> `rasa run actions` -> New terminal `rasa shell`
# Major features
- Informational& Covid Related functions:
  - return time in friendly format
  - can start quarantine, query days left, quarantine progress bar
  - Covid symptoms responses (guide users through what to do if they feel sick)
  - Useful authority links to Covid information
  - linked to HKO APIs to return realtime weather and temperature
  
 - Entertainment:
  - music - soft/pop music videos
  - return joke - jokes[fun/not fun path]
  - workout videos
  - return cat/dog/travel images

- miscellaneous/humanly tweak
  - greet according to time
  - Add some reactions before the weather actually returns
  - use of emojis, 表情符號 Emoticon
  - user feeling tired -> goodnight path
  - nlu fallback -> provide help to use the robot if can't recognise users input
  - robot humorous path


# Connect to Telegram

1. install `ngrok` https://ngrok.com/download
2. run `ngrok http 5005` on the terminal
3. Change `webhook_url` attribute under `credentials.yml` with your own ngrok link
4. run rasa with `rasa run --enable-api --cors "*"` (with `rasa run actions` if needed)
5. find the bot on telegram with the link `t.me/high_five_self_quarantine_bot`
6. chat!
