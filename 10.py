from flask import*
app = Flask(__name__)

@app.route('/theform')
def form():
    return '''

      
   
if __name__ == '__main__':
   app.run(debug = True)