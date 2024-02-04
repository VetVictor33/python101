math_expression = input('Digite a sua expressão matemática: ')

braces = math_expression.count('{') + math_expression.count('}')
parenthesis = math_expression.count('(') + math_expression.count(')')
brackets =  math_expression.count('[') + math_expression.count(']')

missing_braces = braces % 2 != 0
missing_parenthesis = parenthesis % 2 != 0
missing_brackets = brackets % 2 != 0


if missing_braces or missing_parenthesis or missing_brackets:
  print('Expressão inválida!', end =' ')
  message = 'Erro ao lidar com'
  if missing_parenthesis:
    message += ' parênteses'
  if missing_braces:
    message += ' chaves'
  if missing_brackets:
    message += ' colchetes'
  print(message, end='.')
else: 
    print('Expressão válida! Verifique a ordem dos elementos: (, {, [ ')
