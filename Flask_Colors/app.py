from flask import Flask, jsonify
import GetMeMyColor

app = Flask(__name__)

colorz = GetMeMyColor

@app.route('/')
def welcome():
    return 'This is the main page'

@app.route('/colors/<color>')
def getColors(color):
    test = ""
    test = colorz.fetchColors(color)
    return jsonify(test)        

if __name__ == '__main__':
    app.run(debug=True)
