reta_1 = float(input('Diga um lado do triângulo (1/3)')) 
reta_2 = float(input('Diga um lado do triângulo (2/3)')) 
reta_3 = float(input('Diga um lado do triângulo (3/3)')) 

condition1 = reta_1 + reta_2 > reta_3
condition2 = reta_1 + reta_3 > reta_2
condition3 = reta_3 + reta_2 > reta_1

triangle = condition1 and condition2 and condition3

if(triangle):
  print('Nice triangle you\'ve got right there!')
else:
  print('It ain\'t no triangle')