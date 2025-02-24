import requests
from requests.exceptions import ConnectionError
from typing import ByteString, Optional
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_cat_image() -> Optional[ByteString]:
    url = "https://cataas.com/cat"
    try:
        response = requests.get(url)
    except ConnectionError as e:
        logging.error("Holy moly the cat API is down!!!")
        return None
    return response.content


def save_image_to_disk(image: ByteString, filename: str) -> Optional[str]:
    with open(f"{filename}.jpg", 'wb') as file:
        file.write(image)