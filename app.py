import requests






get_weather = input("Enter a city: ")

url = f"https://open-weather13.p.rapidapi.com/city/{get_weather}"

headers = {
	"X-RapidAPI-Key": "fa30f2837cmshab533ead272d05ap1c57bcjsn8d181ef68fbf", # use your own key
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
weather = response.json()
if main in weather:
	temperature = weather['main'].get("temp")
	feels_like = weather['main'].get("feels_like")
	print(f"temperature in {get_weather}  currently : {temperature} feels like {feels_like}")
else:
	print("please enter valid city")

