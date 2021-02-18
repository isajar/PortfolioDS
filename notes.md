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

- **MAE:**
- **MSE:**
- **RMSE:**
