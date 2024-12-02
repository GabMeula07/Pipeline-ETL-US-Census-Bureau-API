import requests

url_base = 'https://api.worldbank.org/v2'
list_json = []

def extract_data_to_endpoint(endpoint: str):
    response = requests.get(f'{url_base}{endpoint}&page=1')
    json_response = response.json()

    iterate_response_json(response_json_list=json_response[1])
    iterate_response_pages(pages=json_response[0]['pages'], endpoint=endpoint)
    print(list_json)

def iterate_response_pages(pages: int, endpoint: str):
    for page_number in range(2, pages):
        response = requests.get(f'{url_base}{endpoint}&page={page_number}')
        json_response = response.json()
        iterate_response_json(response_json_list=json_response[1])

def iterate_response_json(response_json_list: list)-> None:
    for _dict in response_json_list:
        list_json.append(_dict)
        

extract_data_to_endpoint('/country/BR/indicator/NY.GDP.MKTP.CD?format=json')