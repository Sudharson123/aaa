r=str(input('Enter the Row number:'))
c=str(input('Enter the Column number:'))

rows=6
columns=6
while r.isdigit()==False or c.isdigit()==False or int(r) not in range(rows) or int(c) not in range(columns):
        print('enter digits in range')
        r = str(input('Enter the Row number:'))
        c = str(input('Enter the Column number:'))
        rows = 6
        columns = 6
        continue
 print('tats it')



