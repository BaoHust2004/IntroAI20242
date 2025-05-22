import pandas as pd
import random

# Define the columns
columns = [
    "student_code", "school", "sex", "age", "address", "famsize", "Pstatus", 
    "Medu", "Fedu", "Mjob", "Fjob", "guardian", "traveltime", 
    "studytime", "failures", "schoolsup", "famsup", "paid", "activities", 
    "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", 
    "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"
]

# Define sample data for random generation
sample_data = {
    "school": ["GP", "MS"],
    "sex": ["F", "M"],
    "age": list(range(15, 22)),
    "address": ["U", "R"],
    "famsize": ["LE3", "GT3"],
    "Pstatus": ["T", "A"],
    "Medu": list(range(0, 5)),
    "Fedu": list(range(0, 5)),
    "Mjob": ["teacher", "health", "services", "at_home", "other"],
    "Fjob": ["teacher", "health", "services", "at_home", "other"],
    "reason": ["home", "reputation", "course", "other"],
    "guardian": ["mother", "father", "other"],
    "traveltime": list(range(1, 5)),
    "studytime": list(range(1, 5)),
    "failures": list(range(0, 4)),
    "schoolsup": ["yes", "no"],
    "famsup": ["yes", "no"],
    "paid": ["yes", "no"],
    "activities": ["yes", "no"],
    "nursery": ["yes", "no"],
    "higher": ["yes", "no"],
    "internet": ["yes", "no"],
    "romantic": ["yes", "no"],
    "famrel": list(range(1, 6)),
    "freetime": list(range(1, 6)),
    "goout": list(range(1, 6)),
    "Dalc": list(range(1, 6)),
    "Walc": list(range(1, 6)),
    "health": list(range(1, 6)),
    "absences": list(range(0, 5)),
    "G1": list(range(0, 21)),
    "G2": list(range(0, 21)),
    "G3": list(range(0, 21))
}

# Generate 100 rows of data
num_rows = 2000
data = []
for i in range(num_rows):
    row = [
        1000 + i  # student_code
    ] + [random.choice(sample_data[col]) for col in columns[1:]]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("student_data_train.csv", index=False)
print("✅ Dữ liệu đã được lưu vào file student_data_train.csv")
