'''
import requests

url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/%7Btitle%7D"

querystring = {"exact":"true"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "d568dffe17msh4d2e5541e5c4748p16acefjsnea109f2fc88b",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
'''

import requests

url = "https://openai80.p.rapidapi.com/chat/completions"

question = input("Pregunta: ")

payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": question
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d568dffe17msh4d2e5541e5c4748p16acefjsnea109f2fc88b",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()["choices"][0]["message"]["content"]) 


