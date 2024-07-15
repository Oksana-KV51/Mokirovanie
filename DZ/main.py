import requests


def get_random_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['url']
    return None


if __name__ == "__main__":
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        print("Вот случайно выбранная ссылка на изображение кошечки URL:", cat_image_url)
    else:
        print("Не удалось получить изображение кошки")
