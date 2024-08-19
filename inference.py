import joblib
import tensorflow as tf
import numpy as np

labels = []
with open('labels.txt','r') as f:
    for f in f.readlines():
        labels.append(f.split('\t')[1].strip())


files_list = ['logistic_regression.pkl',
              'decision_tree.pkl',
              'k_neighbors.pkl',
              'random_forest.pkl',
              'gradient_boost.pkl',
              'x_gradient_boost.pkl',
              'stacking.pkl',
              'neural_network.keras']
def get_predictions(model_num,features):
    features = np.reshape(features,[1,5])
    if model_num in range(1,8):
        model = joblib.load(files_list[model_num-1])
        pred = model.predict(features)

    elif model_num == 8:
        model = tf.keras.models.load_model(files_list[model_num-1])
        pred = tf.argmax(model.predict(features),-1)
        
    return labels[pred[0]]


features = []
feature_list = ['CO_Room','H2_Room','Humidity_Room','Temperature_Room','VOC_Room_RAW']
for i in range(5):
    features.append(float(input(f'Enter the {feature_list[i]} value\t')))


model_num = int(input(f'Which model to use......\n\
                1.Logistic Regression\n\
                2.Decision Tree\n\
                3.KNeighbors\n\
                4.Random Forest\n\
                5.Gradient Boosting\n\
                6.Extreme Gradient Boosting\n\
                7.Stacking\n\
                8.Neural Network\n'))

print(get_predictions(model_num,features))
