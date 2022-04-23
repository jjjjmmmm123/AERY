import pickle

FILE_NAME = 'random_forest_model.sav'
sc = pickle.load(open('scaler.pkl','rb'))
loaded_model = pickle.load(open(FILE_NAME, 'rb'))

def predict(data_from_user):
    X = sc.transform(new_data)
    prediction = loaded_model.predict(X)
    return prediction


new_data = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 85, 82, 89, 83]]


print(predict(new_data)[0])

