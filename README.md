# Roadmap Journal
My learning journal for Python and industrial AI.
## Requirements
- Python 3
- No third-party libraries are required.
## Programs
### 1. Temperature Classifier
File: `temperature.py`
Reads a temperature in degrees Celsius and classifies it.

Run:
```powershell
python temperature.py
```

Rules:
- Valid range: -40°C to 125°C, inclusive.
- Cold: below 20°C within the valid range.
- Comfortable: 20°C to 30°C, inclusive.
- Hot: above 30°C within the valid range.
- Invalid: outside the valid range.
### 2. Humidity Classifier
File: `humidity.py`
Reads a humidity percentage and classifies it.

Run:
```powershell
python humidity.py
```

Rules:
- Valid range: 0% to 100%, inclusive.
- Dry: below 30% within the valid range.
- Normal: 30% to 70%, inclusive.
- Humid: above 70% within the valid range.
- Invalid: outside the valid range.

## Limitation
Entering non-numeric text, such as "abc", causes an error during conversation to float.
The program currently expects numeric input.
## Learning journal
See `W01.md` for my learning notes and progress.