from add import adde
from display import displa
from read import readdata
while True:
        a = readdata()
        print(f'''
{' '*70}____________________________________________                                     
{' '*70}[S.N.|    Menu                             ]
{' '*70}[════|═════════════════════════════════════]
{' '*70}[ 1  |    Display                          ]
{' '*70}[════|═════════════════════════════════════]
{' '*70}[ 2  |    Add                              ]
{' '*70}[════|═════════════════════════════════════]   
{' '*70}[ 3  |    Exit                             ]
{' '*70}[____|_____________________________________]
''')

        c = input(f'''
{' '*70}+____________________________________________ |
{' '*70}|Enter operation to be performed:             |
{' '*70}|____________________________________________ |
{' '*70}                   = ''')

        if c == "1":
            displa(a)
        elif c == "2":
            adde(a)
        elif c == "3":
            print("Exit.......")
            break
        else:
            print("Invalid choice, try again.")