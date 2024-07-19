class Bill:
    """
    this class contains information amount bills
    later this bill will be splitted
    """
    def __init__(self,amount,period):
        """this is constructor which is required 
        to instiate an object"""
        self.amount=amount
        self.period=period
        
class Flatmate:
    """
    creates a flatmate person who lives in the flat
    and pays a share of the bill
    """
    def __init__(self,name,days_in_house):
        self.name=name
        self.days_in_house=days_in_house

    def pays(self,bill,flatmate2):
        print("The bill is paid by, ",self.name,"and has paid for the period",self.days_in_house)
        amount=self.days_in_house/(self.days_in_house+flatmate2.days_in_house)*bill.amount
        return amount
