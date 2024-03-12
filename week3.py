price=input("Enter the price: ")
discount_percent=input("Enter the discount: ")

price=int(price)
discount_percent=int(discount_percent)

def calculate_discount(price, discount_percent):
    if discount_percent>20:
        discount_price=(discount_percent*price)/100
        new_price=price-discount_price
        return new_price
        
    else:
        print(price)
    
print(calculate_discount(price, discount_percent))    
