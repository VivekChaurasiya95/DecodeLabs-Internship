<div align="center">
  <img src="https://media.giphy.com/media/W36mE7A2Ew2x4E3wA0/giphy.gif" alt="Data Analysis GIF" width="400">

  # 🛒 Basic Exploratory Data Analysis
  ### *DecodeLabs Drive Task*
</div>

---

## 📋 Comprehensive Overview
This specific repository represents the initial step in the DecodeLabs Internship. It introduces the fundamental concepts of handling tabular data using Python. By interacting with a rich dataset of customer shopping patterns, this task emphasizes understanding data structures, recognizing anomalies, and extracting baseline statistical summaries before any complex modeling occurs.

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=500&color=27AE60&center=true&vCenter=true&width=800&lines=Loading+Dataset+(99k+Rows)...;Evaluating+Categorical+Data...;Calculating+Statistical+Summaries..." alt="Typing SVG" />
</div>

---

## 📂 Dataset Details
The dataset utilized is `customer_shopping_data.csv`, comprising **99,457 entries** and **10 features**:
1. `invoice_no`: Unique identifier for the transaction.
2. `customer_id`: Unique identifier for the shopper.
3. `gender`: Male / Female categorization.
4. `age`: Customer age ranging from 18 to 69.
5. `category`: Product grouping (e.g., Clothing, Shoes, Toys).
6. `quantity`: Number of items purchased per invoice (1 to 5).
7. `price`: Total cost of the items.
8. `payment_method`: Cash, Credit Card, Debit Card.
9. `invoice_date`: Date of the transaction.
10. `shopping_mall`: The location where the purchase was made.

---

## 🔬 Detailed Step-by-Step Workflow

### 1. Environment Setup & Data Ingestion
- **Libraries**: Configured the environment using `numpy` for array manipulation and `pandas` for DataFrame operations.
- **Loading**: Utilized Google Colab's `files.upload()` mechanism to ingest the dataset securely.

### 2. High-Level Data Inspection
- **`.head()`**: Extracted the first 5 rows to visually confirm data integrity and formatting.
- **`.shape`**: Verified the dimensionality of the dataset (99,457 rows × 10 columns).
- **`.columns`**: Listed all feature names to ensure parsing was successful.

### 3. Data Profiling & Quality Checks
- **`.info()`**: Analyzed the memory footprint (7.6+ MB) and the data types of each column (1 Float, 2 Integers, 7 Objects/Strings).
- **`.isnull().sum()`**: Conducted a rigorous check for missing or `NaN` values across all vectors. The dataset was found to be perfectly clean with 0 missing values.
- **`.describe()`**: Generated descriptive statistics for numerical columns:
  - Discovered the average customer age is ~43 years.
  - The mean purchase quantity is exactly 3 items.
  - The average transaction price is approximately ~689 units, with a maximum spend of 5,250 units.

---

## 🛠️ Tools & Libraries Utilized
- **Python** 🐍
- **Pandas** 🐼 
- **NumPy** 🔢 

<br>
<div align="center">
  <i>"A thorough understanding of your raw data is the prerequisite to any successful machine learning pipeline."</i>
</div>
