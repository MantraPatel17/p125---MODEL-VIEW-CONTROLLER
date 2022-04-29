from flask import Flask, jsonify, request

from classifer import get_prediction

app = Flask(__name__)

@app.route('/post-data',methods = ["POST"])

def PredictData():
    image = request.files.get("digit")
    Pred = get_prediction(image)
    return jsonify({
      "Prediction":Pred
    } , 200)


if __name__ == '__main__':
  app.run()


