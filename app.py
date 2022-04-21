import requests

API_link = 'https://api.telegram.org/bot5364043773:AAG9EaODSj82vPP7_wFMww1DlURVi1JPIvk'
# https://api.telegram.org/bot5364043773:AAG9EaODSj82vPP7_wFMww1DlURVi1JPIvk/sendMessage?chat_id=2092218723&text=Hi

updates = requests.get(API_link + '/getUpdates?offset=-1').json()

print(updates)

message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

sent_message = requests.get(API_link + f'/sendMessage?chat_id={chat_id}&text=Привет! Ты написал текст {text}')