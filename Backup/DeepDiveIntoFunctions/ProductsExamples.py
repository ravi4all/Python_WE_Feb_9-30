products = [
    {'id':101,'name':'Apple','price':86000,'color':'silver'},
    {'id':102,'name':'Samsung','price':55000,'color':'gray'},
    {'id':103,'name':'Vivo','price':22000,'color':'white'},
    {'id':104,'name':'Apple','price':36000,'color':'silver'},
    {'id':105,'name':'Redmi','price':12000,'color':'silver'},
    {'id':106,'name':'Redmi','price':15000,'color':'black'},
    {'id':107,'name':'Vivo','price':18000,'color':'black'},
    {'id':108,'name':'Samsung','price':66500,'color':'silver'},
    {'id':109,'name':'Samsung','price':56500,'color':'white'},
    {'id':110,'name':'Apple','price':96000,'color':'gray'},
]

# search = list(filter(lambda n : n['name'] == 'Apple', products))
# print(search)

search = list(filter(lambda n : n['price'] < 20000, products))
# for data in search:
#     print(data)

# for each in products:
#     print(each['name'] == 'Apple')

# sorted_products = sorted(products, key=lambda n : n['name'])
sorted_products = sorted(products, key=lambda n : n['price'], reverse=True)
for data in sorted_products:
    print(data)