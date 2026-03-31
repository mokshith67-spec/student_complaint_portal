import pandas as pd
import os

FILE = "complaints.xlsx"

def save_complaint(roll, category, complaint):
    data = {
        "Roll": [roll],
        "Category": [category],
        "Complaint": [complaint],
        "Status": ["Pending"]
    }

    df = pd.DataFrame(data)

    if os.path.exists(FILE):
        old = pd.read_excel(FILE)
        new = pd.concat([old, df], ignore_index=True)
        new.to_excel(FILE, index=False)
    else:
        df.to_excel(FILE, index=False)


def load_complaints():
    if os.path.exists(FILE):
        return pd.read_excel(FILE)
    else:
        return pd.DataFrame(columns=["Roll","Category","Complaint","Status"])


def update_status(index, status):
    df = pd.read_excel(FILE)
    df.loc[index, "Status"] = status
    df.to_excel(FILE, index=False)


def delete_complaint(index):
    df = pd.read_excel(FILE)
    df = df.drop(index)
    df.to_excel(FILE, index=False)
