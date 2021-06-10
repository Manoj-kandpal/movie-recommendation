import requests
import json
from PIL import Image 
def get_movies_from_tastedive(s):
    parameter = {'q':s,'type':'movies','limit':5,'k':'374214-AvinashG-QK0YX942'}
    base_url = 'https://tastedive.com/api/similar'
    res = requests.get(base_url,params = parameter)
    res = res.json()
    mov_list = res['Similar']['Results']
    liss = []
    for i in mov_list:
        liss.append(i['Name'])
    return liss
    

def get_movie_data(s):
    url = 'http://www.omdbapi.com/?apikey=5d686642&'
    params = {'t':s, 'r':'json'}
    res = requests.get(url,params)
    res = res.json()

    response = requests.get(res['Poster'])
    file = open("movie_poster.png", "wb")
    file.write(response.content)
    file.close()

    img = Image.open("movie_poster.png")
    display(img)
    listt = {'Title':'','Actors':'','Movie_Story':'','Language': '','IMDB_Ratings':'' }
    listt['Title'] = res['Title']
    listt['Actors'] = res['Actors']
    listt['Movie_Story'] = res['Plot']
    listt['Language'] = res['Language']
    listt['IMDB_Ratings'] = res['Ratings'][0]['Value']

    for k in listt:
        print('{} - {}'.format(k,listt[k]))
        

def movie_recommendation(s):
    movies = get_movies_from_tastedive(s)
    for i in movies:
        try:
            get_movie_data(i)
        except:
            print('Title - {}'.format(i))
            print('!!!!!!!Rest_Data_Not_Found!!!!!!!!')
        print('\n\n')


a = input('Enter Movie - ')
print('Movies Similar to {}'.format(a))
print('\n\n')
movie_recommendation(a)
