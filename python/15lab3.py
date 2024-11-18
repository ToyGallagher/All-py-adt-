def discount_tuesday(adults_price:int,children_price:int) -> float:
    total_discount = (adults_price+children_price)25/100
    print(f"Tuesday discount 25% = ({adults_price} + {children_price}) x 25% = {total_discount:.2f}")
    return total_discount

def discount_wednesday(adults_price:int,children_price:int) -> float:
    total_discount = (adults_price+children_price)50/100
    addition_discount_chlidren = 0
    print(f"Wednesday discount 50% = ({adults_price} + {children_price}) x 50% = {total_discount:.2f}")
    if children_price >= 1000:
        addition_discount_chlidren = children_price20/100
        print(f"Wednesday children over 1000 discount 20% = {children_price} x 20% = {addition_discount_chlidren:.2f}")
    return total_discount + addition_discount_chlidren

total_adults = int(input("How many adults?: "))
total_children = int(input("How many children?: "))
inp_day = input("Day (su,mo,tu,we,th,fr,sa): ")

if inp_day in ("su","mo","tu","we","th","fr","sa"):
    adults_price = total_adults500
    children_price = total_children*250
    discount_price = 0

    print(f"{total_adults} adults = {total_adults}x500 = {adults_price}")
    print(f"{total_children} children = {total_children}x250 = {children_price}")

    if inp_day == "tu":
        discount_price = discount_tuesday(adults_price=adults_price,children_price=children_price)
    elif inp_day == "we":
        discount_price = discount_wednesday(adults_price=adults_price,children_price=children_price)
    total_price = adults_price+children_price-discount_price

    print(f"Total price is {total_price:.2f} Baht.")
else:
    print("Incorrect input!")