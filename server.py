from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) # Create a new instance of the Flask class called "app"

@app.route ('/play')  # The "@" decorator associates this route with the function immediately following
def index():
    # returns the result of the render_template method, using play.html
    return render_template("play.html", num=3, color="blue")

@app.route('/play/<int:num>') # for route '/play/num', parameters in the url gets passed as number of boxes
def index_one(num):
    # returns the result of the render_template method, using play.html
    return render_template("play.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>') # for route '/play/num/color', two parameters in the url get passed as number of boxes and color of boxes
def index_two(num,color):
    # returns the result of the render_template method, using play.html
    return render_template("play.html", num=num, color=color)


if __name__ == "__main__": # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5002) # Run the app in debug mode.