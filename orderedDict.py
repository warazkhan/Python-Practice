#You are the manager of a supermarket.
#You have a list of  items together with their prices that consumers bought on a particular day.
#Your task is to print each item_name and net_price in order of its first occurrence.

#item_name = Name of the item.
#net_price = Quantity of the item sold multiplied by the price of each item.

from collections import OrderedDict

ordered_dict = {}

for _ in range(int(input())):

    itemsList = input().split()
    net_price = int(itemsList[-1])
    item_name = ' '.join(map(str, itemsList[:-1]))
    
    if item_name  in ordered_dict:
        ordered_dict[item_name] += net_price
    else:
        ordered_dict[item_name] = net_price

for key, value in ordered_dict.items(): 
    print(key, value)
  

