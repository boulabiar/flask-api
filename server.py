from flask import render_template
import connexion
import config


# Create the application instance
#app = connexion.App(__name__, specification_dir='./') ## generate error because it makes 2 instances, use already defined app as below
app = config.connex_app

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


