# Google images crawler

## Prerequisites
Python 3.x

## Installation
```bash
git clone https://github.com/baoanh1310/ggcrawl
cd ggcrawl
pip install -r requirements.txt
```

## Crawling details
- Prepare list of keywords before crawling and list them in file **order.txt**
- Keywords that we used are listed in the file **keyword_list.txt**
### Crawling
```bash
python icrawler_test.py
```
### Merge download folders into one folder
```bash
python merge.py
```
All downloaded images will be copied to *merge_results* folder