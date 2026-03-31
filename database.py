import pandas as pd
import os

FILE = "complaints.csv"

def save_complaint(name, roll, complaint_type, priority, complaint):
    data = {
        "Name": [name],
        "Roll": [roll],
        "Type": [complaint_type],
        "Priority": [priority],
        "Complaint": [complaint],
        "Status": ["Pending"]
    }

    df = pd.DataFrame(data)

    if os.path.exists(FILE):
        df.to_csv(FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE, index=False)


def load_complaints():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    else:
        return pd.DataFrame(columns=["Name","Roll","Type","Priority","Complaint","Status"])
