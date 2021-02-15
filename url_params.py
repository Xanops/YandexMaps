server = 'https://static-maps.yandex.ru/1.x/'
kords_x_1 = 110
kords_x_2 = 155
kords_y_1 = -13
kords_y_2 = -45
type_of_map = 'sat'
size = '450'
params = {
    "bbox": f'{kords_x_1},{kords_y_1}~{kords_x_2},{kords_y_2}',
    "l": type_of_map,
    'size': ",".join([size, size]),
}
