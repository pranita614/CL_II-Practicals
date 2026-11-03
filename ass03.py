import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import pandas as pd  # Imports Pandas library for data handling and analysis

from pgmpy.models import DiscreteBayesianNetwork  # Imports the class to create a Discrete Bayesian Network, Probabilistic Graphical Models-represent relationships between different variables.
from pgmpy.estimators import MaximumLikelihoodEstimator  # Estimates probabilities from the dataset
from pgmpy.inference import VariableElimination  # Performs probability-based inference using the Bayesian Network

data = pd.read_csv("heartdisease.csv")  # Reads the heart disease CSV dataset

print("First 5 records:")
print(data.head())
print("\nDataset columns:")
print(data.columns.tolist())

columns = [  # Stores the required column names from the dataset
    "age",
    "Gender",
    "Family",
    "diet",
    "Lifestyle",
    "cholestrol",
    "heartdisease"
]

data = data[columns]  # Selects only the required columns from the dataset

data = data.dropna()  # Removes rows containing missing values

for column in columns:  # Loops through each selected column
    data[column] = pd.to_numeric(data[column], errors="coerce")  # Converts column values into numbers; invalid values become NaN

data = data.dropna()  # Removes rows containing missing or invalid values

for column in columns:  # Loops through each selected column
    data[column] = data[column].astype(int)  # Converts all column values into integers

model = DiscreteBayesianNetwork([  # Creates a Bayesian Network with the following relationships
    ("age", "heartdisease"),  # Age influences heart disease probability
    ("Gender", "heartdisease"),  # Gender influences heart disease probability
    ("Family", "heartdisease"),  # Family history influences heart disease probability
    ("diet", "heartdisease"),  # Diet influences heart disease probability
    ("Lifestyle", "heartdisease"),  # Lifestyle influences heart disease probability
    ("cholestrol", "heartdisease")  # Cholesterol influences heart disease probability
])

estimator = MaximumLikelihoodEstimator(model, data)  # Estimates probabilities using the dataset
cpds = estimator.get_parameters()  # Calculates Conditional Probability Distributions (CPDs)

model.add_cpds(*cpds)  # Adds the calculated CPDs to the Bayesian Network

print("\nBayesian Network Edges:")
print(list(model.edges()))

print("\nModel valid:")
print(model.check_model())

print("\nConditional Probability Distributions:")

for cpd in model.get_cpds():  # Loops through all Conditional Probability Distributions
    print("\n", cpd)

inference = VariableElimination(model)  # Creates an inference object to calculate probabilities

print("\nEnter Patient Information")
print("-------------------------")

age = int(input("Age category: "))  # Takes the patient's age category as integer input
gender = int(input("Gender (0/1): "))  # Takes gender as input (0 or 1)
family = int(input("Family history (0/1): "))  # Takes family history as input (0 or 1)
diet = int(input("Diet (0/1): "))  # Takes diet category as input (0 or 1)
lifestyle = int(input("Lifestyle (0-3): "))  # Takes lifestyle category as input (0 to 3)
cholestrol = int(input("Cholesterol category (0-2): "))  # Takes cholesterol category as input (0 to 2)

evidence = {  # Creates a dictionary containing patient information
    "age": age,
    "Gender": gender,
    "Family": family,
    "diet": diet,
    "Lifestyle": lifestyle,
    "cholestrol": cholestrol
}

result = inference.query(  # Calculates the probability of heart disease
    variables=["heartdisease"],  # Specifies the variable whose probability is required
    evidence=evidence  # Provides the patient's information as evidence
)

print("\nDiagnosis Result")
print("----------------")

print(result)

probabilities = result.values  # Extracts the calculated probability values from the result

print(
    "\nProbability of No Heart Disease:",
    round(probabilities[0] * 100, 2), "%"  # Converts probability into percentage and rounds to 2 decimal places
    
)

print(
    "Probability of Heart Disease:",
    round(probabilities[1] * 100, 2), "%" # Converts probability into percentage and rounds to 2 decimal places
)

if probabilities[1] > probabilities[0]:  # Checks whether heart disease probability is higher
    print("\nResult: Higher probability of heart disease.")
else:  # Executes when no heart disease probability is higher or equal
    print("\nResult: Higher probability of no heart disease.")