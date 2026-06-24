# 💳 Subscription Waste Detector

AI-Powered Subscription Tracking & Cost Optimization Tool built using Streamlit, Pandas, Plotly, and Groq AI.

## Overview

Subscription Waste Detector helps users identify recurring subscriptions, track monthly spending, receive renewal reminders, and generate AI-powered cost-saving recommendations.

The application analyzes bank statements, expense CSV files, or manually entered expenses to detect recurring payments and highlight potential subscription waste.

## Features

### Subscription Detection

* Detect recurring subscriptions automatically
* Identify monthly subscription costs
* Count subscription occurrences

### Expense Management

* Upload CSV files
* Upload Excel files
* Add manual expenses
* Categorize expenses

### Renewal Reminders

* Track renewal dates
* Display upcoming subscription renewals
* Prevent unexpected charges

### Analytics Dashboard

* Total monthly spending
* Active subscriptions count
* Possible savings estimation
* Interactive spending visualization

### AI Cost Optimization

* AI-generated spending analysis
* Cost-saving recommendations
* Subscription optimization suggestions
* Alternative service recommendations

### Report Generation

* Download subscription reports
* Export AI analysis
* Share spending summaries

---

## Tech Stack

Frontend:

* Streamlit

Data Processing:

* Pandas

Visualization:

* Plotly

AI Integration:

* Groq API

Language:

* Python

---

## Project Structure

subscription-waste-detector/

├── .streamlit/
│ └── secrets.toml

├── data/
│ └── sample_expenses.csv

├── utils/
│ ├── ai_helper.py
│ ├── detector.py
│ ├── manual_entry.py
│ ├── reminders.py
│ └── report_generator.py

├── app.py
├── requirements.txt
└── README.md

---

## Installation

### Clone Repository

git clone <repository-url>

cd subscription-waste-detector

### Install Dependencies

pip install -r requirements.txt

### Configure API Key

Create:

.streamlit/secrets.toml

Add:

GROQ_API_KEY = "your_api_key"

### Run Application

streamlit run app.py

---

## Sample Dataset Format

Date,Description,Amount,Category,RenewalDate

2026-01-05,Netflix,649,Video,2026-06-28

2026-01-10,Spotify,119,Music,2026-06-29

2026-01-15,ChatGPT,2000,Productivity,2026-07-15

---

## Future Enhancements

* PDF Report Export
* Email Renewal Notifications
* Budget Tracking
* Multi-User Support
* Historical Trend Analysis
* Mobile Responsive Dashboard

---

## Author

Developed as part of the AI Specialist BFSI Program.
