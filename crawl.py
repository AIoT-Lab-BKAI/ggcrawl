from google_images_download import google_images_download

from config import MAX_IMG

def _scene_text_crawler(keyword, max_img):
    response = google_images_download.googleimagesdownload()
    arguments = {'keywords': keyword, 'limit': max_img}
    try:
        absolute_image_paths = response.download(arguments)
    except Exception as e:
        print(keyword)

def main():

    with open('order.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip('\n') for line in lines]

    for keyword in lines:
        _scene_text_crawler(keyword, MAX_IMG)

main()