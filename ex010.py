def how_much_paint_do_i_need(height, width, paint_liter_per_area):
  area = height * width
  return area/paint_liter_per_area

height = int(input('Tell me the height of your wall: '))
width = int(input('Tell me the width of your wall: '))
paint_liter_per_area = int(input('Tell me how much paint you use for 1m2 of wall: '))

print('You will need {}L of paint'.
      format(how_much_paint_do_i_need(height, width, paint_liter_per_area)))