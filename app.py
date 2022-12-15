from flask import Flask, render_template
import conLayer

import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

options = [
    {'link': '/chart1', 'label': 'Query 1'},
    {'link': '/chart1', 'label': 'Query 2'},
    {'link': '/chart1', 'label': 'Query 3'},
    {'link': '/chart1', 'label': 'Query 4'},
    {'link': '/chart1', 'label': 'Query 5'},

]


@app.route("/")
def index():
    return render_template('index.html', options=options)


@app.route("/db")
def db():

    # need to handle the data here, making the assumption that
    #[('Action,Adventure,Drama', '99644'), ('Comedy,Drama', '98906'), ('Biography,Comedy,Crime', '987857'), ('Drama', '98587'), ('Comedy', '98587')]
    # first category is the genre of movie, we need to get Action and the revenue(last element)
    data = conLayer.query1()
    return data


@app.route("/dash")
def dash():
    return render_template("notdash2.html")


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
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description, options=options)


if __name__ == "__main__":
    app.run(debug=True)
