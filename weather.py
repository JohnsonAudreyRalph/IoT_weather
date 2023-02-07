import requests

Api_Key = "1ce7185d18f8940b4093013365c81a21"

final_URL = 'http://api.openweathermap.org/data/2.5/forecast?lat=21.567156&lon=105.825203&appid=c55cad7bdd0e7d82b0b958fdfd7ceeae'

result = requests.get(final_URL)
data = result.json()
# print(data['list'][2]['main'])

NhietDo = data['list'][2]['main']['temp']
DoAm = data['list'][2]['main']['humidity']

NhietDo = round(NhietDo-273)
print('Nhiệt độ hiện tại là: ', NhietDo, 'C')
print('Độ ẩm hiện tại là: ', DoAm, '%')