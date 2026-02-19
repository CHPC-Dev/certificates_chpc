# Winter School Certificate Generator

A lioghweight application for generating personalized certificates from an approved participant dataset.

Built with **Python**, **Streamlit**, and **Pillow**, the app verifies users against a CSV file, then dynamically places their name, date, and a unique serial number onto a certificate template and exports it as a PDF.

---

## Features

- Search participants by name or surname(Registered_with)  
- Verify identity using email + name(Registered_with)
- Generate certificates only for approved records  
- Place text precisely using pixel coordinates  
- Automatic date stamping  
- Unique serial number generation  
- Export certificates as PDF  
- Simple web interface using Streamlit  

---


## How It Works
1. User enters email and name/surname  
2. App verifies details against the CSV database  
3. If verified:
   - Full name is populated automatically  
   - User can edit display name if needed  
4. Certificate is generated:
   - Name placed at predefined coordinates  
   - Date added  
   - Unique serial number generated  
5. User downloads certificate as PDF  
---

## Usage

To test the app, the repo contains a **`test.csv`** file as an example. It should include the following columns:

> **Note:** The app is deployed on Streamlit Cloud and publicly accessible.  
> The repo includes the CSV for testing, but ensure any CSV you upload or use only contains publicly shareable information (to comply with privacy rules, e.g., POPIA).

- `first_name`
- `surname`
- `email`

Example:
[Open the live app](https://share.streamlit.io/<your-username>/<your-repo>/main/app.py)

| first_name | surname  | email                    |
|------------|---------|--------------------------|
| John        | Doe     | john@example.com   |

> **Tip:** To use your own dataset, upload a CSV file with the same columns (`first_name`, `surname`, `email`) and replace `test.csv` with your file name in the app directory. The app will read this CSV to verify records and generate certificates.


### 1. Matching Email and Name
When the user enters an **email and surname/first name** that exists in the CSV, the app verifies the record, enables the name field, and allows certificate generation.

<img width="400" height="370" alt="successful" src="https://github.com/user-attachments/assets/b8775b76-0ab9-4979-9ac9-561ef48ab5aa" />

The app checks both email and surname/first name. If a match is found, the **Name to appear on certificate** field is populated and active. The user can generate the certificate as PDF.

---

### 2. Non-Matching Email or Name
When the entered email or name does **not match** a record in the CSV, the verification fails.
<img width="400" height="370" alt="unsuccessful" src="https://github.com/user-attachments/assets/4fa7fa28-e56e-4798-8278-49efd84747bd" />

The app displays an error message: **“No matching record found.”** Certificate generation remains disabled until the user enters correct details.

---
## Running the App Locally

To run the Winter School Certificate Generator on your local machine:

1. **Clone the repository**

```bash
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>

python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt #install dependencies
```
## Place your CSV file

The repo includes a test.csv for testing.

To use your own dataset, upload a CSV with the same columns (first_name, surname, email) and replace test.csv.

```
streamlit run app.py
```



