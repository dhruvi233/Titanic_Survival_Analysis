# 🚢 Titanic Survival Analysis

## 📌 Project Overview

The **Titanic Survival Analysis** project is a Python-based Exploratory Data Analysis (EDA) project developed to analyze passenger information from the Titanic dataset.

The main purpose of this project is to understand the factors that influenced passenger survival, including gender, age, passenger class and embarkation location.

The project uses Pandas for data manipulation, NumPy for numerical calculations, Matplotlib and Seaborn for data visualization.

🎥 Project Demonstration Video

I have also recorded a video explaining the project, its functionalities, implementation and working process.

Watch the Project Explanation Video:

▶️https://drive.google.com/file/d/1CYMMoAQbhLkP-yDym1teNPTh8V6gDS_C/view?usp=sharing

## 🎯 Objectives

- To explore and analyze the Titanic passenger dataset.
- To identify and handle missing values.
- To analyze passenger survival rates.
- To understand survival patterns based on gender and passenger class.
- To perform numerical and statistical calculations.
- To create meaningful data visualizations.
- To understand the practical implementation of Python libraries.

## 🚀 Features

1. **Load Dataset**
   - Import Titanic passenger data from a CSV file.
   - Handle file loading errors.

2. **Explore Data**
   - Display the first five rows.
   - Display the last five rows.
   - Display column names.
   - Display dataset information.
   - Generate descriptive statistics.

3. **Data Cleaning**
   - Identify missing values.
   - Fill missing Age values using median.
   - Fill missing Embarked values using mode.
   - Fill missing Fare values using median.
   - Replace missing Cabin values with "Unknown".

4. **Survival Analysis**
   - Calculate total passengers.
   - Display survival counts.
   - Calculate survival percentages.
   - Analyze survival rates by gender.
   - Analyze survival rates by passenger class.
   - Analyze survival rates by embarkation location.
   - Calculate average age and fare.

5. **NumPy Operations**
   - Convert Age column into NumPy arrays.
   - Perform indexing and slicing.
   - Calculate average age.
   - Find maximum and minimum age.
   - Calculate standard deviation and variance.

6. **Data Visualization**
   - Survival Count Plot.
   - Survival by Gender.
   - Survival by Passenger Class.
   - Age Distribution Histogram.
   - Fare Distribution Histogram.
   - Correlation Heatmap.

7. **Save Cleaned Dataset**
   - Export the cleaned dataset into a CSV file.
   - Generate `cleaned_titanic.csv`.

8. **Menu-Driven Interface**
   - Select different analysis operations.
   - Execute required functions through the main menu.
   - Exit the application.

## 🛠️ Python Concepts Used

- Variables and Data Types
- Functions
- Global Variables
- Conditional Statements
- While Loop
- If-Elif-Else
- Exception Handling
- File Handling
- Menu-Driven Programming
- Data Manipulation
- Exploratory Data Analysis (EDA)

## 📚 Libraries Used

- **Pandas:** Loading, cleaning and analyzing passenger data.
- **NumPy:** Numerical calculations and array operations.
- **Matplotlib:** Creating graphs and histograms.
- **Seaborn:** Creating statistical visualizations and heatmaps.

## 📂 Project Structure

```text
Titanic Survival Analysis/
│
├── titanic_analysis.py
├── titanic.csv
├── cleaned_titanic.csv
│
└── README.md
```

## ▶️ How to Run the Project

**Step 1:** Install Python on your system.

**Step 2:** Download the Titanic training dataset (`train.csv`) from Kaggle.

**Dataset Link:** https://www.kaggle.com/competitions/titanic/data

**Step 3:** Rename the downloaded file to `titanic.csv`.

**Step 4:** Install the required libraries.

```bash
pip install pandas numpy matplotlib seaborn
```

**Step 5:** Keep the Python file and CSV dataset in the same folder.

**Step 6:** Open the project folder in VS Code.

**Step 7:** Run the Python file.

```bash
python titanic_analysis.py
```

**Step 8:** Select the required operations from the main menu.

## 💻 Sample Program Output

```text
========== TITANIC SURVIVAL ANALYSIS ==========

1. Load Dataset
2. Explore Data
3. Clean Data
4. Survival Analysis
5. NumPy Operations
6. Data Visualization
7. Save Cleaned Data
8. Exit

Enter your choice: 1

Dataset loaded successfully!
```

Example survival analysis output:

```text
Total Passengers: 891

Survival Count:

0    549
1    342

Survival Percentage:

0    61.62
1    38.38
```

*The example percentages are based on the standard Kaggle Titanic training dataset.*

## ⚠️ Input Validation Rules

- The Titanic dataset must be available in CSV format.
- The dataset must contain the required columns.
- The dataset must be loaded before performing analysis.
- Missing numerical and categorical values are handled using suitable methods.
- Invalid menu choices are handled.
- File loading errors are handled using exception handling.

## 📝 Assumptions

- The Kaggle Titanic training dataset is used for this project.
- The `Survived` column represents passenger survival status:
  - 0 = Did not survive.
  - 1 = Survived.
- Passenger class is represented by 1, 2 and 3.
- Missing Age and Fare values are filled using median.
- Missing Embarked values are filled using mode.
- Missing Cabin values are replaced with "Unknown".

## 🔮 Future Enhancements

- Add interactive dashboards using Plotly.
- Analyze survival patterns by family size.
- Perform more advanced statistical analysis.
- Add additional visualizations.
- Implement machine learning models to predict passenger survival.

## 👩‍💻 Author

**Dhruvi Das**

Student | Python Programming & Data Analytics Project

## 📄 License

This project is developed for educational and learning purposes. No open-source license has been specified.

---

✨ Happy Coding! ✨
