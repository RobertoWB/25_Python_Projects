var1 = ' '
var2 = ' '
var3 = ' '
var4 = ' '
var5 = ' '
var6 = ' '
var7 = ' '
var8 = ' '
var9 = ' '

def gato():
    print('--------Tic Tac Toe:--------\n')
    contador = 0
    while contador != 9:
        contador += 1
        element = input('Write an X or O on the number to play on the chart: ')
        position = input('In what position wanna play (1 - 9): ')

        table(position, element)


def table(position, element_to_write):
    global var1, var2, var3, var4, var5, var6, var7, var8, var9
    stick = '|'
    dash = '-'
    space = ' '
    ex = 'X'
    oo = 'O'
    memoria = ''

    if element_to_write == 'x':
        option_on_chart = ex
    elif element_to_write == 'o':
        option_on_chart = oo
    
    if position == '1':
        var1 = option_on_chart
    elif position == '2':
        var2 = option_on_chart
    elif position == '3':
        var3 = option_on_chart
    elif position == '4':
        var4 = option_on_chart
    elif position == '5':
        var5 = option_on_chart
    elif position == '6':
        var6 = option_on_chart
    elif position == '7':
        var7 = option_on_chart
    elif position == '8':
        var8 = option_on_chart
    elif position == '9':
        var9 = option_on_chart
    
    memoria = ( var1 + space + stick + space + var2 + space + stick + space + var3 + '\n'+ dash*9 + '\n' + var4 + space + stick + space + var5 + space + stick + space + var6 + '\n'+ dash*9 + '\n' + var7 + space + stick + space + var8 + space + stick + space + var9)
    print(memoria)


gato()
