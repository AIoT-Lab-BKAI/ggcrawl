import os
import shutil

with open('draft.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.strip('\n') for line in lines]

dest_folder = 'before_crafting_imgs_gg'
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

wrong = 0
for i in range(len(lines)):
    imgs = os.listdir(os.path.join('downloads', lines[i]))
    sources = [os.path.join('downloads/{}'.format(lines[i]), img) for img in imgs]
    destinations = [os.path.join(dest_folder, str(i)+'_'+img) for img in imgs]
    for i in range(len(sources)):
        try:
            shutil.copyfile(sources[i], destinations[i])
        except:
            wrong += 1

print('Total images: ', len(os.listdir(dest_folder)))
print('Total wrong images: ', wrong)
