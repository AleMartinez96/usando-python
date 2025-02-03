from io import BytesIO
from math import gcd
from PIL import Image
import requests

url: str = (
    "https://wallpapers.com/images/hd/1920x1080-aesthetic" "-glrfk0ntspz3tvxg.jpg"
)

try:
    respuesta: requests.Response = requests.get(url)
    imagen: Image.Image = Image.open(BytesIO(respuesta.content))
    ancho: float
    alto: float
    ancho, alto = imagen.size
    ratio = gcd(ancho, alto)
    print(f"{ancho // ratio}:{alto // ratio}")
except requests.RequestException as e:
    print(f"{e}")
except IOError as e:
    print(f"{e}")
