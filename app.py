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


@app.route('/chart10')
def chart10():
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


"""
Obtains the data from query1 to plot a chart representing the data of Query1
"""
# GET data for query 1


@app.route('/chart1')
def chart1():
    return render_template('chart1data.html', options=options)


"""
Run Query1, allows the user to select the a month to obtain the top 5 genres of movies by Box office collection
"""
# query 1
# render query 1


@app.route('/chart1', methods=['POST'])
def chart1_post():
    genre_bo={}
    month = request.form['month']
    data = conLayer.query1(month)
    for i in data:
        gen_str=i[0]
        bo_str=i[1]
        
        #mainGenre
        mainGenreList=list(gen_str.split(","))
        mainGenre=mainGenreList[0]
        genre_bo[mainGenre]=bo_str
    df=pd.DataFrame(list(genre_bo.items()))
    fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Query 1"
    description = "Shows the top 3 genres of movies in the chosen month"
    return render_template('chart1.html', options=options, month=month, data=data, header=header, description=description)


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
    description = "Show the top 3 Box Office Collection in the year range"
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
    description = "Shows the top 3 genres the director is famous for making movies in"
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
    description = "Shows the avg Rating of the Directors Movies"
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
    description = "Shows the number of movies beloging to a genre between 2 time ranges."
    return render_template('chart5.html', options=options, from_year=from_year, to_year=to_year, genre=genre, data=data, header=header, description=description)


if __name__ == "__main__":
    app.run(debug=True)
