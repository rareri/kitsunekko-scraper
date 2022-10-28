import sys, os, bs4, requests

base_link = 'https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F'
anime = sys.argv[1]
anime_link = base_link + anime

os.makedirs(anime, exist_ok=True)

res = requests.get(anime_link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, 'lxml')
links = soup.select('a')
all_links = []
for link in links:
    link = link.get('href')
    if str(link).endswith(('.rar', '.7z', '.zip', '.ass', '.srt')):
        all_links.append(link)
         
        #Gets every the link for every file in the page

for file in all_links:
    file_link = 'https://kitsunekko.net/' + file
    res = requests.get(file_link)
    res.raise_for_status()
    sub_file = open(os.path.join(anime, os.path.basename(file)),'wb')
    for chunk in res.iter_content(100000):
        sub_file.write(chunk)

        #Downloads every file in a folder named after the given input, and located in the current working directory
 
    sub_file.close()
