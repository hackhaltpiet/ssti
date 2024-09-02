from flask import Flask, request, render_template_string
from jinja2 import Environment, BaseLoader

app = Flask(__name__)

# Initialize a Jinja2 environment with an empty loader
Jinja2 = Environment(loader=BaseLoader())

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                background-color: #007bff;
                color: white;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Search</h1>
            <form action="/page" method="get">
                <input type="text" name="name" placeholder="Enter your name" required>
                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/page')
def page():
    name = request.values.get('name', 'World')
    
    # Demonstrate SSTI vulnerability
    # Create a template from the user input directly (vulnerable)
    template_string = 'Hello ' + name + '!'
    template = Jinja2.from_string(template_string)
    output = template.render()

    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
