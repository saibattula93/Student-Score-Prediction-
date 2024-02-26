# Student performance prediction using MLops
## Demo video of Student performance prediction
https://github.com/saibattula93/Student_Performance_Prediction/assets/116423301/8ec0ef26-c3f5-4a50-9c74-968a0e7bd416

Welcome to the Student Performance Prediction using MLops in Regression project! In this repository, we present an end-to-end solution for predicting student performance using Machine Learning and adopting MLOps practices. This README provides an overview of the model, its motivation, success metrics, requirements, methodology, architecture, pipeline, and conclusion.

## 1. Overview of the Model
This project understands how the student’s performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, and Lunch and Test preparation course.

## 2. Motivation of the Model
The motivation behind this model is to assist educational institutions in identifying students who might be at risk of underperforming. By predicting student performance early, educators can provide timely interventions and support, potentially improving overall success rates.

## 3. Success Metrics
The success of the model will be evaluated based on metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared score, which measure the accuracy and goodness-of-fit of the regression model.

## 4. Requirements & Constraints
### 4.1. Functional Requirements
Access to labeled student performance dataset.
Machine Learning libraries (e.g., scikit-learn, TensorFlow).
Deployment platform (e.g., Docker, cloud services).
### 4.2. Non-Functional Requirements
Scalability: The model should be able to handle a growing number of students and features.

Latency: Real-time predictions for timely interventions.

Security: Protecting student data and ensuring compliance with data privacy regulations.
### 4.3. Constraints
Availability and quality of input data may impact the model’s accuracy.
Resource constraints might affect the choice of algorithms and deployment options.
### 4.4. Out-of-Scope
Individual student-level interventions are out of scope; the model provides predictions but not recommendations for action.

## 5. Methodology
### 5.1. Problem Statement
Given historical student performance data and relevant features, build a regression model that can accurately predict the final grades of students.

### 5.2. Data
The dataset should include features like study hours, attendance, previous exam scores, and final grades. It should be split into training and testing sets for model evaluation.

### 5.3. Techniques
Data preprocessing: Handle missing values, feature scaling, and encoding categorical variables.

Feature selection: Identify the most relevant features for prediction.

Model selection: Choose regression algorithms (e.g., Linear Regression, Random Forest) and perform hyperparameter tuning.

MLOps integration: Implement CI/CD, model monitoring, and automated retraining for continuous improvement.

## 6. Architecture
The architecture consists of the following components:

1. **Data Ingestion:** Fetch and preprocess data.
2. **Data preprocessing:** Implement the data preprocessing technique.
3. **Model Training:** Build and train the regression model.
4. **Model Evaluation:** Assess model performance using test data.
5. **Model Deployment:** Deploy the model using a suitable platform.
6. **MLOps Pipeline:** Automate data updates, model retraining, and deployment.

## 7. Pipeline
1. Data Collection & Preprocessing
2. Feature Engineering & Selection
3. Model Building & Training
4. Model Evaluation & Metrics Calculation
5. Model Deployment & Monitoring
6. Continuous Integration & Continuous Deployment (CI/CD)
7. Model Retraining based on Data Drift


## 8. Conclusion
In this project, we have showcased a comprehensive approach to predict student performance using a regression model and MLOps practices. By accurately predicting student grades, educational institutions can take proactive measures to support struggling students and enhance overall academic success.

Life cycle of this project: ![image](https://github.com/saibattula93/Student_Performance_Prediction/assets/116423301/0b7b3892-f3ce-4517-9660-def3bd5debfc)


**If you can read on more about my project in detail please click my blog: https://www.analyticsvidhya.com/blog/2023/04/student-performance-analysis-and-prediction/** 
