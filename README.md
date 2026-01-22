# Assignment 5 

## Test System
https://the-internet.herokuapp.com

## Tech Stack
- Python 3.11
- pytest
- Selenium WebDriver
- webdriver-manager
- Python logging
- pytest-html (HTML report)


## Installation & Execution

### 1. Install Python 3.11+
https://www.python.org/downloads/

### 2. Install Dependencies
```bash
pip install pytest selenium webdriver-manager pytest-html
```

### 3. Run All Tests
```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

### 4. Run Specific Test
```bash
python -m pytest tests/test_assignment5.py::test_login_valid -v
```

### 5. View HTML Report
After running tests, open: `reports/report.html`

## Test Cases

**TC-LOGIN-001**: Valid Login
- Navigate to login page
- Enter credentials: `tomsmith` / `SuperSecretPassword!`
- Verify success message appears

**TC-DOWNLOAD-001**: File Download
- Navigate to download page
- Click `SomeFile.txt` link
- Verify href ends with `/download/SomeFile.txt`
- File is downloaded to `downloads/` folder

**TC-ADDREMOVE-001**: Add/Remove Elements
- Navigate to add/remove elements page
- Click "Add Element" button → verify delete button appears
- Click "Delete" button → verify element removed

**TC-FORGOTPASS-001**: Forgot Password
- Navigate to forgot password page
- Enter email: `test@gmail.com`
- Click "Retrieve password"
- Verify confirmation message: "Your e-mail's been sent!"

## Logging & Artifacts

- **Logs**: `logs/test_execution.log` - detailed execution logs
- **Reports**: `reports/report.html` - HTML test report with results
- **Screenshots**: `screenshots/` - auto-captured on test failures
- **Downloads**: `downloads/` - downloaded test files during execution

## Features

 Automatic WebDriver management (webdriver-manager)
 Structured logging with timestamps
 HTML reports for test results
 Automatic screenshot capture on failure
 Proper fixture setup/teardown with pytest
 File download verification with folder monitoring
 Implicit waits for element detection
 Descriptive test naming (TC-XXX-001)
