import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images_from_annonce(annonce_url, annonce_id):
    if not os.path.exists('scrap2'):
        os.makedirs('scrap2')

    response = requests.get(annonce_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    images = soup.select('div.images img')  # Sélectionne toutes les images à l'intérieur des div avec la classe 'images'
    if images:
        for i, image in enumerate(images[0:], start=0):  # Commence à partir de l'index 1 pour ignorer la première image
            image_url = image['src']

            if image_url.startswith('/'):
                image_url = urljoin(annonce_url, image_url)

            image_response = requests.get(image_url)
            image_filename = f'annonce_{annonce_id}_{i}.jpg'
            with open(os.path.join('scrap2', image_filename), 'wb') as f:
                f.write(image_response.content)

        print(f"Toutes les photos de l'annonce {annonce_url} ont été téléchargées et enregistrées dans le dossier 'scrap2'.")
    else:
        print(f"Aucune image n'a été trouvée sur la page de l'annonce {annonce_url}.")


main_url = 'http://www.wassit.info/automobile.html'

annonce_urls = ['http://www.wassit.info/annonces/12044.html', 
                'http://www.wassit.info/annonces/12022.html', 
                'http://www.wassit.info/annonces/11797.html', 
                'http://www.wassit.info/annonces/11779.html',
                'http://www.wassit.info/annonces/11703.html', 
                'http://www.wassit.info/annonces/11508.html', 
                'http://www.wassit.info/annonces/11251.html',
                'http://www.wassit.info/annonces/11087.html']
             


for index, annonce_url in enumerate(annonce_urls, start=1):
    download_images_from_annonce(annonce_url, index)






