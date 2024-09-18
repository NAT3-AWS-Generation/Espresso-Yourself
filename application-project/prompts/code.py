#This displays the total shop inventory
shop_inventory = {"Books": {"1":"Malcolm X",
                             "2": 'Learn how to code for Dummies',
                               "3": 'Life of Pi',}
                  "Drinks": ['Latte', 'Coffee', 'Tea', 'Juice'],
                   "Food": ["Sandwich", "Pastry", "Salad", "Cookie"] }
 
 
#This function represents the main menu screen
def customer_menu() :
     print('1. Books')
     print('2. Food')
     print('3. Drink')
     print('3. Exit')

     user_input = input("Please could you type")
 
def employee_menu():
     return print('testing')
 
def main_menu():
     print('Welcome to Espresso Yourself.\nPlease select one of the following')
     print('1. Customer')
     print('2. Employee')
     print('3. Exit')
     user_input=input('Enter 1 for Customer and 2 for Employee:')
 
     if user_input == '1':
         customer_menu()
     elif user_input =='2':
         employee_menu()
     else:
         print('Goodbye')
 
main_menu()



