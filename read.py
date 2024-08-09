def readdata():
    data = []
    try:
            file = open("write.txt", "r")
            for line in file:
                indexx = line.strip().split(", ")
                if len(indexx) >= 3:  
                    item, price, total = indexx[:3]  
                    info = {
                        "item": item,
                        "price":  price,
                        "total":  total
                    }
                    data.append(info)
            file.close()
            return data

    except FileNotFoundError:
        print("File not found read")