import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e56b5713ea441ed63ed932aaa6ab53ee'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '24553'

def test_ststus_code():
    response = requests.get(url =f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_part_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert  response_get.json()['data'][0]['name'] == 'fudzi'
    
@pytest.mark.parametrize('key,value', [('name','fudzi'), ('trainer.id',TRAINER_ID),('id','24553')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
    