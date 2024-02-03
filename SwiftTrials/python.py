# 

import json
import requests

def format_classyfire_output(data):
    smiles = data.get("smiles", "")
    inchl_key = data.get("inchikey", "")
    superclass = data.get("superclass", {}).get("name", "")
    class_ = data.get("class", {}).get("name", "")
    subclass = data.get("subclass", {}).get("name", "")
    molecular_framework = data.get("molecular_framework", "")
    pathway = data.get("pathway", "")

    print(f"SMILES: {smiles}")
    print(f"InChIKey: {inchl_key}")
    print(f"Superclass: {superclass}")
    print(f"Class: {class_}")
    print(f"Subclass: {subclass}")
    print(f"Molecular Framework: {molecular_framework}")
    print(f"Pathway: {pathway}")

# Replace this with your actual SMILES string
your_smiles = "CC1COC(=O)O1"

base_url = "https://structure.gnps2.org/classyfire"
params = {"smiles": your_smiles}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception for bad requests
    data = response.json()

    format_classyfire_output(data)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
# import pandas as pd
# import requests

# def get_classyfire_info(smiles):
#     base_url = "https://structure.gnps2.org/classyfire"
#     params = {"smiles": smiles}

#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()  # Raise an exception for bad requests
#         data = response.json()

#         # Extract relevant information from the response
#         inchl_key = data.get("inchikey", "")
#         superclass = data.get("superclass", {}).get("name", "")
#         class_ = data.get("class", {}).get("name", "")
#         subclass = data.get("subclass", {}).get("name", "")
#         molecular_framework = data.get("molecular_framework", "")
#         pathway = data.get("pathway", "")

#         return inchl_key, superclass, class_, subclass, molecular_framework, pathway

#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return "", "", "", "", "", ""

# # Load CSV file into a DataFrame
# file_path = r"C:\Python\master_db.csv"  # Use a raw string or double backslashes
# try:
#     df = pd.read_csv(file_path)
# except FileNotFoundError:
#     print(f"Error: File not found at {file_path}")
#     exit(1)

# # Apply the ClassyFire API to each row in the DataFrame
# result = df["Canonical SMILES"].map(get_classyfire_info)

# # Create new columns with the extracted information
# df[["InChIKey", "Superclass", "Class", "Subclass", "Molecular Framework", "Pathway"]] = pd.DataFrame(result.tolist(), index=df.index)

# # Save the updated DataFrame to a new CSV file
# output_file_path = r"C:\Python\master_db.csv"  # Use a raw string or double backslashes
# df.to_csv(output_file_path, index=False)
