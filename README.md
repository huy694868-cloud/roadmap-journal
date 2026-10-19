# Temperature Classifier
## Purpose
A program reads a temperature in degrees Celsius and classifies it.
## Requirements
Python 3 is required.
## How to run
Run the following command in the project directory:

```powershell
python temperature.py
```

Enter a numeric temperature when prompted.
## Classification rules
The valid temperature range is: -40°C to 125°C, inclusive.
- Cold: below 20°C within the valid range.
- Comfortable: From 20°C to 30°C within the valid range.
- Hot: Above 30°C within the valid range.
- Invalid: out of valid temperature range.
## Limitation
Entering non-numeric text, such as "abc", causes an error during conversation to float.
The program currently expects numeric input.