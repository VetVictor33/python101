def how_much_paint_do_i_need( paint_liter_per_area):
  wall_area = calc_area(height, width)
  return paint_liter_per_area * wall_area

def calc_area(height, width):
  return height * width

height = float(input('Tell me the height of your wall: '))
width = float(input('Tell me the width of your wall: '))
paint_liter_per_area = float(input('Tell me how much paint you use for 1m² of wall: '))

area = calc_area(height, width)
paint_amount = how_much_paint_do_i_need(paint_liter_per_area)

print(f'Your wall is {width}x{height}m and {area}m²')
print(f'You will need {paint_amount}L of paint')