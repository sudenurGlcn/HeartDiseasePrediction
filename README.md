# HeartDiseasePrediction
This project utilizes a neural network model to predict the risk of heart disease based on user health data. The model is developed using one of the deep learning algorithms, 1D Convolutional Neural Network (1DCNN).

![image](https://github.com/sudenurGlcn/HeartDiseasePrediction/blob/main/images/HeartDiseasePrediction1.png)
![image](https://github.com/sudenurGlcn/HeartDiseasePrediction/blob/main/images/HeartDiseasePrediction2.png)
## Project Description
This project assists users in predicting the risk of heart disease by inputting their personal health information. After users enter basic health data such as age, gender, smoking status, alcohol consumption, and other relevant factors, the model utilizes this information to predict the likelihood of heart disease. The prediction result is presented to the user as a probability value. 
## Usage
The project serves users through a website interface. Users input their personal health information on the website and view the predicted risk of heart disease provided by the model.

## Development of the Model
The model is developed using the Python programming language and the TensorFlow library. Unlike image processing problems, the CNN architecture is appropriately used in predicting heart disease with a one-dimensional CNN. Suitable datasets are used for training and testing the model. The dataset used is the 2022 dataset shared by Kamıl Pytlak on Kaggle in the "Indicators of Heart Disease (2022 UPDATE)" notebook.

## Risk Score Calculation Steps
### Step 1:
The user needs to provide answers to the questions asked on the website.
![image](https://github.com/sudenurGlcn/HeartDiseasePrediction/blob/main/images/HeartDiseasePrediction4.png)
![image](https://github.com/sudenurGlcn/HeartDiseasePrediction/blob/main/images/HeartDiseasePrediction5.png)

### Step 2: 
The answers provided by the user are taken by the form structure in the index.html page and passed to the predict function in the app.py file. After the inputs from the user are prepared to be used in the model within the predict function, they are passed to the model. The result returned from the model is then displayed to the user on the result.html page.

![image](https://github.com/sudenurGlcn/HeartDiseasePrediction/blob/main/images/HeartDiseasePrediction3.png)
