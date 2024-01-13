def give_me_discount(old_price, discount_percentage):
  discount = old_price * (discount_percentage/100)
  return old_price - discount

old_price = float(input('Tell me the current prince: '))
discount = float(input('Tell me the percentage of discount: '))

new_price = give_me_discount(old_price, discount)

print(f'You will now pay only ${new_price:.2f}! \n Because your {discount:.0f}% of discount you\'re paying ${old_price - new_price:.2f} less')