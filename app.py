import os
from flask import *
import clique
import cliquebk

app = Flask(__name__)

def getfor(formula):
    formula = formula[1:-1]
    clauses = formula.split("),(")
    tuplas = []
    for clause in clauses:
        clause = tuple(map(int,clause.split(",")))
        tuplas.append(clause)
    return tuplas
    
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        clauses = request.form.get('clauses',False,type=str)
        if(not clauses):
            return render_template('index.html',clausula = clauses,maxclique="Escriba una clausula")
        else:
            if request.form['submit'] == 'Fuerza Bruta':
                maxclique = clique.create(getfor(str(clauses)))    
                return render_template('index.html',clausula = clauses,maxclique = maxclique )
            elif request.form['submit'] == 'Optimizado':
                maxclique = cliquebk.findMaxClique(getfor(str(clauses)))
                return render_template('index.html',clausula = clauses,maxclique = maxclique )
            else:
                return render_template('error.html',error='This should never happen')
            
    else:
        return render_template('index.html',maxclique="Escriba una clausula")
	
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8081)),debug=True)
