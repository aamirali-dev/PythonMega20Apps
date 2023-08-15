from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv('data_small/stations.txt', skiprows=17)


@app.route('/')
def home():
    return render_template('tutorial.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temprature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {'station': station, 'date': date, 'temprature': temprature}


@app.route('/api/v1/<station>')
def all_data(station):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    return str(df.to_dict(orient='record'))


@app.route('/api/v1/yearly/<station>/<year>')
def yearly(station, year):
    filename = f'data_small/TG_STAID{str(station).zfill(6)}.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df.loc[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return str(result)


@app.route('/api/v1/dictionary/<word>')
def dictionary(word):
    return {'word': word, 'definition': word.upper()}


if __name__ == '__main__':
    app.run(debug=True)
