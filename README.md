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



