def displa(data):
    print(f"{' '*60}+{'-'*60}+")
    print(f"{' '*60}|   {'Item':<15}   | {'Price':<15}   | {'Total':<15}  |")
    for i in data:
              print(f"{' '*60}|{'-' * 60}|")
              a = i['item']
              b = i['price']
              c = i['total']
              print(f"{' '*60}|   {a:<15}   |    {b:<15}|   {c:<15}|")
    print(f"{' '*60}+{'-' * 60}+")


