import requests

def create_short_link(api_key,  long_url,
                    short_id=None, 
                    domain=None, 
                    ):
    """Creates a short link using the t.ly API
    """

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    endpoint = "https://t.ly/api/v1/link"

    api_token = api_key

    url = f"{endpoint}/shorten"
    payload = {
        "long_url": long_url,
    }
    if short_id:
        payload['short_id'] = short_id
    if domain:
        payload['domain'] = domain
    params = {
        "api_token": api_token
    }

    response = requests.request('POST', url, headers=headers, json=payload, params=params)
    if response.status_code != 200:
        raise Exception(response.text)
    
    return response.json()['short_url']