def adde(info):
    item =  input("Enter the name of the item")
    price = int(input("enter the price of the item"))
    li_ne = ""
    updated_info = []
    j = {}
    total = 0
    j['item'] = item
    j['price'] = price
    if info :
        print(True)
        for i in info:
            total = int(i['total']) + price
    else:
        total = price
    j['total'] = total
    updated_info.append(j)


    file = open('write.txt','a')
    for m in updated_info:
        line = f"{m['item']} , {m['price']}, {m['total']}\n"
        li_ne = li_ne + line
    file.write(li_ne)
    file.close()
