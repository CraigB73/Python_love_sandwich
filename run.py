import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the termina, which must be a string of 6 numbers separated by commas.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        #printed instructions to the users
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your sales data here: ")   
        sales_data = data_str.split(",") #Removes the commas(CSV) from user typed input
        
        if vaildate_data(sales_data):
            print("Data is vaild!")
            break
        
    return sales_data


def vaildate_data(values):
    """
    Inside the try, converts all string values into intergers.
    Raises ValueError if strings cannont be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        [int(value) for value in values] # check that converts string to integers:(for loop returns int(value)). Ensures that no strings can be entered (ex:'four') by the user
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True 

def update_worksheet(data, worksheet): # Need to pass in data as a paramenter
    """
    Update worksheets, add new row with the provided data.
    """
    print(f"Updating {worksheet} worksheet...\n")
    sales_worksheet = SHEET.worksheet(worksheet) # Access worksheet(Tab) from google sheets using the SHEET variable declared at top of the page that access the spreadsheet
    sales_worksheet.append_row(data) # google append_row method that adds data to new row 
    print(f"{worksheet} worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste and desposed of.
    - Negative surplus indicates extra made when stock was sold out.
    """
    
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    # stock_row = SHEET.worksheets(stock) # This will get a list of all rows and values in the worksheet
    stock_row = stock[-1]
  
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row): # using built-in zip() method: unpacks stock_row and sales_row to be use in an expession to get surplus data
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data

    
def get_stock_data():
    """
    Update surplus worksheet, add new row with each item total.
    """
    data_str = input("Enter stock data here: ")   
    stock_data = data_str.split(",") #Removes the commas(CSV) from user typed input
        
    if stock_data:
        vaildate_data(stock_data) 
        print("Data is vaild!")
    
    return stock_data

def get_last_5_entries_sales():
    """
    Collects collumns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """ 
    
    sales = SHEET.worksheet('sales')
    # column = sales.col_values(3) #Grabs the data from column three ('chicken salad)
    
    columns = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns.append(column[-5:])# column[-5:] is a slice the ":" the want to slice multiple values from the list
    return columns 
        
    
    
def main(): # Good practice to have a main funtion to run all functions 
    """
    Run all program function
    """   
    data = get_sales_data()
    print(data)
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    new_stock_data = get_stock_data()
    update_worksheet(new_stock_data, "stock")
    
print("Welcome to Love Sandwiches Data Automation")
#main()
sales_columns = get_last_5_entries_sales()


    
    
    
    
"""
real world you would set up own api that connects to python
the company will use to enter in data/information  
"""
# csv format: comma sperated values(basic file type): a way for user to enter data using the teminal 
# uses the with_scope() method pass in SCOPE
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
