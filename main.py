import json


from pyautocad import Autocad, APoint


with open('arhip_output.json', 'r', encoding='utf-8') as file:
    coords = json.load(file)

acad = Autocad(create_if_not_exists=True)
# acad.prompt("Hello, Autocad from Python\n")
# start_x, start_y = coords['area_poins'][0]
# k = coords['area_pixel_scale_coef']
# for x ,y in coords['area_poins'][1:]:
#     acad.model.AddLine(APoint(start_x * k, start_y * k), APoint(x * k, y * k))
#     start_x, start_y = x, y

for c1 ,c2 in coords['sections_coordinates']:
    acad.model.Add
