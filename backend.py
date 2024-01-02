import requests
import os



os.environ.get('SECRET_KEY')







def get_data(place="tokyo", days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list'][:8*days]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="london", days=2, option="Temperature"))
