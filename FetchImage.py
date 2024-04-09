import requests


def fetch_image(query, api_key):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    headers = {"Authorization": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    else:
        data = response.json()

        # fetch image result validation check
        if 'photos' in data and len(data['photos']) > 0:
            return data['photos'][0]['src']['large']
        else:
            return None  # replace with your default image URL or error message


def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
