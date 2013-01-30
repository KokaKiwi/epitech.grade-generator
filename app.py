import os, random
from flask import Flask
app = Flask(__name__)

grades = ['A', 'B', 'C', 'D']

@app.route("/")
def hello():
    grade = random.choice(grades)
    return 'Ton grade: %s' % (grade)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
