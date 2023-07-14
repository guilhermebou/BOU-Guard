import requests
from bs4 import BeautifulSoup
url = 'https://api.openai.com/v1/chat/completions'
model = 'gpt-3.5-turbo'
token = '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'

link = "https://sedh.es.gov.br/Not%C3%ADcia/novembro-negro-conheca-algumas-expressoes-racistas-e-seus-significados"

requisicao = requests.get(link)
print(requisicao)
#print(requisicao.text)


soup = BeautifulSoup(requisicao.text, "html.parser")

#org
#print(link.prettify())

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'strong', 'span']

input = soup.find_all('strong')
print (input)
#.replace('\n', '')

format = format(input)

def gpt(format):

    prompt = [
        {'role': 'user', 'content': 'identifique e enumere as expressões associadas ao racismo'},
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
