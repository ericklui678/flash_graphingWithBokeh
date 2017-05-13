from flask import Flask, render_template, request, redirect, session
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
html_text = ""
x = []
y = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    global html_text
    x.append(int(str(request.form['x'])))
    y.append(int(str(request.form['y'])))
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)
    html_text = file_html(p, CDN, 'my plot')

    return redirect('/success')

@app.route('/success')
def success():
    global html_text
    return render_template('lines.html', html_text=html_text)

app.run(debug = True)
