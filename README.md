# Loan Default Prediction

## Project Overview
This project predicts whether a loan applicant will default or not using machine learning classification models.  
The best-performing model is deployed using a Flask web application.

Project:-“I built an end-to-end Loan Default Prediction project using classical machine learning.
I started with data cleaning, handled missing values, converted categorical features using label encoding, and fixed real-world issues like the ‘3+’ dependents value.
I trained multiple models including Logistic Regression, KNN, SVC, Naive Bayes, and Random Forest, and compared them using accuracy, confusion matrix, and ROC curve.
Random Forest performed best because it handles non-linear relationships and mixed data types well.
Finally, I deployed the model using Flask with an HTML interface, and managed the project professionally on GitHub using .gitignore.

---

## Dataset
Loan Prediction dataset containing applicant demographic and financial details.

### Features
- Gender
- Married
- Dependents
- Education
- Self Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

### Target
- Loan_Status (Approved / Rejected)

---

## Models Used
- Logistic Regression
- Random Forest Classifier
- KNN Classifier
- Support Vector Classifier (SVC)
- Naive Bayes
- XGBoost

---

## ML Workflow
1. Data cleaning & missing value handling  
2. Label encoding of categorical features  
3. Feature scaling using StandardScaler  
4. Train-test split  
5. Train multiple baseline models  
6. Compare models using accuracy  
7. Select best model  
8. Visualize performance using:
   - Accuracy comparison (matplotlib)
   - Confusion Matrix
   - ROC Curve
9. Deploy best model using Flask  

---

## Model Evaluation
- Accuracy comparison using matplotlib bar chart
- Confusion Matrix to analyze prediction errors
- ROC Curve and AUC score to measure class separation

---

## Best Model
**Random Forest Classifier**

### Why Random Forest?
- Combines multiple decision trees
- Reduces overfitting
- Handles non-linear patterns well
- Works effectively with mixed data types

---

## Deployment
Run the Flask app:
```bash
python app.py
