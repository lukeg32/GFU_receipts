# get the three names their prices
# Calculate taxes
# display

WIDTH = 64 #must be even

######################################################################
#Get inputs                                                          #
######################################################################

tax_rate = float(input('Tax rate: '))

item1 = input('Item 1: ').upper()
item1_price = float(input('Item 1 price: '))

item2 = input('Item 2: ').upper()
item2_price = float(input('Item 2 price: '))

item3 = input('Item 3: ').upper()
item3_price = float(input('Item 3 price: '))

#debug mode
#tax_rate = .05

#item1 = 'nuke'.upper()
#item1_price = 123456789.05

#item2 = 'nike'.upper()
#item2_price = 100

#item3 = 'car'.upper()
#item3_price = 9999.99

######################################################################
#calculate numbers then format them                                  #
######################################################################

total = item1_price + item2_price + item3_price
tax = total * tax_rate
total += tax

item1_price = '$' + format(item1_price, '.2f')
item2_price = '$' + format(item2_price, '.2f')
item3_price = '$' + format(item3_price, '.2f')

tax = '$' + format(tax, '.2f')
total = '$' + format(total, '.2f')

######################################################################
# DISPLAY PORTION OF THE CODE                                        #
######################################################################

print("PURCHASE:")
print(WIDTH * '*')

width1 = WIDTH - len(item1) - len(item1_price)
print(item1 + (width1 * ' ') + item1_price)

width2 = WIDTH - len(item2) - len(item2_price)
print(item2 + (width2 * ' ') + item2_price)

width3 = WIDTH - len(item3) - len(item3_price)
print(item3 + (width3 * ' ') + item3_price)

print(WIDTH * ' ')
print(WIDTH * '*')

width_tax_front = int(WIDTH / 2) - len(' +%')
width_tax_end = int(WIDTH / 2) - len(tax) - len('TAX:')

print(' +%' + (width_tax_front * ' ') + "TAX:" + (width_tax_end * ' ') + tax)

width_total_front = int(WIDTH / 2) + 2
width_total_end = WIDTH - int((WIDTH / 2) + 2) - len('TOTAL:') - len(total)

print(width_total_front * ' ' + 'TOTAL:' + width_total_end * ' '+ total)

print(WIDTH * '*')