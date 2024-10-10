<h3>Set up access to the Google Sheets API</h3>

<h4>Go to the Google Cloud Console and create a new project or select an existing project.</h4>
<h4>Go to the "API & Services" section and select "Enable APIs and Services".</h4>
 <h4>Search for Google Sheets API and enable it.</h4>
 <h4>Go to the "Credentials" section and select "Create Credentials".</h4>
 <h4>Select "Service account" and follow the creation steps. Finally, you will download a JSON file containing account service information.</h4>
 <h4>In the JSON file, find client_email and add it to your Google Sheets sharing settings (like a regular email).</h4>
 <h4>Access management: Make sure your email service account has access to Google Sheets. To do this, enter your Google Sheet and use the "Share" option and add the email in the JSON file.</h4>
 <h4>JSON file format: The JSON file should contain information about the private and public keys of your account service.</h4?
 <h4>Installing libraries: If you are using a Python virtual environment, make sure that the libraries are installed in the appropriate environment.</h4>

<h4>By following these steps, you can automatically import data into Google Sheets through Python.</h4>

<h4>Requirements:</h4>
<h4>pip install gspread google-auth</h4>
