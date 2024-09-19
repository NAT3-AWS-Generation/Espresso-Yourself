#This dictionary stores the entire shop inventory
#It's organized in categories with numbered items

shop_inventory = {"Books": {"1":"Malcolm X",
                             "2": 'Learn how to code for Dummies',
                               "3": 'Life of Pi',
                               "4":"Three body problem"},

                  "Drinks": {'1': 'Latte', 
                             '2': 'Coffee', 
                             '3': 'Tea', 
                             '4': 'Juice'},

                   "Foods": {'1': "Sandwich", 
                            '2': "Pastry", 
                            '3': "Salad", 
                            '4': "Cookie"}
                   }
 
#this class creates a customer and trolley functions to be accessed later in the code

class Customer:
     def __init__(self,name):
          self.name = name #stores the customer name
          self.trolley = [] #initializes an empty list to be used later by the customer class

     def add_to_trolley(self,item):
         self.trolley.append(item)
         print(f'{item} has been added to your trolley')

#This function represents the main menu screen for the customer

def customer_menu() :
     print(f"\n{customer_name.name} Hello! Have a look at our menu")
     print('1. Books')
     print('2. Foods')
     print('3. Drinks')
     print('4. View Trolley')
     print('5. Exit')
     user_input = input("\nPlease could you type your option. \n")
     
     # if statements handle user's choices

     if user_input == '1':
          inventory_menu("Books")
     elif user_input == '2':
          inventory_menu('Foods')
     elif user_input == '3':
          inventory_menu('Drinks')
     elif user_input == '4':
          print(customer_name.trolley)
          customer_menu()
     elif user_input == '5': 
          print(f'Thank you for shopping at Espresso Yourself,{customer_name}')
          main_menu()
     else: 
         print("invalid option")
         customer_menu()
         

# Function for the shopping trolley of the customer

def inventory_menu(trolley):
     print(f"\n{trolley.title()} in stock: ")
     for key, value in shop_inventory[trolley].items():
          print(f"{key}.{value}")
    
     choice = input("\nSelect from the number options: ")
     customer_name.add_to_trolley(shop_inventory[trolley][choice]) # Add selected item to trolley
     ''' 
     print(f'{customer_name.trolley} has been added to your trolley')
     print(customer_name.trolley)
     print(customer_name)
     '''
     customer_menu()   #to return to main menu after making your choice 
     
#This function represents the submenu to remove items for the employee

def remove_item():
     print("\nChoose a category to remove an item from: ")
     print("1. Books")
     print("2. Foods")
     print("3. Drinks")
     
     category_selection = input("\nSelect a category number: ")
     
     category = None
     if category_selection == "1":
          category = "Books"
     elif category_selection == "2":
          category = "Foods"
     elif category_selection == "3":
          category = "Drinks"
     else:
          print("Invalid choice")
          return
          
     print(f"\n{category} we have in stock: ")
     for key,value in shop_inventory[category].items():
          print(f"{key}.{value}")
          
     remove_selection = input("\nChoose the number of the item you wish to remove: " )
     if remove_selection in shop_inventory[category]:
          removed_item = shop_inventory[category].pop(remove_selection)
          print(f"{removed_item}  has been removed from the shop inventory.")
          main_menu()
     else:
          print("Invalid item number selected please try again. ")
          remove_item()
     

#This function represents the submenu to add items

def add_item():
     print("\nChoose a category to add an item from:")
     print("1. Books")
     print("2. Foods")
     print("3. Drinks")
     print("4. return")

     category = input("\nSelect a category number:\n")
     
     if category == '1':
          user_input =input('What would you like to add\n')
          last_key = list(shop_inventory['Books'])[-1]
          new_key = str(int(last_key) + 1)          
          shop_inventory['Books'][str(new_key)] = user_input
          print(f'{user_input} was added')
          print(shop_inventory['Books'])
          add_item()
     elif category == "2":
          user_input =input('What would you like to add\n')
          last_key = list(shop_inventory['Foods'])[-1]
          new_key = str(int(last_key) + 1)          
          shop_inventory['Foods'][str(new_key)] = user_input
          print(f'{user_input} was added')
          print(shop_inventory['Foods'])
          add_item()
     elif category == "3": 
          user_input =input('What would you like to add\n')
          last_key = list(shop_inventory['Drinks'])[-1]
          new_key = str(int(last_key) + 1)          
          shop_inventory['Drinks'][str(new_key)] = user_input
          print(f'{user_input} was added')
          print(shop_inventory['Drinks'])
          add_item()
     elif category == "4":
          employee_menu()
     else: 
          print("invalid selection")
          add_item()
     
          
               
# This function represents the employee menu

def employee_menu():
     print("\nEmployee Menu:")
     print('1. View Inventory')
     print('2. Remove Items from Inventory')
     print('3. Add Items to the Inventory')
     print("4. Exit")
     choice = input("\nPlease pick a number")
     
     if choice == '1':
          print(shop_inventory) #displays the shop inventory
          employee_menu() # returns to main menu to allow newer inputs
     elif choice == '2':
          remove_item() 
     elif choice == '3':
          add_item()
     else: 
          choice == '4'
          main_menu() #if invalid input returns to main menu


# This function displays the main menu screen of the cafe
customer_name = '' #creates an empty customer name string 
def main_menu():
     print('Welcome to Espresso Yourself.\nPlease select one of the following\n')
     print('1. Customer')
     print('2. Employee')
     print('3. Exit')
     user_input=input('\nEnter 1 for Customer and 2 for Employee: ')
 
     if user_input == '1':
        name=input('Please enter your name: ').lower()
        global customer_name #makes it so the customer name becomes a global variable that can be accessed by the inventory function
        customer_name = Customer (name)  # creates a customer object for the class       
        customer_menu()
     elif user_input =='2':
         employee_menu()
     else:
         print('Goodbye')


# start the cli interface by calling the main menu function
 
main_menu()



