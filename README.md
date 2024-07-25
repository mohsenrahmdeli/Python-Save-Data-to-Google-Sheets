Set up access to the Google Sheets API

 Go to the Google Cloud Console and create a new project or select an existing project.
 Go to the "API & Services" section and select "Enable APIs and Services".
 Search for Google Sheets API and enable it.
 Go to the "Credentials" section and select "Create Credentials".
 Select "Service account" and follow the creation steps. Finally, you will download a JSON file containing account service information.
 In the JSON file, find client_email and add it to your Google Sheets sharing settings (like a regular email).
 Access management: Make sure your email service account has access to Google Sheets. To do this, enter your Google Sheet and use the "Share" option and add the email in the JSON file.
 JSON file format: The JSON file should contain information about the private and public keys of your account service.
 Installing libraries: If you are using a Python virtual environment, make sure that the libraries are installed in the appropriate environment.

By following these steps, you can automatically import data into Google Sheets through Python.

Requirements:
pip install gspread google-auth
