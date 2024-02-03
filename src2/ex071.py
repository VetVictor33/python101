def atm (amount: int):
  available_ballots = (50, 20, 10, 1)
  user_ballots = {
    50: 0, 20: 0, 10: 0, 1: 0}
  
  for ballot in available_ballots:
    result = withdraw(amount, ballot)
    used_ballots, remaining_amount = result
    amount = remaining_amount
    user_ballots[ballot] += used_ballots
  
  return user_ballots


def withdraw (amount: int, ballot: int):
  fifty_ballots = amount // ballot
  amount -= fifty_ballots * ballot
  return fifty_ballots, amount

amount_to_withdraw = int(input('Quanto vossa senhoria gostaria de sacar? R$'))
ballots_withdrew = atm(amount_to_withdraw)

print(f'Você sacou:', end=' ')
for ballot, ballot_amount in ballots_withdrew.items():
  if ballot_amount > 0:
    print(f'{ballot_amount} notas de R${ballot:.2f}', end=' ')