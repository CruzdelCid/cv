from flask import Flask, render_template,url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml

file_louder = FileSystemLoader('templates')
env = Environment(loader = file_louder)

app = Flask(__name__)
data = yaml.safe_load(open('data.yaml'))

@app.route("/")
@app.route("/inicio")
def inicio():
    template = env.get_template('index.html')
    css = url_for('static', filename='styles.css')
    my_icon = url_for('static', filename='favicon.ico')
    avatar = data['fotografia']
    my_avatar = url_for('static', filename= avatar)
    return template.render(data = data, my_style = css, my_icon = my_icon, my_avatar = my_avatar)

@app.route("/linktree") 
def link(): 
    css2 = url_for('static', filename='estilo.css')
    avatar2 = data['fotografia']
    my_avatar2 = url_for('static', filename= avatar2)
    link = env.get_template("linktree.html")
    return link.render(css2 = css2, my_avatar = my_avatar2)
    
if __name__ == "__main__": 
    app.run(debug = True)
