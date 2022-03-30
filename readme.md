# Execution

`rasa train` -> `rasa run actions` -> New terminal `rasa shell`

- Put down feature/things to look for, so easier to make videos
- miscellaneous/make it more humanly

  - greet according to time
  - Add some reactions before the weather actually returns
  - emojis, 表情符號 Emoticon
  - user feeling tired -> goodnight
  - nlu fallback -> provide help if can't recognise users input
  - robot humorous path

- Entertain - actual functions to display:

  - music - soft/pop
  - return joke - jokes[fun/not fun]
  - workout videos
  - return cat/dog/travel images

- Informational - actual functions to display:
  - return time in friendly format
  - start quarantine, query days left, quarantine progress

# Connect to Telegram

1. install `ngrok` https://ngrok.com/download
2. run `ngrok http 5005` on the terminal
3. Change `webhook_url` attribute under `credentials.yml` with your own ngrok link
4. run rasa with `rasa run --enable-api --cors "*"` (with `rasa run actions` if needed)
5. find the bot on telegram with the link `t.me/high_five_self_quarantine_bot`
6. chat!
