from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def show_datetime():
    data_time_now = datetime.now()
    data_now = data_time_now.date()
    data_format = data_now.strftime('%d. %m. %Y')
    time_now = data_time_now.time()
    time_now_format = time_now.strftime("%Hч %Mмин %Sс")
    return f"<h1 align='center'>Сегодня {data_format}</h1> <h2 align='center'>Московское время {time_now_format}</h2>"


if __name__ == '__main__':
    app.run(debug=True)
