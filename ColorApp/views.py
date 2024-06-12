from django.shortcuts import render
import requests
from .forms import Color

def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def get_random_palette(request):
    url = "http://colormind.io/api/"
    data = {"model": "default"}
    response = requests.post(url, json=data)
    palette = response.json()["result"]
    print('PALETTE: %s' % palette)

    # Create a new palette with HEX and RGB values
    palette_with_hex = [{"rgb": color, "hex": rgb_to_hex(color[0], color[1], color[2])} for color in palette]

    return render(request, "ColorApp/colors_random.html", {"palette": palette_with_hex, "random": 'random'})

def index(request):
    # Fetch available models from Colormind API
    list_url = 'http://colormind.io/list/'
    response = requests.post(list_url)
    if response.status_code == 200:
        available_models = response.json()["result"]
    else:
        available_models = []

    # Fetch all colors from the database
    colors = Color.objects.all()
    return render(request, 'ColorApp/index.html', {'colors': colors, 'models': available_models})


def get_suggested_palette(request):
    import re

    if request.method == 'POST':
        colors = []
        for i in range(1, 6):
            color_value = request.POST.get(f'color{i}')
            if color_value and color_value != 'N':
                colors.append(color_value)

        # Convert color names to RGB
        input_colors = []
        for color in colors:
            if re.match(r'^#[A-Fa-f0-9]{6}$', color):
                # Convert hex to RGB
                rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                input_colors.append(rgb)
            else:
                return render(request, 'ColorApp/error.html')  # Handle invalid color input

        model = request.POST.get('model', 'default')

        # Request color palette from API
        url = 'http://colormind.io/api/'
        data = {"model": model, "input": input_colors}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            palette = response.json()["result"]
            palette_with_hex = [(rgb_to_hex(color[0], color[1], color[2]), color) for color in palette]

            return render(request, 'ColorApp/colors.html', {"palette": palette_with_hex, "model": model})
        else:
            return render(request, 'ColorApp/error.html')

    return render(request, 'ColorApp/index.html')
