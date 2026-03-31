import pandas as pd
import os

FILE = "complaints.xlsx"

def create_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Roll", "Category", "Complaint", "Status"])
        df.to_excel(FILE, index=False)

def save_complaint(roll, category, complaint):
    create_file()
    df = pd.read_excel(FILE)

    new_data = pd.DataFrame({
        "Roll": [roll],
        "Category": [category],
        "Complaint": [complaint],
        "Status": ["Pending"]
    })

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(FILE, index=False)

def load_complaints():
    create_file()
    return pd.read_excel(FILE)

def update_status(index, status):
    df = pd.read_excel(FILE)
    df.loc[index, "Status"] = status
    df.to_excel(FILE, index=False)

def delete_complaint(index):
    df = pd.read_excel(FILE)
    df = df.drop(index)
    df.to_excel(FILE, index=False)
