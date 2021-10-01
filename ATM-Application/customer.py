from atm_card import ATMCard

class Customer:
    def __init__ (self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance