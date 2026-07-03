<div align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jIGsnu/giphy.gif" alt="Fraud Detection GIF" width="400">

  # 🛡️ Credit Card Fraud Detection Pipeline
  ### *DecodeLabs Task 2*
</div>

---

## 🎯 Comprehensive Objective
Credit card fraud is a rare but highly damaging event. This project tackles the intricacies of **Supervised Binary Classification** on highly imbalanced data (`credit_card_fraud_10k.csv`). The pipeline encompasses rigorous preprocessing, synthetic data generation, model training, hyperparameter tuning, and advanced threshold evaluation.

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=500&color=9B59B6&center=true&vCenter=true&width=800&lines=Handling+1.5%25+Fraud+Imbalance;SMOTE+Synthetic+Oversampling;Scikit-Learn+%2B+Imblearn+Pipelines;GridSearchCV+Hyperparameter+Tuning" alt="Typing SVG" />
</div>

---

## 📂 Dataset Profile
- **Size**: 10,000 Transactions.
- **Class Imbalance**: Only ~1.5% of the dataset is marked as Fraud (`is_fraud` = 1).
- **Features**: 
  - `amount`, `transaction_hour`, `merchant_category`
  - `foreign_transaction`, `location_mismatch`
  - `device_trust_score`, `velocity_last_24h`, `cardholder_age`

---

## 🧠 In-Depth Technical Methodology

### 1. Data Segregation & Pipeline Architecture
- Segregated data into `X` (Features) and `y` (Target). Applied an 80/20 train-test split via `train_test_split`.
- Built modular preprocessing pipelines using `ColumnTransformer`:
  - **Numerical Features**: Scaled using `StandardScaler` to ensure algorithms like Logistic Regression converge properly.
  - **Categorical Features**: Handled via `OneHotEncoder` (e.g., transforming `merchant_category` into distinct binary columns).

### 2. Solving Class Imbalance with SMOTE
- Because algorithms favor the majority class, evaluating accuracy alone leads to a false sense of security.
- Integrated **SMOTE (Synthetic Minority Over-sampling Technique)** using `imblearn.pipeline.Pipeline`. SMOTE synthetically generates new fraud examples in the feature space based on nearest neighbors, ensuring the models train on a balanced representation.

### 3. Model Engineering & Tuning
Implemented and compared two powerful algorithms:
1. **Logistic Regression**: Serves as an interpretable, fast baseline.
2. **Random Forest Classifier**: A robust ensemble tree algorithm capable of capturing complex, non-linear fraud patterns.
- Executed extensive **Hyperparameter Tuning** via `GridSearchCV` (testing different max depths, estimators, and class weights) using cross-validation to prevent overfitting.

### 4. Advanced Evaluation Metrics
Standard accuracy is discarded in favor of metrics sensitive to the minority class:
- **Confusion Matrix**: To strictly monitor False Positives (customer friction) and False Negatives (financial loss).
- **Precision & Recall**: Calculated directly and visualized via the **Precision-Recall Curve**.
- **F1-Score**: The harmonic mean of precision and recall.
- **ROC-AUC Score**: Receiver Operating Characteristic curve to measure the model's ability to distinguish between fraud and legitimate transactions across all threshold values.

### 5. Final Outputs
- Extracted and plotted **Feature Importances** from the optimized Random Forest to inform business logic (e.g., identifying that `device_trust_score` and `amount` are massive indicators of fraud).
- Saved the final production-ready model architecture using `joblib`.

---

## 🛠️ Technology & Libraries
- **Scikit-Learn**: `ColumnTransformer`, `StandardScaler`, `OneHotEncoder`, `GridSearchCV`, `RandomForestClassifier`, `LogisticRegression`.
- **Imbalanced-Learn (imblearn)**: `SMOTE`, `ImbPipeline`.
- **Data & Viz**: Pandas, NumPy, Matplotlib, Seaborn.

---
<div align="center">
  <img src="https://media.giphy.com/media/J1Y89ThkHjwJxeRS0A/giphy.gif" width="250" alt="Security Shield">
  <br>
  <i>"In fraud detection, a False Negative is a financial loss; a False Positive is a lost customer."</i>
</div>
