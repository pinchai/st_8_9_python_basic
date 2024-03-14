import requests
import time
from datetime import date
import random

bot_token = "6986363245:AAEKpwak_fBiBX9Pmy08IyxjuH1-_zf0Dqo"
chat_id = "@st89_channel"



html = (
    "<strong>🧾 {inv_no}</strong>\n"
    "<code>សរុប: {grand_total}</code>\n"
    "<code>ប្រាក់ទទួល: {received_amount}</code>\n"
    "<code>ប្រាក់អាប់: {received_amount}</code>\n"
    "<code>📆 {date}</code>\n"
    "<code>=======================</code>\n"
    "<code>1. coca 10x0.25</code>\n"
    "<code>2. abc 1x25</code>\n"
    "<del>3. hanuman 1x25</del>\n"
).format(
    inv_no='INV0001',
    grand_total='6 $',
    received_amount='10$',
    change_amount='10$',
    date=date.today(),
)

html = requests.utils.quote(html)
url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
res = requests.get(url)
print(res.status_code)


