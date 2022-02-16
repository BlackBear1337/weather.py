from tkinter import *
import requests

root = Tk()


def get_weather():
	city = cityField.get()
	key = '144aad8b326f4a8ede3b1521eeadd6ed'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q': city, 'units': 'metric'}
	result = requests.get(url, params=params)
	weather = result.json()

	info['text'] = f'{str(weather["name"])} \n Температура: {weather["main"]["temp"]} \n По ощущению: {weather["main"]["feels_like"]}  \n Влажность: {weather["main"]["humidity"]} \n Давление: {weather["main"]["pressure"]}'


root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('300x450')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.15)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.25)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()