#This displays the total shop inventory

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
 
class Customer:
     def __init__(self,name):
          self.name = name 
          self.trolley = []

     def add_to_trolley(self,item):
         self.trolley.append(item)
         print(f'{item} has been added to your trolley')

#This function represents the main menu screen

def customer_menu() :
     print(f"\n{customer_name.name} Hello! Have a look at our menu")
     print('1. Books')
     print('2. Foods')
     print('3. Drinks')
     print('4. View Trolley')
     print('5. Exit')
      
     user_input = input("\nPlease could you type your option. \n")
     
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
         
          
# shall we meet in group 3??yes yes

# shop_trolley = []

def inventory_menu(trolley):
     print(f"\n{trolley.title()} in stock:")
     for key, value in shop_inventory[trolley].items():
          print(f"{key}.{value}")
    
     choice = input("\nSelect from the number options: ")
     customer_name.add_to_trolley(shop_inventory[trolley][choice]) 
    #  print(f'{customer_name.trolley} has been added to your trolley')
    #  print(customer_name.trolley)
     #print(customer_name)
     customer_menu()   
     

 
def employee_menu():
     print("\nEmployee Menu:")
     print('1. View Inventory')
     print('2. Remove Items from Inventory')
     print('3. Add Items to the Inventory')
     print("4. Exit")
     return print('testing')


customer_name = ''
def main_menu():
     print('Welcome to Espresso Yourself.\nPlease select one of the following\n')
     print('1. Customer')
     print('2. Employee')
     print('3. Exit')
     user_input=input('\nEnter 1 for Customer and 2 for Employee: ')
 
     if user_input == '1':
        name=input('Please enter your name: ').lower()
        global customer_name
        customer_name = Customer (name)         
        customer_menu()
     elif user_input =='2':
         employee_menu()
     else:
         print('Goodbye')


 
main_menu()



