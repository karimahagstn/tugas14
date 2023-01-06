#tugas14

print("======toko pakaian=====")

item= input('input item:')
price = float(input('input price item:'))
quantity= float(input('input quantity:'))
total_money = float(input('input total money:'))
return_money = total_money-quantity*price

#Note

teks = f'''
===========
    NOTA
===========

- item name :{item}
- item price :{price}
- item quantity :{quantity}
- total money :{total_money}
- total of change : IDR(return_money)
=======================
'''''
#open and make new file txt

file = open('biodata.txt','w')

#writing into file
file.write(teks)
