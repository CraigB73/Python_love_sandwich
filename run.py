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

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data formthe last market.")
    print("Data should be six numbers, seperated by commas.")
    print("Example: 10,20,30,40,50,60\n")
    
    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    vaildate_data(sales_data)
    
def vaildate_data(values):
    """
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannont be converted into int,
    or if there aren't exactly 6 values
    """
    
    try:
        values = [eval(i) for i in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
        print(values)
       
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")    

get_sales_data()
    
    
    
    
"""
real world you would set up own api that connects to python
the company will use to enter in data/information  
"""
# csv format: comma sperated values(basic file type): a way for user to enter data using the teminal 
# uses the with_scope() method pass in SCOPE
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
