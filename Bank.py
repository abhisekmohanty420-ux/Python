class Bank:

    def __init__(self,account_holder_name,account_number,branch,balance,accout_type):
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.branch=branch
        self.__balance=balance
        self.accout_type=accout_type
        
        self.__pin = None
        self.__withdrawal = 0
        self.__diposit = 0
    @property
    def get_pin(self):
        return self.__pin
    @property
    def get_balance(self):
        return self.__balance
    @property
    def get_withdraw(self):
        return self.__withdrawal
    @property
    def get_diposit(self):
        return self.__diposit
    @get_pin.setter
    def set_pin(self,pin):
        self.__pin=pin
    def diposit(self,amount):
        
        if amount<0:
            return "invalid diposits please valid amount"
        else:
            self.__diposit=amount
            self.__balance+=amount
    def withdraw_amount(self,amount):
        
        if  self.__balance <=0:
            return "insufficent balance"
        elif self.__balance<amount:
            return "insufficent balance"
        else:
            self.__withdrawal=amount
            self.__balance-=amount
            print("withdrawamount is ",amount ,"remain balance is", self.__balance)

    def get_account_holder(self):
        print("Account Holder Name is ",self.account_holder_name)

    def get_branch(self):
        print("Branch Name is ",self.branch)
    def get_accountType(self):
        print("Account type is ", self.accout_type)
    def get_accountnumber(self):
        print("Account number is ",self.account_number)
            
b1=Bank("Abhisek Mohanty",12345,"UditNagar",50000,"saving")
b1.set_pin=9692
print(b1.get_balance)
print(b1.get_branch())
print(b1.get_account_holder())
print(b1.get_accountType())
print(b1.get_accountnumber())

b1.diposit(2000)
print(b1.get_diposit)
print(b1.get_balance)
b1.withdraw_amount(10000)
print(b1.get_withdraw)
print(b1.get_balance)