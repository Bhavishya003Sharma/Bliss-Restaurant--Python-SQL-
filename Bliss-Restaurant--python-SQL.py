import mysql.connector as c
import random


print("(^-^)"*36)
print(" "*35,end=' ')
print("Welcome to the")
print(" "*39,end=' ')
print("BLISS")
print("(^-^)"*36)


con=c.connect(host="localhost",
              user="root",
              passwd="1234",
              )
cursor=con.cursor()

def initialize_database():
    c = con.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS bliss")
    con.database = "bliss" 
    
    create_table_login_query = '''
        CREATE TABLE IF NOT EXISTS login (
            Username VARCHAR(25) NOT NULL,
            Password VARCHAR(25) NOT NULL,
            User_Id VARCHAR(50) NOT NULL
        );
    '''
    create_table_signup_query = '''
        CREATE TABLE IF NOT EXISTS signup (
            Name VARCHAR(25) NOT NULL,
            Phone_Number VARCHAR(25) NOT NULL,
            Username VARCHAR(25) NOT NULL,
            Password VARCHAR(25) NOT NULL
        );
    '''
    create_table_orders_query = '''
    CREATE TABLE IF NOT EXISTS orders (
        Order_Id INT PRIMARY KEY AUTO_INCREMENT,
        User_Id VARCHAR(50),
        Items VARCHAR(255),
        Price VARCHAR(255),
        Order_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Total_Amount VARCHAR(255)
    );
'''

    
    c.execute(create_table_login_query)
    con.commit()
    
    c.execute(create_table_signup_query)
    con.commit()
    
    c.execute(create_table_orders_query)
    con.commit()
    
def menu():
    print("---------------------------------")
    print("|       Items             Price |")
    print("|-------------------------------|")
    print("|01. Cheese Pizza          99   |")
    print("|02. Tomato Pizza          99   |")
    print("|03. Aaloo Tikki Burger    99   |")
    print("|04. Cheese Burger         99   |")
    print("|05. Peri Peri Burger      99   |")
    print("|06. Pizza Burger          99   |")
    print("|07. Red Sauce Pasta       99   |")
    print("|08. White Sauce Pasta     99   |")
    print("|09. Cold Coffe            99   |")
    print("|10. Hot Coffe             99   |")
    print("|11. Cafe Mocha            99   |")
    print("|12. Mango Shake           99   |")
    print("|13. Banana Shake          99   |")
    print("|14. Chocolate Shake       99   |")
    print("|15. Lemon Mojito          99   |")
    print("|-------------------------------|")

    
def signup():
    name = input("Enter your name: ")
    phonenumber = input("Enter your phone number: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_id = random.randint(1000, 9999)
    sql1 = "INSERT INTO signup (name, phone_number, username, password) VALUES (%s, %s, %s, %s)"
    val1 = (name, phonenumber, username, password)
    sql2 = "INSERT INTO login  (username, password, user_id) VALUES (%s, %s, %s)"
    val2 = (username, password, user_id)
    cursor.execute(sql1, val1)
    cursor.execute(sql2, val2)
    con.commit()
    print("You have successfully signed up! Your user ID is:", user_id)
    return user_id


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    sql = "SELECT * FROM login WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        user_id = result[2]
        print("Login successful!")
        return user_id
    else:
        print("Invalid username or password.")
        return None

    
def user_interface(user_id):
    
    A = []
    
    while True:
        
        print("1. Menu")
        print("2. Cart")
        print("3. Log out ")
        choice = input("Enter your choice: ")

        if choice == "1":
            menu()
            item_choices = input("Enter item numbers separated by commas (e.g., 1,2,3): ")
            items_to_add = [int(item) for item in item_choices.split(",") if item.isdigit() and 1 <= int(item) <= 15]
            A.extend(items_to_add)
            print("Items added to cart!")

        elif choice == "2":
            
            if A==[]:
                print("Your cart is empty.")
                
            else:
                while True:
                    print("1. View Cart")
                    print("2. Edit Cart")
                    print("3. Place Order")
                    print("4. Exit")
                    cart_choice = input("Enter your choice: ")

                    if cart_choice == "1":
                        print("Your Cart:")
                        menu_items = {
                            1: "Cheese Pizza", 2: "Tomato Pizza", 3: "Aaloo Tikki Burger",
                            4: "Cheese Burger", 5: "Peri Peri Burger", 6: "Pizza Burger",
                            7: "Red Sauce Pasta", 8: "White Sauce Pasta", 9: "Cold Coffee",
                            10: "Hot Coffee", 11: "Cafe Mocha", 12: "Mango Shake",
                            13: "Banana Shake", 14: "Chocolate Shake", 15: "Lemon Mojito"
                            }  
                        items_list = [menu_items[item] for item in A] 
                        items_str = ', '.join(items_list)
                        print("Items in cart:", items_str)
                    elif cart_choice == "2":
                        while True:
                            print("1. Add Items")
                            print("2. Delete Items")
                            print("3. Exit")
                            edit_choice = input("Enter your choice: ")
                            if edit_choice == "1":
                                menu()
                                items_to_add = input("Enter item numbers to add, separated by commas: ")
                                items_to_add = [int(item) for item in items_to_add.split(",") if item.isdigit() and 1 <= int(item) <= 15]
                                A.extend(items_to_add)
                                print("Items added to cart!")
                            elif edit_choice == "2":
                                items_to_delete = input("Enter item numbers to delete, separated by commas: ")
                                items_to_delete = [int(item) for item in items_to_delete.split(",") if item.isdigit()]
                                for item in items_to_delete:
                                    if item in A:
                                        A.remove(item)
                                        print(f"Item {item} removed from cart.")
                                    else:
                                        print(f"Item {item} not found in cart.")
                            elif edit_choice == "3":
                                break
                            else:
                                print("Invalid choice")
                    elif cart_choice == "3":
                        if not A:
                            print("Your cart is empty. Add items before placing an order.")
                            continue
                        menu_items = {
                            1: "Cheese Pizza", 2: "Tomato Pizza", 3: "Aaloo Tikki Burger",
                            4: "Cheese Burger", 5: "Peri Peri Burger", 6: "Pizza Burger",
                            7: "Red Sauce Pasta", 8: "White Sauce Pasta", 9: "Cold Coffee",
                            10: "Hot Coffee", 11: "Cafe Mocha", 12: "Mango Shake",
                            13: "Banana Shake", 14: "Chocolate Shake", 15: "Lemon Mojito"
                            }

                        total_price = len(A) * 99  
                        items_list = [menu_items[item] for item in A] 
                        items_str = ', '.join(items_list)  
                        prices_str = ', '.join(['99' for _ in A])  

                        sql_insert_order = "INSERT INTO orders (user_id, items, Price, total_amount) VALUES (%s, %s, %s, %s)"
                        val_insert_order = (user_id, items_str, prices_str, total_price)
                        try:
                          cursor.execute(sql_insert_order, val_insert_order)
                          con.commit()
                        except Exception as e:
                          print("Internal Error:", e)

                        print("Order placed successfully!")
                        print("Items ordered:", items_str)
                        print("Total amount:", total_price)
                    elif cart_choice == "4":
                        break
                    else:
                        print("Invalid choice")
                        break
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice")
            break
        
def main():
    while True:
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = signup()
            user_interface(user_id)
        elif choice == "2":
            user_id = login()
            if user_id:
                user_interface(user_id)
            else:
                print("Login failed.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    initialize_database()
    main()
