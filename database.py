import pandas as pd
import os

FILE = "complaints.csv"

def create_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["ComplaintID", "Roll", "Category", "Complaint", "Status"])
        df.to_csv(FILE, index=False)

def save_complaint(roll, category, complaint):
    create_file()
    df = pd.read_csv(FILE)

    complaint_id = "C" + str(len(df) + 1)

    new_data = pd.DataFrame({
        "ComplaintID": [complaint_id],
        "Roll": [roll],
        "Category": [category],
        "Complaint": [complaint],
        "Status": ["Pending"]
    })

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE, index=False)

def load_complaints():
    create_file()
    return pd.read_csv(FILE)

def update_status(index, status):
    df = pd.read_csv(FILE)
    df.loc[index, "Status"] = status
    df.to_csv(FILE, index=False)

def delete_complaint(index):
    df = pd.read_csv(FILE)
    df = df.drop(index)
    df.to_csv(FILE, index=False)
