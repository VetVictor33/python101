def give_me_discount(old_price, discount_percentage):
  discount = old_price * (discount_percentage/100)
  return old_price - discount

old_price = int(input('Tell me the current prince: '))
discount = int(input('Tell me the percentage of discount: '))

new_price = give_me_discount(old_price, discount)

print('You will now pay only ${}! \n Because your {}% of discount you\'re paying ${} less'.
      format(new_price, discount, old_price - new_price))