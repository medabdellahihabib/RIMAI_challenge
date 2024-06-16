




# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=3 ' 
    

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4573',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-vitz-hodh-el-gharbi-aioun-4572',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-hilux-brakna-alaq-4571',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4565',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-camry-inchiri-akjoujt-4564',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-ist-hodh-ech-chargui-adel-bagrou-4560',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-aleg-4556'
# ]


# for annonce_url in annonce_urls:
#     download_images_from_annonce(annonce_url)




    
    
    
    
    

# # Fonction pour télécharger les images d'une annonce donnée
# def download_images_from_annonce(annonce_url):
#     # Obtenir le contenu de la page de l'annonce
#     response = requests.get(annonce_url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     photodiv = soup.find('div', id='slick-slide')

#     if slick-slide:
#         images = slick-slide.find_all('img')

#         for i, image in enumerate(images):
      
#             image_url = image['src']

#             if image_url.startswith('/'):
#                 image_url = urljoin(annonce_url, image_url)

#             image_response = requests.get(image_url)

            

#             sanitized_url = re.sub(r'[&*]', '_', annonce_url)
#             product_id = re.search(r'pdtid=(\d+)', annonce_url).group(1)

# # Use the product ID to name the file
#             with open(os.path.join('scrap', f'annonce_{product_id}_{i+1}.jpg'), 'wb') as f:

#                 f.write(image_response.content)

#         print(f"Les photos de l'annonce {annonce_url} ont été téléchargées et enregistrées dans le dossier 'scrap'.")
#     else:
#         print(f"Aucune image n'a été trouvée sur la page de l'annonce {annonce_url}.")    

# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=3'






# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4573',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-vitz-hodh-el-gharbi-aioun-4572',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-hilux-brakna-alaq-4571',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4565',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-camry-inchiri-akjoujt-4564',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-ist-hodh-ech-chargui-adel-bagrou-4560',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-aleg-4556'
# ]

# for annonce_url in annonce_urls:
#     download_images_from_annonce(annonce_url)


import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Fonction pour télécharger les images d'une annonce donnée
def download_images_from_annonce(annonce_url, annonce_id):
    # Créer le dossier 'scrap' s'il n'existe pas
    if not os.path.exists('scrap2'):
        os.makedirs('scrap2')

    # Obtenir le contenu de la page de l'annonce
    response = requests.get(annonce_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver toutes les balises <div> avec la classe 'slider-nav'
    slider_divs = soup.find_all('div', class_='slider-nav')

    if slider_divs:
        for slider_div in slider_divs:
            images = slider_div.find_all('img')
            for i, image in enumerate(images):
                image_url = image['src']

                if image_url.startswith('/'):
                    image_url = urljoin(annonce_url, image_url)

                image_response = requests.get(image_url)

                # Utiliser un nom unique basé sur l'index de l'image
                image_filename = f'annonce_{annonce_id}_{i+1}.jpg'

                # Enregistrer l'image dans le dossier 'scrap'
                with open(os.path.join('scrap2', image_filename), 'wb') as f:
                    f.write(image_response.content)

        print(f"Toutes les photos de l'annonce {annonce_url} ont été téléchargées et enregistrées dans le dossier 'scrap2'.")
    else:
        print(f"Aucune image n'a été trouvée sur la page de l'annonce {annonce_url}.")    

# main_url = 'https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=3'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4573',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-vitz-hodh-el-gharbi-aioun-4572',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-hilux-brakna-alaq-4571',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4565',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-camry-inchiri-akjoujt-4564',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-ist-hodh-ech-chargui-adel-bagrou-4560',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-aleg-4556'
# ]






# main_url = 'https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=4'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-allex-inchiri-akjoujt-4553',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-rav4-hudh-ash-sharqi-an-na-mah-4548',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-alaq-4547',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-highlander-brakna-aleg-4546',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-altezza-inchiri-akjoujt-4543',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-alaq-4540',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-aleg-4539',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-vista-inchiri-akjoujt-4538',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-rav4-brakna-aleg-4537',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-brakna-alaq-4534'
# ]




# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=10'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-mercedes-viano-nouakchott-ouest-nouakchott-4407',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-avensis-nouakchott-ouest-nouakchott-4406',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-peugeot-104-nouakchott-ouest-nouakchott-4405',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-4runner-nouakchott-ouest-nouakchott-4403',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-nouakchott-ouest-nouakchott-4399',
# ]

# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=11'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-ford-escape-nouakchott-ouest-nouakchott-4395',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-abarth-500-nouakchott-ouest-nouakchott-4391',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-hyundai-accent-nouakchott-ouest-nouakchott-4389',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-audi-q7-wilaya-du-trarza-tevragh-zeina-4369',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-chevrolet-equinox-nouakchott-ouest-nouakchott-4368'
# ]



# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=12'


# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-avensis-hodh-ech-chargui-adel-bagrou-4358',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4355',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4352',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4351',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-hilux-hodh-ech-chargui-adel-bagrou-4349'
# ]


# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=13'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-corolla-hodh-ech-chargui-adel-bagrou-4330',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-avensis-hodh-ech-chargui-adel-bagrou-4328',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-hyundai-tucson-hodh-ech-chargui-adel-bagrou-4327',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-avensis-nouakchott-ouest-nouakchott-4318',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-peugeot-807-nouakchott-ouest-nouakchott-4317',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-hyundai-elantra-nouakchott-ouest-nouakchott-4316'
# ]


# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=14'

# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-nissan-pathfinder-nouakchott-ouest-nouakchott-4312',
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-hyundai-elantra-nouakchott-ouest-nouakchott-4280'
# ]



# main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=15'


# annonce_urls = [
#     'https://www.automauritanie.com/fr/vehicle_listings/annonce-renault-megane-hodh-ech-chargui-adel-bagrou-4270'
# ]



main_url = ' https://www.automauritanie.com/fr/vehicle_listings?_=1714933731166&page=18'


annonce_urls = [
    'https://www.automauritanie.com/fr/vehicle_listings/annonce-citroen-ds3-nouakchott-ouest-nouakchott-4182',
    'https://www.automauritanie.com/fr/vehicle_listings/annonce-bmw-x5-nouakchott-ouest-nouakchott-4176',
    'https://www.automauritanie.com/fr/vehicle_listings/annonce-bmw-x3-nouakchott-ouest-nouakchott-4174',
    'https://www.automauritanie.com/fr/vehicle_listings/annonce-toyota-land-cruiser-nouakchott-ouest-nouakchott-4167',
    'https://www.automauritanie.com/fr/vehicle_listings/annonce-hyundai-elantra-nouakchott-ouest-nouakchott-4157'
]




for index, annonce_url in enumerate(annonce_urls, start=1):
    download_images_from_annonce(annonce_url, index)




