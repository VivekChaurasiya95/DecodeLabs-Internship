<div align="center">
  <img src="https://media.giphy.com/media/3oKIPeqZ1B0Eu0Fz56/giphy.gif" alt="Advanced Data GIF" width="500">

  # 🔍 Advanced EDA & Feature Engineering
  ### *DecodeLabs Task 1*
</div>

---

## 📊 Comprehensive Project Overview
This project transitions from basic data viewing to **Advanced Exploratory Data Analysis (EDA)** and **Feature Engineering**. Working with an E-commerce Order Dataset (`Dataset for Data Analytics - Sheet1.csv`), the objective is to rigorously clean the data, handle complex missing values, detect anomalies, engineer new predictive features, and visualize multidimensional relationships to unearth actionable business intelligence.

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=500&color=E74C3C&center=true&vCenter=true&width=800&lines=KNN+Missing+Value+Imputation;IQR+Outlier+Detection;Temporal+Feature+Extraction;Mutual+Information+%26+Feature+Importance" alt="Typing SVG" />
</div>

---

## 📂 Dataset Information
The dataset consists of **1,200 orders** across **14 distinct features**:
- **Identifiers**: `OrderID`, `CustomerID`, `TrackingNumber`
- **Product Details**: `Product`, `Quantity`, `UnitPrice`, `ItemsInCart`
- **Transaction Details**: `Date`, `ShippingAddress`, `PaymentMethod`, `OrderStatus`, `CouponCode`, `ReferralSource`, `TotalPrice`

---

## 🚀 Detailed Technical Workflow

### 1. Data Cleaning & Null Handling
- **Initial Inspection**: Used `.info()` and `.isnull().sum()` to map out data gaps. `CouponCode` showed significant missingness.
- **Advanced Imputation**: Rather than using simple mean/mode for numeric/categorical features blindly, implemented **KNNImputer** alongside statistical mode logic to reconstruct missing categorical links based on neighborhood similarity.

### 2. Outlier Detection & Treatment
- **Visual Detection**: Utilized Seaborn `boxplot` and `violinplot` to identify skewness and extreme values in `UnitPrice` and `TotalPrice`.
- **Statistical Filtering**: Applied the **Interquartile Range (IQR)** method to cap or flag outliers, ensuring statistical models won't be heavily skewed by extreme individual transactions.

### 3. Feature Engineering & Extraction
- **Temporal Extraction**: Converted the raw `Date` string into a `datetime` object. Extracted new independent features: `Year`, `Month`, `Day`, and `DayOfWeek`.
- **Aggregations**: Validated `TotalPrice` consistency by cross-referencing `Quantity * UnitPrice`.

### 4. Data Preprocessing & Encoding
- **Categorical Encoding**: Transformed categorical text (e.g., `PaymentMethod`, `OrderStatus`, `ReferralSource`) into machine-readable formats using **One-Hot Encoding** (`pd.get_dummies()`).
- **Feature Scaling**: Applied **StandardScaler** to standardize normally distributed features and **MinMaxScaler** to normalize skewed data, placing all continuous variables on a uniform scale.

### 5. Advanced EDA & Visualizations
- **Univariate Analysis**: Histograms and KDE plots showing the distribution of numerical features.
- **Bivariate Analysis**: Scatter plots analyzing `Quantity` vs `TotalPrice`.
- **Multivariate Analysis**: Generated an exhaustive **Correlation Matrix Heatmap** to identify collinearity between variables.

### 6. Feature Selection
- Implemented **Mutual Information Scores** to quantify the dependency between independent variables and target outcomes.
- Trained a baseline **Random Forest Regressor/Classifier** to extract mathematical `Feature Importances`, validating which newly engineered features carry the most predictive power.

---

## 🛠️ Technology Stack
- **Python** 🐍
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning / Preprocessing**: Scikit-Learn (`KNNImputer`, `StandardScaler`, `MinMaxScaler`, `RandomForest`)
- **Data Visualization**: Matplotlib, Seaborn

---
<div align="center">
  <img src="https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif" width="300" alt="Code Matrix">
  <br>
  <i>"Feature engineering is the secret sauce to predictive modeling."</i>
</div>
