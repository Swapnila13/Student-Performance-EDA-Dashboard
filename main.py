# main.py
# Student Performance EDA functions

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8,5)

# -------------------------
# Load Dataset & Feature Engineering
# -------------------------
def load_data(file_path="StudentsPerformance.csv"):
    df = pd.read_csv(file_path)
    # Create total score
    df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]
    return df

# -------------------------
# Dataset Summary
# -------------------------
def get_summary(df):
    return df.describe()

# -------------------------
# Missing Values
# -------------------------
def missing_values(df):
    return df.isnull().sum()

# -------------------------
# Plots / Visualizations
# -------------------------

# Gender distribution
def plot_gender_distribution(df):
    fig, ax = plt.subplots()
    sns.countplot(x="gender", data=df, ax=ax)
    ax.set_title("Gender Distribution")
    return fig

# Score distributions
def plot_score_distribution(df, score_column):
    fig, ax = plt.subplots()
    sns.histplot(df[score_column], kde=True, bins=10, ax=ax)
    ax.set_title(f"{score_column.capitalize()} Distribution")
    return fig

# Gender vs Math Score
def plot_gender_vs_math(df):
    fig, ax = plt.subplots()
    sns.boxplot(x="gender", y="math score", data=df, ax=ax)
    ax.set_title("Gender vs Math Score")
    return fig

# Test preparation vs Total Score
def plot_testprep_vs_total(df):
    fig, ax = plt.subplots()
    sns.boxplot(x="test preparation course", y="total_score", data=df, ax=ax)
    ax.set_title("Test Preparation Course vs Total Score")
    return fig

# Parental Education vs Total Score
def plot_parental_education_vs_total(df):
    fig, ax = plt.subplots()
    sns.boxplot(x="parental level of education", y="total_score", data=df, ax=ax)
    ax.set_title("Parental Level of Education vs Total Score")
    plt.xticks(rotation=45)
    return fig

# Lunch vs Total Score
def plot_lunch_vs_total(df):
    fig, ax = plt.subplots()
    sns.boxplot(x="lunch", y="total_score", data=df, ax=ax)
    ax.set_title("Lunch Type vs Total Score")
    return fig

# Correlation heatmap
def plot_correlation_heatmap(df):
    fig, ax = plt.subplots()
    corr = df[["math score","reading score","writing score","total_score"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Score Correlation Heatmap")
    return fig


