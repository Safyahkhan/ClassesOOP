import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0


customer_1 = fc.Customer(570,"Danni Sellyar","97 Mitchell Way Hewitt Texas 76712","dsellyarft@gmpg.org","254-555-9362",False) 

customer_2 = fc.Customer(569,"Aubree Himsworth","1172 Moulton Hill Waco Texas 76710","ahimsworthfs@list-manage.com","254-555-2273",True) 


transactions = []

for key in dict:
    date, item_name, cost, customerid = dict[key]
    transaction = fc.Transaction(date, item_name, cost, customerid)
    transactions.append(transaction)

for customer in [customer_1, customer_2]:
    print(f"Customer Name: {customer.get_name()}")
    print(f"Phone: {customer.get_phone()}")

    order_total = 0
    for transaction in transactions:
        if transaction.get_customerid() == customer.get_customerid():
            order_total += transaction.get_cost()
            print(f"Order Item: {transaction.get_item_name()} \t Price: ${transaction.get_cost():.2f}")

    if customer.is_member():
        member_discount = order_total * 0.2
        order_total *= 0.8
        print(f"Total Cost: ${order_total:.2f}")
        print("Member Discount: 20%")
        print(f"Total Cost after Discount: ${order_total - member_discount:.2f}")
    else:
        print(f"Total Cost: ${order_total:.2f}")

    print("\n")
