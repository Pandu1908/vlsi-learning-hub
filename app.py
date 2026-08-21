from flask import Flask

app = Flask(__name__)

@app.route("/")
def quiz():
    return """
    <h1>ECE Quiz</h1>
    <p>What does VLSI stand for?</p>
    <p>A) Very Large Scale Integration</p>
    <p>B) Variable Logic System Input</p>
    <p>C) Virtual Logic System</p>
    """

app.run(debug=True)
