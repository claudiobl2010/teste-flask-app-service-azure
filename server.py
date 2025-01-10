from flask import Flask, render_template

app = Flask(__name__)

app.template_folder = '%s/web/templates' % app.root_path
app.static_folder = '%s/web/static' % app.root_path

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
