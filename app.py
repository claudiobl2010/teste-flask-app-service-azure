from flask import Flask
app = Flask(__name__)

app.template_folder = '%s/web/templates' % app.root_path
app.static_folder = '%s/web/static' % app.root_path

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
