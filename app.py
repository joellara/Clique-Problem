import os

from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')
	
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8081)),debug=True)
