import os, random
from flask import Flask
app = Flask(__name__)

grades = ['A', 'B', 'C', 'D']
matieres = [
    'B1 - Anglais',
    'B1 - C - Prog Elem',
    'B1 - Mathematiques',
    'B1 - Igraph',
    'B1 - Expression Ecrite',
    'B1 - Systeme Unix'
]

@app.route("/")
def hello():
    s = 'Tes grades:\n'
    for matiere in matieres:
        grade = random.choice(grades)
        s += '%s : %s\n' % (matiere, grade)
    return s

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
