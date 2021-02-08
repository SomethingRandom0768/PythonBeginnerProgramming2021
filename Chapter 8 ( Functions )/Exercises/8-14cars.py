

def make_car(manufacturer, model_name, **car_info):
    car_info['Manufacturer'] = manufacturer
    car_info['Model Name'] = model_name
    print(car_info)

car = make_car('subaru', 'outback', color='blue', tow_package=True)