
# TITANIC SURVIVAL ANALYSIS PROJECT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.DataFrame()


def load_data():
    global data

    try:
        data = pd.read_csv("titanic.csv")
        print("\nDataset loaded successfully!")

    except FileNotFoundError:
        print("File not found! Check titanic.csv location.")




def explore_data():

    if data.empty:
        print("Please load dataset first!")
        return

    print("\nFirst 5 rows:")
    print(data.head())

    print("\nLast 5 rows:")
    print(data.tail())

    print("\nColumn Names:")
    print(data.columns)

    print("\nDataset Information:")
    data.info()

    print("\nStatistical Description:")
    print(data.describe())


def clean_data():

    if data.empty:
        print("Please load dataset first!")
        return

    print("\nMissing Values Before Cleaning:")
    print(data.isnull().sum())

    # Fill missing Age with median
    data["Age"] = data["Age"].fillna(data["Age"].median())

    # Fill missing Embarked with mode
    data["Embarked"] = data["Embarked"].fillna(
        data["Embarked"].mode()[0]
    )

    # Fill missing Fare with median
    data["Fare"] = data["Fare"].fillna(data["Fare"].median())

    # Fill missing Cabin
    data["Cabin"] = data["Cabin"].fillna("Unknown")

    print("\nData cleaned successfully!")

    print("\nMissing Values After Cleaning:")
    print(data.isnull().sum())



def survival_analysis():

    if data.empty:
        print("Please load dataset first!")
        return

    print("\nTotal Passengers:", len(data))

    print("\nSurvival Count:")
    print(data["Survived"].value_counts())

    print("\nSurvival Percentage:")
    print(data["Survived"].value_counts(normalize=True) * 100)

    print("\nSurvival by Gender:")
    print(data.groupby("Sex")["Survived"].mean() * 100)

    print("\nSurvival by Passenger Class:")
    print(data.groupby("Pclass")["Survived"].mean() * 100)

    print("\nSurvival by Embarked Location:")
    print(data.groupby("Embarked")["Survived"].mean() * 100)

    print("\nAverage Age:")
    print(data["Age"].mean())

    print("\nAverage Fare:")
    print(data["Fare"].mean())




def numpy_analysis():

    if data.empty:
        print("Please load dataset first!")
        return

    age_array = data["Age"].dropna().to_numpy()

    print("\nAge Array:")
    print(age_array)

    print("\nFirst 5 Ages:")
    print(age_array[:5])

    print("\nAverage Age:", np.mean(age_array))

    print("Maximum Age:", np.max(age_array))

    print("Minimum Age:", np.min(age_array))

    print("Standard Deviation:", np.std(age_array))

    print("Variance:", np.var(age_array))




def visualization():

    if data.empty:
        print("Please load dataset first!")
        return

    print("\n1. Survival Count")
    print("2. Survival by Gender")
    print("3. Survival by Passenger Class")
    print("4. Age Distribution")
    print("5. Fare Distribution")
    print("6. Correlation Heatmap")

    choice = input("Enter your choice: ")

    if choice == "1":

        sns.countplot(x="Survived", data=data)

        plt.title("Titanic Survival Count")
        plt.xlabel("Survived (0 = No, 1 = Yes)")
        plt.ylabel("Number of Passengers")

    elif choice == "2":

        sns.countplot(
            x="Sex",
            hue="Survived",
            data=data
        )

        plt.title("Survival by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Number of Passengers")

    elif choice == "3":

        sns.barplot(
            x="Pclass",
            y="Survived",
            data=data
        )

        plt.title("Survival Rate by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")

    elif choice == "4":

        plt.hist(data["Age"], bins=20)

        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Frequency")

    elif choice == "5":

        sns.histplot(data["Fare"], bins=20)

        plt.title("Fare Distribution")
        plt.xlabel("Fare")
        plt.ylabel("Frequency")

    elif choice == "6":

        sns.heatmap(
            data.select_dtypes(include=np.number).corr(),
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Titanic Correlation Heatmap")

    else:
        print("Invalid choice!")
        return

    plt.tight_layout()
    plt.show()



def save_data():

    if data.empty:
        print("Please load dataset first!")
        return

    data.to_csv("cleaned_titanic.csv", index=False)

    print("\nCleaned dataset saved successfully!")




while True:

    print("\n========== TITANIC SURVIVAL ANALYSIS ==========")

    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Clean Data")
    print("4. Survival Analysis")
    print("5. NumPy Operations")
    print("6. Data Visualization")
    print("7. Save Cleaned Data")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        load_data()

    elif choice == "2":
        explore_data()

    elif choice == "3":
        clean_data()

    elif choice == "4":
        survival_analysis()

    elif choice == "5":
        numpy_analysis()

    elif choice == "6":
        visualization()

    elif choice == "7":
        save_data()

    elif choice == "8":
        print("Thank you for using Titanic Analysis!")
        break

    else:
        print("Invalid choice! Please try again.")
