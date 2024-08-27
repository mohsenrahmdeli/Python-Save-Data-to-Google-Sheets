import gspread
from google.oauth2.service_account import Credentials

# Replace 'path/to/your/credentials.json' with the path to the JSON file you downloaded
creds = Credentials.from_service_account_file('path/to/your/credentials.json')
client = gspread.authorize(creds)

# Open Google sheet using its name or URL
spreadsheet = client.open("Your Google Sheet Name")

# Select the desired sheet
worksheet = spreadsheet.sheet1  # Or you can use the name of the sheet: spreadsheet.worksheet('Sheet1')

# Add a new row
row = ["example@example.com", "valid"]  # Here you can enter the information you want
worksheet.append_row(row)
