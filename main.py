from flask import Flask, render_template, url_for
import random
import string
import os

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 9999)
    
    formatted_number = f"{random_number:04d}"

    image_folder = os.path.join(app.static_folder, 'cars')
    images = [f'cars/{file}' for file in os.listdir(image_folder) if file.endswith(('.jpg', '.png', '.jpeg'))]

    electric_cars_file = os.path.join(app.static_folder, 'electric_cars.txt')
    with open(electric_cars_file, 'r') as file:
        electric_cars = [line.strip() for line in file.readlines()]

    random_image = random.choice(images)

    is_electric = any(electric_car in random_image for electric_car in electric_cars)

    if is_electric:
        random_letter = random.choice(["EY", "EX"])
    else:
        random_letter = random.choice(["AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST", "UV", "WX", "YZ"])

    body_types_file = os.path.join(app.static_folder, 'body_types.txt')
    with open(body_types_file, 'r') as file:
        body_types = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in file.readlines()}

    car_body_type = "Unknown"
    car_model = "Unknown"
    for body_key, body_value in body_types.items():
        if body_key in random_image:
            car_body_type = body_value
            car_model = os.path.splitext(os.path.basename(random_image))[0].replace('_', ' ').title()
            break

    car_type = "Electric" if is_electric else "Regular"

    return render_template(
        "index.html",
        number=formatted_number,
        letters=random_letter,
        image=random_image,
        electric=is_electric,
        car_type=car_type,
        body_type=car_body_type,
        car_model=car_model
    )

if __name__ == '__main__':
    app.run(debug=True)