import requests
import cherrypy

Api_Key = "1ce7185d18f8940b4093013365c81a21"

final_URL = 'http://api.openweathermap.org/data/2.5/forecast?lat=21.567156&lon=105.825203&appid=c55cad7bdd0e7d82b0b958fdfd7ceeae'

result = requests.get(final_URL)
data = result.json()

NhietDo = data['list'][2]['main']['temp']
DoAm = data['list'][2]['main']['humidity']
City = data['city']['name']


NhietDo = round(NhietDo-273)
# print('Nhiệt độ hiện tại là: ', NhietDo, 'C')
# print('Độ ẩm hiện tại là: ', DoAm, '%')
# print('Khu vực: ', City)


class WeatherDashboardHTML(object):
    @cherrypy.expose
    def index(self):
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Weather</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
                <style>
                    .element-box {
                        border-radius: 10px;
                        border: 2px solid #C8C8C8;
                        padding: 20px;
                    }
                    .card {
                        width: 600px;
                    }
                    .col {
                        margin: 10px;
                    }
                </style>
            </head>
            <body>
                <div class="container center">
                    <br>
                    <div class="card">
                        <div class="card-header">
                            <h2>Chương trình dự báo thời tiết tại khu vực """+ str(City) +"""</h2>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col element-box">
                                    <h3>Nhiệt độ hiện tại là: """+ str(NhietDo) +"""</h3>
                                </div>
                                <div class="col element-box">
                                    <h3>Độ ẩm hiện tại là: """+ str(DoAm) +"""</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
            </body>
            </html>
        """

if __name__=="__main__":
    cherrypy.quickstart(WeatherDashboardHTML())