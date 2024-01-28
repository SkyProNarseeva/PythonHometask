# def bank_app(X, Y):
#     interest_rate = 0.10  
#     total_amount = X  

#     for _ in range(Y):
#         total_amount = total_amount + (total_amount * interest_rate) 

#     return total_amount

# initial_deposit = int(input("Введите сумму первоначального взноса:"))
# years = int(input("Введите срок взноса:"))
# result = bank_app(initial_deposit, years)

# print(f"Сумма на счету после {years} лет: {result:.2f} рублей")

X = int(input("Сколько денег вкладываем? "))
Y= int(input("На сколько лет? "))
bank =  X + X * 0.1 * Y 
print(f"{bank}р. будет на счету пользователя спустя {Y} лет.")