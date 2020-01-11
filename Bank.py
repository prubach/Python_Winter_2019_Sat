class Customer():
    last_id = 0
    def __init__(self, imie, nazwisko):
        Customer.last_id += 1
        self.customer_id = Customer.last_id
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return 'Customer[{0},{1},{2}]'.format(self.customer_id, self.imie, self.nazwisko)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.customer = customer
        self.balance = 0

    def uznanie(self, kwota):
        self.balance += kwota

    def obciazenie(self, kwota):
        if kwota > self.balance:
            raise BankException('Brak srodkow na obciazenie, jest tylko {}'.format(self.balance))
        self.balance -= kwota

    def __str__(self):
        return "Account[{0},{1},{2}]".format(self.account_id, self.customer.nazwisko, self.balance)

class BankException(Exception):
    pass


c1 = Customer('Jan', 'Kowalski')
c2 = Customer('Anna', 'Malinowska')
a1 = Account(c1)
try:
    a1.uznanie(100)
    a1.obciazenie(160)
    a2 = Account(c2)
    print(a1)
    print(a2)
except BankException as be:
    print(be)


