# OrangeHRM Selenium test

This folder contains a Selenium end-to-end test that logs in to the OrangeHRM demo, opens PIM, runs an employee search, and logs out.

## Run on Windows PowerShell

```powershell
cd C:\Users\udhaa\Downloads\selenium\orangehrm_e2e
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v test_orangehrm.py
```

Install Google Chrome first. Selenium Manager will locate or download a compatible ChromeDriver when the test starts.

Optional environment variables can override the demo settings:

```powershell
$env:ORANGEHRM_URL = "https://opensource-demo.orangehrmlive.com/"
$env:ORANGEHRM_USERNAME = "Admin"
$env:ORANGEHRM_PASSWORD = "admin123"
```
