import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e56b5713ea441ed63ed932aaa6ab53ee'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "nailagabdrakhmanova@yandex.ru",
    "password": "Naila7"
 }

body_confirmation ={
     "trainer_token": TOKEN
}

body_create = {
    
"name": "fudzi",
"photo_id": 2
}

body_change = {
     "pokemon_id": "12331",
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "9"
}


response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/trainers/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/trainers/v2/pokemons' , headers = HEADER, json = body_change)
print(response_create.text)

response_catch = requests.post(url = f'{URL}/trainers/v2/trainers/add_pokeball' , headers = HEADER, json = body_catch)
print(response_catch.text)