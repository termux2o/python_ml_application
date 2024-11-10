from django.http import JsonResponse
import pickle
import numpy as np

# Load the model
with open("mlappfinal/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(request):
    # Get parameters from the URL query string
    sepal_length = float(request.GET.get("sepal_length"))
    sepal_width = float(request.GET.get("sepal_width"))
    petal_length = float(request.GET.get("petal_length"))
    petal_width = float(request.GET.get("petal_width"))
    
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    return JsonResponse({"prediction": int(prediction[0])})
