import requests
import time
import random

bot_token = "6986363245:AAEKpwak_fBiBX9Pmy08IyxjuH1-_zf0Dqo"
chat_id = "@st89_channel"
text = "sender"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"

for item in range(10):
    duration = random.randint(1, 5) # 1, 2, 3,4, 5
    time.sleep(duration)
    res = requests.get(url)
    print(res.status_code)


