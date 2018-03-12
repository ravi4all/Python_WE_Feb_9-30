# Array of Object
# List of Dict
data = [
    {'product':'Apple','price':50000,'color':'White'},
    {'product':'Samsung','price':40000,'color':'Silver'},
    {'product':'Nokia','price':15000,'color':'Gray'},
    {'product':'Redmi','price':12000,'color':'White'}
]

for product in data:
    print(product['product'],",",product['price'], ",",product['color'])

# data[0]['product']