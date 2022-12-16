from flask import Flask, render_template, request, jsonify
import conLayer
from tabulate import tabulate


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


"""
Obtains the data from query1 to plot a chart representing the data of Query1
"""
# GET data for query 1


@app.route('/chart1')
def chart1():
    header = "Query 1"
    description = "Shows the top genres of movies for a month (all-time)"
    return render_template('chart1data.html', options=options, header=header, description=description)


"""
Run Query1, allows the user to select the a month to obtain the top 5 genres of movies by Box office collection
"""
# query 1
# render query 1


@app.route('/chart1', methods=['POST'])
def chart1_post():

    genre_bo = {}
    genre_bo["Genre"] = []
    genre_bo["Box Office Collection"] = []
    month = request.form['month']
    data = conLayer.query1(month)

    for i in data:
        genre_bo["Box Office Collection"].append(int(i[1]))
        genre_str = i[0]
        gen_list = list(genre_str.split(","))
        genre_bo["Genre"].append(gen_list[0])

    df = pd.DataFrame(genre_bo, columns=[
                      "Genre", "Box Office Collection"])

    fig = px.bar(df, x='Genre', y='Box Office Collection',
                 color='Genre', barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Query 1"
    description = "Shows the top genres of movies for the month of " + \
        str(month) + " (all time)"

    return render_template('chart1.html', options=options, month=month, data=data, header=header, description=description, graphJSON=graphJSON)


# GET data for query 2
@app.route('/chart2')
def chart2():
    header = "Query 2"
    description = "Shows the top 3 Box Office Collection between 2 years"
    return render_template('chart2data.html', options=options, header=header, description=description)


# render query2
@app.route('/chart2', methods=['POST'])
def chart2_post():
    movie_bo = {}
    from_year = request.form['from_year']
    to_year = request.form['to_year']

    # exectues query2
    data = conLayer.query2(from_year, to_year)
    for i in data:
        print(i)
        movie_str = i[0]
        bo_str = i[2]

       # movie:box office map
        movie_bo[movie_str] = bo_str
    df = pd.DataFrame(list(movie_bo.items()), columns=[
                      "Movie name", "Box Office"])
    df['Box Office'] = df['Box Office'].astype(str).astype(float)
    df_sorted = df.sort_values(by=['Box Office'], ascending=False)
    fig = px.bar(df_sorted, x='Movie name', y='Box Office', color='Movie name',
                 barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Query 2"
    description = "Shows the top 3 Box Office Collection between the year {} and {}".format(
        from_year, to_year)
    return render_template('chart2.html', options=options, from_year=from_year, to_year=to_year, data=data, header=header, description=description, graphJSON=graphJSON)


# GET data for query 3
@app.route('/chart3')
def chart3():
    header = "Query 3"
    description = "Shows the top 3 genres that a director is famous for making movies in"
    return render_template('chart3data.html', options=options, header=header, description=description)


# render query 3
@app.route('/chart3', methods=['POST'])
def chart3_post():
    dir_bo = {}
    dir_bo["Movie"] = []
    dir_bo["Genre"] = []
    director_name = request.form['director_name']
    data = conLayer.query3(director_name)
    for i in data:
        movie_str = i[0]
        dir_bo["Movie"].append(movie_str)
        bo_str = i[1]
        bo_list = list(bo_str.split(","))
        dir_bo["Genre"].append(bo_list[0])

    df = pd.DataFrame(dir_bo, columns=[
                      "Movie", "Genre"])
    print(df)
    result = df.to_html()

    header = "Query 3"
    description = "Shows the top 3 genres that {} is famous for making movies in".format(
        director_name)

    return render_template('chart3.html', options=options, dir_name=director_name, data=data, header=header, description=description, result=result)


# GET data for query 4
@app.route('/chart4')
def chart4():
    header = "Query 4"
    description = "Shows the average Rating of a Director's Movies"
    return render_template('chart3data.html', options=options, header=header, description=description)


# render query 4
@app.route('/chart4', methods=['POST'])
def chart4_post():
    dir_rating = {}
    director_name = request.form['director_name']
    dir_rating["Director Name"] = director_name
    dir_rating["Avg Rating"] = 0
    data = conLayer.query4(director_name)
    result = 0
    for i in data:
        result = i[0]

        dir_rating["Avg Rating"] = result
    df = pd.DataFrame(list(dir_rating.items()))

    print(df)
    result = df.to_html()

    header = "Query 4"
    description = "Shows the average Rating of " + director_name + "'s Movies"

    return render_template('chart4.html', options=options, dir_name=director_name, data=data, header=header, description=description, result=result)


# GET data for query 5
@app.route('/chart5')
def chart5():
    header = "Query 5"
    description = "Shows the number of movies belonging to a genre between 2 time ranges"
    return render_template('chart5data.html', options=options, header=header, description=description)


# render query 5
@app.route('/chart5', methods=['POST'])
def chart5_post():
    count = {}
    from_year = request.form['from_year']
    to_year = request.form['to_year']
    genre = request.form['genre'] + '%'
    gen_copy = request.form['genre']
    data = conLayer.query5(from_year, to_year, genre)
    count["Time-range"] = str(from_year)+"-"+str(to_year)
    count["genre"] = gen_copy
    count["count"] = 0
    for i in data:
        count["count"] = i[0]

    df = pd.DataFrame(list(count.items()))
    result = df.to_html()

    header = "Query 5"
    description = "Shows the number of movies belonging to the genre {} between 2 time ranges {}-{}.".format(
        gen_copy, from_year, to_year)
    return render_template('chart5.html', options=options, from_year=from_year, to_year=to_year, genre=genre, data=data, header=header, description=description, result=result)


if __name__ == "__main__":
    app.run(debug=True)
