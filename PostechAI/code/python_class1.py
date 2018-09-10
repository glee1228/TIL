class Account:
    # 계좌의 속성(Attr)
    number = '0000-000-000000'
    balance = 0
    rate = 1.0

    # def __init__(self): Default 생성자
    def __init__(self, num='OOO-OOO-OOOOO', amnt=0, rate=1.0):
        self.number = num
        self.balance = amnt
        self.rate = rate
    # 계좌의 기능(Method)
    def deposit(self, money):  # 입금
        self.balance += money

    def withdraw(self, money):  # 인출
        self.balance -= money

    def obtain_interest(self):  # 이자 획득
        self.balance += self.balance * (self.rate / 100)

    def get_balance(self):
        return self.balance

    def set_balance(self, amnt):
        self.balance = amnt
    def transfer(self,another,amnt):
        self.balance -=amnt
        another.balance+=amnt
class MinBalanceAccount(Account): #Account 클래스를 상속받음
    def __init__(self, min_balance, num='OOOO-OOO-OOOOO',amnt=0, rate=1.0):
        Account.__init__(self, num=num, amnt=amnt,rate=rate)
        self.minimum_balance = min_balance
        self.bonus_rate = 1.0

acc1 = Account()
acc2 = Account()
acc3 = Account()


acc1= MinBalanceAccount(min_balance=0)
acc1.set_balance(500)
acc2= MinBalanceAccount(min_balance=0)
acc2.set_balance(1000)
acc1.transfer(acc2, 100) # acc1에서 acc2로 100원
print(acc1.get_balance()) # 400
print(acc2.get_balance()) # 1100