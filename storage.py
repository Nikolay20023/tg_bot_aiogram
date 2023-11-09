from typing import Optional


data = dict()


def add_link(
    telegram_id: int,
    link: str,
    tittle: str,
    description: str
):
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefault("links", dict())
    data[telegram_id]["links"][link] = {
        "title": tittle,
        "description": description
    }


def add_photo(
    telegram_id: int,
    photo_file_id: int,
    photo_unique_id: str
):
    data.setdefault(telegram_id, dict())
    data[telegram_id].setdefault("images", [])
    if photo_file_id not in data[telegram_id]["images"]:
        data[telegram_id]["images"].append((photo_file_id,  photo_unique_id))


def get_links_by_id(telegram_id: int) -> dict:
    if telegram_id in data and "links" in data[telegram_id]:
        return data[telegram_id]["links"]
    
    return dict()


def get_images_by_id(telegram_id: int) -> dict:
    if telegram_id in data and "images" in data[telegram_id]:
        return [item[0] for item in data[telegram_id]["images"]] 
    
    return []


def delete_link(telegram_id, link: str):

    if telegram_id in data:
        if "links" in data[telegram_id]:
            if link in data[telegram_id]["links"]:
                del data[telegram_id]["links"][link]


def delete_images(telegram_id: int, photo_file_unique_id: int):
    if telegram_id in data:
        for index, (_, unique_id) in enumerate(data[telegram_id]["images"]):
            if unique_id == photo_file_unique_id:
                data[telegram_id]["images"].pop(index)



