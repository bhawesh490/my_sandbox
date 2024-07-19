class BankAccount:
    apr = 1.2


print(BankAccount.__dict__)
# {'__module__': '__main__', 'apr': 1.2, '__dict__': <attribute '__dict__' of 'BankAccount' objects>, '__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, '__doc__': None}

print(type(BankAccount))
print(BankAccount)

acc_1 = BankAccount()
acc_2 = BankAccount()
print(acc_1 is acc_2)  # there are two different objects
print(acc_1.__dict__)  # empty namespace dict
print(acc_2.__dict__)  # empty namespace dict

# though there namespace dictionary is empty stil they have apr attributes coming from class attributes
print(acc_1.apr, acc_2.apr)
x = 1, 2
print(x)
print(*x)

# Since python is a dynamic we can add class attribute later also
BankAccount.account_type = "saving"
print(BankAccount.__dict__)
print(acc_1.account_type, acc_2.account_type)

acc_1.apr = 0
print(acc_1.__dict__)  # {'apr': 0}
print(acc_2.__dict__)  # {}
print(acc_1.apr, acc_2.apr)  # 0 1.2
# from account 1 we get values from instance namespace and from account 2 we get values from class namespace

setattr(acc_2, "apr", 0)
print(getattr(acc_2, "apr"))

acc_3 = BankAccount()
print(acc_3.apr)  # 1.2 we get this from class attributes
