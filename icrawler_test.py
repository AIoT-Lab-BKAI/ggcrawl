import os

from icrawler.builtin import GoogleImageCrawler
import multiprocessing
from multiprocessing import Process

from config import MAX_IMG

def _scene_text_crawler(keyword, max_img):
    img_folder = os.path.join('downloads', keyword)
    google_crawler = GoogleImageCrawler(storage={'root_dir': img_folder})
    try:
        google_crawler.crawl(keyword=keyword, max_num=max_img)
    except:
        print("Keyword failed: ", keyword)

num_cpu = multiprocessing.cpu_count()

with open('order.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

num_processes = num_cpu if num_cpu < len(lines) else len(lines)
print('num_processes: {}'.format(num_processes))

processes = []
for i in range(num_processes):
	process = Process(target=_scene_text_crawler, args=(lines[i], MAX_IMG))
	processes.append(process)

for process in processes:
	process.start()

for process in processes:
	process.join()
