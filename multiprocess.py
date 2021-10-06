import multiprocessing
from multiprocessing import Process
from google_images_download import google_images_download

from config import MAX_IMG

def _scene_text_crawler(keyword, max_img):
    response = google_images_download.googleimagesdownload()
    arguments = {'keywords': keyword, 'limit': max_img}
    try:
        absolute_image_paths = response.download(arguments)
    except Exception as e:
        print(keyword)

num_cpu = multiprocessing.cpu_count()

with open('order.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

num_processes = num_cpu if num_cpu < len(lines) else len(lines)

processes = []
for i in range(num_processes):
	process = Process(target=_scene_text_crawler, args=(lines[i], MAX_IMG))
	processes.append(process)

for process in processes:
	process.start()

for process in processes:
	process.join()
