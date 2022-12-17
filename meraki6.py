# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry")

def icecream(*flavours):
    i=0
    while i<len(flavours):
        print("i love",flavours[i])
        i=i+1
icecream("chocolate", "butterscotch","vanilla","strawberry")        