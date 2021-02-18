## ML NOTES

### SUPERVISED LEARNING

- Also known as labeled training.
- The desidered output is known.
- Learning from historicla data to predict new outputs.
- Compare actual output with correct output to finde errors and adjust the model.

### ML PROCESS

1. Data Acquisition.
2. Data Cleaning.
3. Model Training and Building.
4. Model Testing
5. Model Deployment

### DATA SPLIT

- Training data: Train model parameters.
- Validation data: Adjust Hyperparameters.
- Test data: Get final performance metric.

### EVALUATION PERFORMANCE

#### Clasification

TP: true positives
TN: true negatives
FP: false positives -> type I error.
FN: false negatives -> type II error.

- Compare prediction to correct label. Confusion Matrix.
- **Accuracy:** # of correct prediction dividev by the total number of prediction. Target Classes must be well balanced for being useful metric.
- **Recall:** Ability of a model to find all relevant cases within a data set. The % of actual spam email that were correctly classified. -> TP / (TP + FN).
- **Precision:** Ability of a model to identify only the relevant data points. The % of email flagged as spam that were correctly classified. -> TP / (TP + FP).
- Often you have a trade-off between recall and precision. If you want to minimize FN you propably will increase FP.
- **F1-Score:** Optimal blend of precision and recall. Harmonic Mean. Punishes extreme values (EX. pre = 1 & rec = 0 -> F1 = 0.5).
- Conclusion: All depends on the context of the situation. We have to decide if the model will try to fix FN or FP. If it is a disease is better to reduce FN at the cost of increase FP.

#### Regression

- **MAE:** Mean Absolute Error -> 1/n \* sum(y_true - y_pred). Won't punish large errors. If the majority of points are well predicted, large error will be hiddem.
- **MSE:** Mean Squared Error -> 1/n \* sum( (y_true - y_pred) ^ 2). Will give more weigth to large errors. The result has different unit than y (unit(y)^2).
- **RMSE:** Root Mean Square Error -> sqrt(MSE). Most popular, has the same unit as y.

#### Conclusion

- You have to take into account your context. $10 is good for housing price, but horrible for candy price.
- Compare your error metric to the average value of the label in your data set.

### Bias-Variance Trade-Off

- The bias-variance trade-off is the point where we are adding just noise by adding model complexity.
- The training error goes down as it has but the test error is starting to go up.
- You can think the data as a convination of signal + noise.
  ** As your model has less bias and more variance you are learning the signal and the noise (overfiting).
  ** As your model has more bias and less variance you avoid noise but learn only part of the signal (underfitting).

### MODELS

#### Logistic Regression

- Clasification problems.
- Sigmoid funtion to get values between 0 and 1.
- Based off this value (probability) we assign a class putting a cut off point in some value like 0.5 (0<-x <? 0.5 ?> x-> 1)

### KNN k-nearest neighbours

1. Calculate the distance from x (new point) to all points in your data.
2. Sort the points in your data by increasing distance from x.
3. Predict the majority label of the "k" closet point. Basically you count whose class has more points in your count.
