import requests

# Fetch available models
list_url = 'http://colormind.io/list/'
response = requests.post(list_url)
if response.status_code == 200:
    available_models = response.json()["result"]
    print("Supported Models:", available_models)

    # Fetch color palettes for each model
    api_url = 'http://colormind.io/api/'
    for model in available_models:
        data = {"model": model}
        palette_response = requests.post(api_url, json=data)
        if palette_response.status_code == 200:
            palette = palette_response.json()["result"]
            print(f"{model} palette: {palette}")
        else:
            print(f"Failed to fetch palette for model {model}")
else:
    print("Failed to fetch models")
