from tkinter import *
import requests
import wikipediaapi

def get_weather():
    city = city_field.get()
    key = '5695844ccfab85425da04d74eb22d491'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{weather["name"]}: Ветер {weather["wind"]["speed"]} м/с'

root = Tk()
root['bg'] = '#ADD8E6' 
root.title('Ветрянное приложение')
root.geometry('500x350')
root.resizable(width=False, height=False)


city_field = Entry(root, bg='white', font=30)
city_field.place(x=155, y=100)

btn = Button(root, text='Каков ветерюга нынче', command=get_weather)
btn.place(x=180, y=125)

Label_text = Label(root, text='Ветер в городе', font=40)
Label_text.place(x=185, y=160)

info = Label(root, bg='#ADD8E6', font=("Helvetica", "16", "bold"))
info.place(x=150, y=190)
root.mainloop()

#13.2-------------------------------------------



def get_pokemon_info():
    pokemon_name = pokemon_field.get()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    result = requests.get(url)
    pokemon_data = result.json()


    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    types = [type_info['type']['name'] for type_info in pokemon_data['types']]
    weight = pokemon_data['weight']
    height = pokemon_data['height']
    info['text'] = f"Характеристики покемона {pokemon_name}:\nТипы: {', '.join(types)}\nСпособности: {', '.join(abilities)}\nВес: {weight/10} кг\nРост: {height/10} см"

root = Tk()
root['bg'] = '#FFFF00'
root.title('Информация о покемонах')
root.geometry('500x350')
root.resizable(width=False, height=False)

pokemon_field = Entry(root, bg='white', font=30)
pokemon_field.place(x=155, y=100)

btn = Button(root, text='Узнать про покемона', command=get_pokemon_info)
btn.place(x=180, y=125)

Label_text = Label(root, text='Информация о покемоне', font=40)
Label_text.place(x=155, y=160)

info = Label(root, bg='#FFFF00', font=("Helvetica", "16"))
info.place(x=80, y=190)


root.mainloop()