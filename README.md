# 🎓 Student Eligibility Dashboard

A simple Streamlit web app that checks a student's eligibility for the mid exam, final exam, and course certificate based on attendance and marks.

## Features

- Input **Attendance**, **Mid Exam Marks**, and **Final Exam Marks** (0–100%)
- Click **Check Eligibility** to see the result:
  - ✅ Certificate awarded if attendance, mid marks, and final marks are all ≥ 50%
  - ⚠️ Not eligible for final exam if mid marks < 50%
  - ❌ Not eligible for mid exam if attendance < 50%
  - ❌ No certificate if final marks < 50%
- Stats overview with pass/fail metrics and progress bars
- Custom blue theme

## Project Structure

```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Theme settings (blue primary color)
└── README.md                # This file
```

## Requirements

- Python 3.8 or higher

## Installation

1. Clone or download this project folder (make sure the `.streamlit` folder stays with `app.py`).
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the app with:

```bash
streamlit run app.py
```

This will open the dashboard automatically in your default web browser (usually at `http://localhost:8501`).

## Eligibility Rules

| Attendance | Mid Marks | Final Marks | Result                          |
|------------|-----------|-------------|----------------------------------|
| < 50%      | —         | —           | Not eligible for mid exam        |
| ≥ 50%      | < 50%     | —           | Not eligible for final exam      |
| ≥ 50%      | ≥ 50%     | < 50%       | No certificate                   |
| ≥ 50%      | ≥ 50%     | ≥ 50%       | 🎉 Certificate awarded           |

## Customization

- Change the theme color by editing `primaryColor` in `.streamlit/config.toml`.
- Adjust pass thresholds (currently 50%) directly in `app.py`.

## License

Free to use and modify for personal or educational purposes.
