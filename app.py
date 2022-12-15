from flask import Flask, render_template, request, jsonify
import conLayer

import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

options = [
    {'link': '', 'label': ''},
    {'link': '/', 'label': 'Home'},
    {'link': '/chart1', 'label': 'Query 1'},
    {'link': '/chart2', 'label': 'Query 2'},
    {'link': '/chart3', 'label': 'Query 3'},
    {'link': '/chart4', 'label': 'Query 4'},
    {'link': '/chart5', 'label': 'Query 5'},

]


@app.route("/")
def index():
    return render_template('index.html', options=options)


@app.route("/db")
def db():
    month = request.form['month']
    # need to handle the data here, making the assumption that
    # [('Action,Adventure,Drama', '99644'), ('Comedy,Drama', '98906'), ('Biography,Comedy,Crime', '987857'), ('Drama', '98587'), ('Comedy', '98587')]
    # first category is the genre of movie, we need to get Action and the revenue(last element)
    data = conLayer.query1(month)
    return data


# query 1
@app.route('/chart1')
def chart1():
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('chart1.html', graphJSON=graphJSON, header=header, description=description, options=options)


# GET data for query 2
@app.route('/chart2')
def chart2():
    return render_template('chart2data.html', options=options)


# render query2
@app.route('/chart2', methods=['POST'])
def chart2_post():
    from_year = request.form['from_year']
    to_year = request.form['to_year']
    data = conLayer.query2(from_year, to_year)
    header = "Query 2"
    description = "Description."
    return render_template('chart2.html', options=options, from_year=from_year, to_year=to_year, data=data, header=header, description=description)


# GET data for query 3
@app.route('/chart3')
def chart3():
    return render_template('chart3data.html', options=options)


# render query 3
@app.route('/chart3', methods=['POST'])
def chart3_post():
    director_name = request.form['director_name']
    data = conLayer.query3(director_name)
    header = "Query 3"
    description = "Description."
    return render_template('chart3.html', options=options, dir_name=director_name, data=data, header=header, description=description)


# GET data for query 4
@app.route('/chart4')
def chart4():
    return render_template('chart3data.html', options=options)


# render query 4
@app.route('/chart4', methods=['POST'])
def chart4_post():
    director_name = request.form['director_name']
    data = conLayer.query4(director_name)
    header = "Query 4"
    description = "Description."
    return render_template('chart3.html', options=options, dir_name=director_name, data=data, header=header, description=description)


# GET data for query 5
@app.route('/chart5')
def chart5():
    return render_template('chart5data.html', options=options)


# render query 5
@app.route('/chart5', methods=['POST'])
def chart5_post():
    from_year = request.form['from_year']
    to_year = request.form['to_year']
    genre = request.form['genre'] + '%'
    data = conLayer.query5(from_year, to_year, genre)
    header = "Query 5"
    description = "Description."
    return render_template('chart5.html', options=options, from_year=from_year, to_year=to_year, genre=genre, data=data, header=header, description=description)




if __name__ == "__main__":
    app.run(debug=True)
