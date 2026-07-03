<div align="center">
  <img src="https://media.giphy.com/media/xT9Igz89RUG1JqE3zW/giphy.gif" alt="Clustering GIF" width="400">

  # 👥 Customer Segmentation via PCA & K-Means
  ### *DecodeLabs Task 3 (Unsupervised Learning)*
</div>

---

## 🎯 Comprehensive Objective
Modern e-commerce relies heavily on personalized marketing. This project applies **Unsupervised Machine Learning** to an extensive `Online_Retail.csv` dataset. By engineering RFM metrics and utilizing dimensionality reduction (PCA) alongside K-Means clustering, the goal is to mathematically deduce distinct customer personas without predefined labels.

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=500&color=F39C12&center=true&vCenter=true&width=800&lines=RFM+(Recency,+Frequency,+Monetary)+Analysis;Principal+Component+Analysis+(PCA);Elbow+Method+%26+Silhouette+Scores;K-Means+Clustering+%26+Radar+Charts" alt="Typing SVG" />
</div>

---

## 📂 Dataset Profile
- **Size**: Massive dataset with **541,909 rows** and 8 columns.
- **Features**: `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`.

---

## 🧠 In-Depth Technical Methodology

### 1. Data Cleaning & Preprocessing
- **Filtering**: Removed cancelled orders (identified by `InvoiceNo` starting with 'C').
- **Null Handling**: Dropped rows missing `CustomerID` as they cannot be tied to an individual segment.
- **Aggregation**: Created a `Total_Spend` column mathematically derived from `Quantity * UnitPrice`.

### 2. RFM Feature Engineering
Aggregated the massive transactional data into a unique Customer-Level DataFrame using the RFM framework:
- **Recency**: Number of days since the customer's last purchase relative to the dataset's maximum date.
- **Frequency**: Total count of unique invoices per customer.
- **Monetary**: Sum of all `Total_Spend` per customer.
- **EDA on RFM**: Generated pairplots, histograms, and checked skewness/kurtosis to understand the heavy right-tail distribution of retail spending.

### 3. Dimensionality Reduction (PCA)
- **Standardization**: Scaled the RFM data using `StandardScaler` to ensure K-Means calculates distances symmetrically.
- **PCA Implementation**: Extracted Principal Components. Evaluated the **Explained Variance Ratio** and plotted a **Scree Plot** and **Cumulative Variance Plot** to mathematically determine the optimal number of components required to retain 95% of the data's variance.
- **Loadings**: Visualized feature contributions to the principal components via a correlation heatmap.

### 4. K-Means Clustering Optimization
- **Elbow Method**: Iterated `k` from 2 to 10, plotting the Within-Cluster-Sum-of-Squares (WCSS) to find the inflection point.
- **Silhouette Analysis**: Calculated the Silhouette Score for every `k` to measure cluster cohesion vs. separation, successfully identifying the mathematically optimal `k`.

### 5. Model Evaluation & Visualization
- Trained the final K-Means model on the chosen `k`.
- Visualized the resultant clusters extensively using **2D Scatter Plots** (PC1 vs PC2) and **3D Scatter Plots** (PC1 vs PC2 vs PC3).
- Displayed cluster centers and generated a cluster-wise summary DataFrame.

### 6. Business Insights & Radar Charts
- Visualized cluster attributes using **Radar/Spider Charts** and Heatmaps for comparative analysis.
- **Persona Generation**: Translated raw cluster centers into distinct business personas:
  - *Champions*: High frequency, high monetary, very recent.
  - *At Risk*: High monetary, but high recency (haven't bought recently).
  - *New/Casual*: Low frequency, low monetary.
- Formulated strict **Business Recommendations** tailored to each segment to maximize retention and ROI.

---

## 🛠️ Technology & Libraries
- **Unsupervised ML**: `KMeans`, `PCA` (Scikit-Learn)
- **Preprocessing**: `StandardScaler` (Scikit-Learn)
- **Data & Visualization**: Pandas, NumPy, Matplotlib, Seaborn, `mpl_toolkits.mplot3d` (for 3D charts).

---
<div align="center">
  <img src="https://media.giphy.com/media/d2jjuAZzDSVLZ5kI/giphy.gif" width="300" alt="Data Network">
  <br>
  <i>"Mapping the mathematical DNA of customer behavior."</i>
</div>
