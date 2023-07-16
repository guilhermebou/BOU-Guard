import requests

from bs4 import BeautifulSoup

url = 'https://api.openai.com/v1/chat/completions'
model = 'gpt-3.5-turbo'

#API-KEY
token = 'API KEY'

#URL DO SITE
link = "URL"

request = requests.get(link)
print(request)

soup = BeautifulSoup(request.text, "html.parser")

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'strong', 'span']

input = soup.find_all(tags)
print (input)

format = format(input)
print(format)

def gpt(format):

    prompt = [

        #RETIRE O COMENTARIO DO CONTEXTO QUE ESTA LIGADO A URL MENCIONADA
        #{'role': 'user', 'content': 'identifique e enumere as expressões associadas a homofobia'},
        #{'role': 'user', 'content': 'identifique e enumere as expressões associadas ao racismo'},
        #{'role': 'user', 'content': 'identifique e enumere as expressões associadas ao machismo'},
        {'role': 'user', 'content': format}
    ]

    response = requests.post(
        url,
        headers={'Authorization': f'Bearer {token}'},
        json={
            'model': model,
            'messages': prompt
        }
    )

    data = response.json()
    for choice in data['choices']:
        reply = choice['message']['content']
        print(reply)

output = gpt(format)
print (output)
