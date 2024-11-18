'''
def print_menu():
  s = Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60
  print(s)
def order_coffee():
  ct = -1 # ct means coffee_type
  order_dict = {}
  total_price = 0
  while ct != 0:
    ct = int(input('Coffee type: '))
    if 0<ct<=5:
      amount = int(input(f'Amount of {coffeeT[ct]}: '))
      total_price += amount * coffeeP[coffeeT[ct]]
      # print('DEBUG: total_price =', total_price)
      #if order_dict.get(coffeeT[ct], '') == '':
      if coffeeT[ct] not in order_dict:
        order_dict[coffeeT[ct]] = amount
      else:
        order_dict[coffeeT[ct]] += amount
  return order_dict, total_price
def change(total_price=450, pay=1000):
  ch = pay - total_price
  print(f'Customer\'s change: {ch}')
  b = [1000,500,100,50,20,10,5,1]
  for i in b:
    m = ch//i
    if m > 0:
      print(f'Change {i}: {m}')
      ch = ch%i
def print_receipt(order_dict={'Espresso':10, 'Americano':1}, customer_name='Toto', total_price=500):
  print('--------- receipt ---------')
  print('CPE36 COFFEE SHOP')
  print(f'Customer name: {customer_name}')
  for k in order_dict:
    print(f'{k} {order_dict[k]}, ', end='')
  print(f'{total_price} baht')
  print('Thank you')
  print('---------------------------')
def print_report(sales_dict={"Vichaiyut": 20450, "Emma": 250}):
  print('---- Daily Sale Report ----')
  total_sale = 0
  for i in sales_dict:
    print(f'{i} {sales_dict[i]} baht')
    total_sale += sales_dict[i]
  print(f'Total sale: {total_sale} baht')
  print('---------------------------')
coffeeP = {'Latte':40, 'Espresso': 45, 'Americano': 50, 'Mocca': 55, 'Cappuccino': 60}
coffeeT = {1:'Latte', 2:'Espresso', 3: 'Americano', 4: 'Mocca', 5: 'Cappuccino'}
## main begins here
sales_dict = {}
while True:
    print_menu()
    customer_name = input("Customer name: ")
    if customer_name == "end day":
        break
    orders_dict, total_price = order_coffee()
    if customer_name not in sales_dict:
        sales_dict[customer_name] = total_price
    else:
        sales_dict[customer_name] += total_price
    print(f'Total price: {total_price}')
    pay = int(input("Customer pay: "))
    change(total_price,pay)
    print_receipt(orders_dict, customer_name, total_price)
print_report(sales_dict)
'''
coffeeP = {'Latte':40, 'Espresso': 45, 'Americano': 50, 'Mocca': 55, 'Cappuccino': 60}
coffeeT = {1:'Latte', 2:'Espresso', 3: 'Americano', 4: 'Mocca', 5: 'Cappuccino'}
def print_menu():
  s = '''Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60'''
  print(s)
def order_coffee():
  total = 0
  order_dict = {}
  while True:
    ct = int(input('Coffee Type: '))
    if ct == 0:
      break
    elif 0<ct<=5:
      amount = int(input(f'Amount of {coffeeT[ct]}: '))
      total+=coffeeP[coffeeT[ct]]*amount
      if coffeeT[ct] not in order_dict:
        order_dict[coffeeT[ct]] = amount
      else:
        order_dict[coffeeT[ct]] += amount
  return order_dict,total
def change(total):
  print(f"total :{total}")
  pay = int(input("customer_pay: "))
  change=pay-total
  print(f'customerchange {change}')
  bank = [1000,500,100,50,20,10,5,1]
  for i in bank:
    m = (change)//i
    if m > 0:
      print(f'Change {i}: {m}')
      change= change%i

def receive(order_dict,total,customer_name):
  print('CPE36 COFFEE SHOP')
  print(f'Customer name: {customer_name}')
  for k in order_dict:
    print(f'{k} {order_dict[k]}, ', end='')
  print(f'{total} baht')
  print('Thank you')
  print('---------------------------')


print_menu()
customer_name = input('customername: ')
order_dict,total = order_coffee()

receive(order_dict, total, customer_name)