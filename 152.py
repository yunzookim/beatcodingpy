colors = ['red', 'orange', 'blue', 'green', 'white', 'black', 'dark blue', 'purple']
col = input('Enter the color : ')
if col in colors :
    print('sorry')
else :
    colors.append(col)
    print(colors)