"""An application to show Variable Rules in Routing"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    """View for the Home page of your website."""
    return "This is your homepage :)"

@app.route("/<your_name>")

def greetings(your_name):
    """View function to greet the user by name."""
    return render_template("test_template.html", name=your_name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)