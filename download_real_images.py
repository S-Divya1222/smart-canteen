import os
import requests

os.makedirs("media/food", exist_ok=True)

images = {
    "idli.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Idli_Sambar.JPG",
    "masala_dosa.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Masala_Dosa.JPG",
    "chicken_biriyani.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Chicken_Biryani.jpg",
}

for filename, url in images.items():
    path = os.path.join("media", "food", filename)

    try:
        response = requests.get(url, timeout=20)

        if response.status_code == 200:
            with open(path, "wb") as file:
                file.write(response.content)

            print("DONE:", filename)
        else:
            print("FAILED:", filename, response.status_code)

    except Exception as e:
        print("ERROR:", filename, e)

print("\nFinished.")