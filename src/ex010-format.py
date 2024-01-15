money = float(input('How much $$$ do you have in your wallet? '))

def convert_to_berinjelas(money, berinjela_quotation):
  berinjelas = money / berinjela_quotation
  return berinjelas

berinjelas = convert_to_berinjelas(money, 3.33)

print(f'According to my calculations you have {berinjelas:.2f} berinjelas')