import gspread
from google.oauth2.service_account import Credentials
"""
The SCOPE lists the APIs that the program should access in order to run
SCOPE will not change so declare as a constant(all caps)
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
(.from_service_account_file) method from the Credentials that was imported 
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) #creates that client for the gspread
SHEET = GSPREAD_CLIENT.open("love_sandwiches") #Using client object that provides authorization

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)


# uses the with_scope() method pass in SCOPE
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
