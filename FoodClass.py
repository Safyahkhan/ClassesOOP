class Customer:
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def get_customerid(self):
        return self.customerid

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def is_member(self):
        return self.member_status
  

class Transaction:
    def __init__(self, date, item_name, cost, customerid):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customerid = customerid

    def get_date(self):
        return self.date

    def get_item_name(self):
        return self.item_name

    def get_cost(self):
        return self.cost

    def get_customerid(self):
        return self.customerid


