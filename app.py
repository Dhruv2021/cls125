from flask import Flask,jsonify,request
from model import get_prediction
import cv2
import numpy as np

app=Flask(__name__)
@app.route("/predictdigit",methods=["POST"])
def predictdata():
    image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
    prediction=get_prediction(image)
    return jsonify({
        "result":prediction
    }),200
if __name__ == "__main__":
    app.run(debug=True)
    