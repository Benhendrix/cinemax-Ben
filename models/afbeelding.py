import requests
import io
from PIL import Image
from PIL.ImageTk import PhotoImage

def get_img_data(film_id, maxsize=(1200, 850), first=False, local=False):
    """Generate image data using PIL, with option local to choose between
       local file or image on the web
    """
    ENDPOINT = f"https://api.themoviedb.org/3/movie/{film_id}/images?api_key=56b70a17fca0d6f0cb706ca6e6882234&language=nl"
    if not local:
        img = Image.open(requests.get(ENDPOINT, stream=True).raw)
    else:
        img = Image.open(film_id)
    img.thumbnail(maxsize)
    if first:  # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return PhotoImage(img)