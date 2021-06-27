import requests
import wikipedia
def Weather(city):
    api_ = "http://api.openweathermap.org/data/2.5/weather?appid=f94d2c559b95719bad20527b12819a53&q="

    url_ = api_ + 'city'
    json_data = requests.get(url_).json()
    format_add = json_data['main']

    return format_add

    
def wikipid(wiki):
    tokenize = wiki
    find_data = wikipedia.summary(tokenize, sentences=2)
    print(find_data)



def get_news(country):

   url = "https://free-news.p.rapidapi.com/v1/search"
   
   PARAMS = {'q' : country}
   headers = {
       'x-rapidapi-key': "6fb3a4d50bmshe03c380fc38f616p1b6d63jsnb62387c0560a",
       'x-rapidapi-host': "free-news.p.rapidapi.com"
       }
    
   response = requests.request("GET", url, headers = headers, params= PARAMS)
   if response.status_code == 200:
       print('loading...')
       print(response.text)

   elif response.status_code == 404:
       print('An error occurred')

       



