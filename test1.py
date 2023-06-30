import requests
with open('dataset_3378_2.txt', 'r', encoding='utf-8') as file:
    url = file.read().strip()
    r = requests.get(url)
    r = r.text
while 'We' not in r:
    url = 'https://stepik.orgstepic.org/media/attachments/course67/3.6.3/' + r
    r1 = requests.get(url)
    r = r1.text
print(r)