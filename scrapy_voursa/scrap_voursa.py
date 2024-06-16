import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import re
import os

# Créer un dossier pour enregistrer les images
if not os.path.exists('photos6'):
    os.makedirs('photos6')

# Fonction pour télécharger les images d'une annonce donnée
def download_images_from_annonce(annonce_url):
    # Obtenir le contenu de la page de l'annonce
    response = requests.get(annonce_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver la balise div avec l'identifiant 'photodiv' qui contient les images
    photodiv = soup.find('div', id='photodiv')

    # Vérifier si la balise 'photodiv' existe
    if photodiv:
        # Trouver toutes les balises 'img' dans 'photodiv'
        images = photodiv.find_all('img')

        # Parcourir chaque image et télécharger
        for i, image in enumerate(images):
            # Obtenir l'URL de l'image
            image_url = image['src']

            # Si l'URL commence par '/', ajouter le domaine au début
            if image_url.startswith('/'):
                image_url = urljoin(annonce_url, image_url)

            # Télécharger l'image
            image_response = requests.get(image_url)

            

# Sanitize the URL for file name
            sanitized_url = re.sub(r'[&*]', '_', annonce_url)
            product_id = re.search(r'pdtid=(\d+)', annonce_url).group(1)

# Use the product ID to name the file
            with open(os.path.join('photos6', f'annonce_{product_id}_{i+1}.jpg'), 'wb') as f:

                f.write(image_response.content)

        print(f"Les photos de l'annonce {annonce_url} ont été téléchargées et enregistrées dans le dossier 'photos'.")
    else:
        print(f"Aucune image n'a été trouvée sur la page de l'annonce {annonce_url}.")



# main_url = 'https://www.voursa.com/Index.cfm?PN=2&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=334597&adtre=Toyota%20Corolla%20%C3%A0%20vendre',
#     'https://www.voursa.com/annonces.cfm?pdtid=330967&adtre=Citroen(peugot)',
#     'https://www.voursa.com/annonces.cfm?pdtid=334426&adtre=Acura%20RDX%20Sport%20full%20option',
#     'https://www.voursa.com/annonces.cfm?pdtid=332354&adtre=Corola',
#     'https://www.voursa.com/annonces.cfm?pdtid=318229&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=333257&adtre=Mercedes%20300%20d%C3%A9douan%C3%A9%20%C3%A0%20vendre',
#     'https://www.voursa.com/annonces.cfm?pdtid=332096&adtre=%D9%87%D9%88%D9%86%D8%AF%D8%A7%D9%8A%20%D9%85%D8%B2%D8%A7%D9%84%D8%AA%20%D9%86%D8%B8%D9%8A%D9%81',
#     'https://www.voursa.com/annonces.cfm?pdtid=291483&adtre=Toyota%20Rav%204%202015%20boite%20manuelle',
#     'https://www.voursa.com/annonces.cfm?pdtid=327424&adtre=%D9%81%D8%B1%D8%B5%D8%A9%20%D8%AD%D9%82%D9%8A%D9%82%D9%8A%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=293501&adtre=Corola%202010',
#     'https://www.voursa.com/annonces.cfm?pdtid=332563&adtre=%D8%A8%D8%B1%D9%84%D9%8A%D9%86%D9%83%D9%88%20%D9%86%D8%B8%D9%8A%D9%81',
#     'https://www.voursa.com/annonces.cfm?pdtid=332101&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=331709&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%20%D9%85%D8%A7%D9%81%D8%A7%D8%AA%20%D8%A7%D8%B1%D9%82%D9%85%D8%AA',
#     'https://www.voursa.com/annonces.cfm?pdtid=330501&adtre=Peugeot%203008',
#     'https://www.voursa.com/annonces.cfm?pdtid=331146&adtre=Toyota%20avensis%20%20atica%20%D9%85%D9%84%D9%81%D9%87%20%D9%81%D9%8A%D9%87%20%D9%86%D9%87%D8%A7%D8%B1%20%D9%88%D8%A7%D8%AD%D8%AF%20%D8%AC%D8%AF%D9%8A%D8%AF',
#     'https://www.voursa.com/annonces.cfm?pdtid=331499&adtre=BMW%20deux%20portes%20%C3%A0%20vendre',
#     'https://www.voursa.com/annonces.cfm?pdtid=331247&adtre=Hyundai%20Elantra%202017%20en%20bon%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=330921&adtre=TOYOTA%20COROLLA%20(DROGBA)',
#     'https://www.voursa.com/annonces.cfm?pdtid=324656&adtre=vendre%20ou%20%C3%A9changer%20corolla%202012%20%D8%A7%D9%84%D8%B3%D8%B9%D8%B1%20%D8%BA%D9%8A%D8%B1%20%D9%82%D8%A7%D8%A8%D9%84%20%D9%84%D9%86%D9%82%D8%A7%D8%B4',
#     'https://www.voursa.com/annonces.cfm?pdtid=330157&adtre=Nissan%20Juke',
#     'https://www.voursa.com/annonces.cfm?pdtid=243588&adtre=Corolla%202018%20bonne%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=327017&adtre=SE%202020',
#     'https://www.voursa.com/annonces.cfm?pdtid=327565&adtre=Hyundai%20petite'
#     'https://www.voursa.com/annonces.cfm?pdtid=327848&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%B1%D8%A7%D9%81%204%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%D9%87%20%D8%AA%D9%86%D8%A8%D8%A7%D8%B9%20%D9%85%D8%A7%D9%87%D9%8A%20%D9%88%D8%A7%D8%B9%D8%B1%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=327833&adtre=%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%20%D8%A8%D9%8A%D9%83%D8%A7%D9%85%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9'
# ]
 
# main_url = ' https://www.voursa.com/Index.cfm?PN=3&gct=1&sct=11&gv=13 '

# annonce_urls = [
#     "https://www.voursa.com/annonces.cfm?pdtid=300088&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202014%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9",
#     "https://www.voursa.com/annonces.cfm?pdtid=326102&adtre=mercedes%20190d%20%20dedouaner",
#     "https://www.voursa.com/annonces.cfm?pdtid=325461&adtre=Vente%20de%20voiture",
#     "https://www.voursa.com/annonces.cfm?pdtid=324352&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%B3%D9%8A%D9%84%D9%81%D9%8A%D8%B1%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%D8%A9%20%D9%85%D8%A8%D9%8A%D9%88%D8%B9%D8%A9%20%D9%86%D8%A7%D9%87%D9%8A%20%D9%88%D8%A7%D8%B9%D8%B1%D8%A9",
#     "https://www.voursa.com/annonces.cfm?pdtid=324314&adtre=vendre%20ou%20%C3%A9changer%20Peugeot%203008",
#     "https://www.voursa.com/annonces.cfm?pdtid=323748&adtre=Toyota%20Corolla%20verso",
#     "https://www.voursa.com/annonces.cfm?pdtid=322924&adtre=Tx%202012%20%D8%B3%D9%8A%D8%A7%D8%B1%D9%87%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9",
#     "https://www.voursa.com/annonces.cfm?pdtid=317132&adtre=voiture%20avensis%20D-4d%20occasion",
#     "https://www.voursa.com/annonces.cfm?pdtid=321330&adtre=Toyota%20Corolla%202013",
#     "https://www.voursa.com/annonces.cfm?pdtid=291058&adtre=Toyota%20Rav4%20D-Cat%20manuelle",
#     "https://www.voursa.com/annonces.cfm?pdtid=296381&adtre=Mekinetheu%20zeyneu%20w%20suspension%20bekmeu",
#     "https://www.voursa.com/annonces.cfm?pdtid=316179&adtre=Mercedes%20190E%20Arrivage",
#     "https://www.voursa.com/annonces.cfm?pdtid=291480&adtre=Toyota%20Rav4%202005%20%20manuelle",
#     "https://www.voursa.com/annonces.cfm?pdtid=315900&adtre=Toyota%20Prado%202008%20en%20bon%20%C3%A9tat"
# ]


# main_url = 'https://www.voursa.com/Index.cfm?gct=1&sct=11&gv=13'
# """ annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=336203&adtre=بيع%20سيارة%20vx%20نظيفة',
#     'https://www.voursa.com/annonces.cfm?pdtid=313763&adtre=Rav4%20model%202015%20diesel%20Manuel%204*4%20%20push%20start%20voursa',
#     'https://www.voursa.com/annonces.cfm?pdtid=334596&adtre=Range%20Rover%202015%20na4ive%20gasoil%20automatique%20mebyo2a%20hwe',
#     'https://www.voursa.com/annonces.cfm?pdtid=337636&adtre=Jeep%20Cherokee%20latitude%202015',
#     'https://www.voursa.com/annonces.cfm?pdtid=337597&adtre=Corolla%20Drogba%202005',
#     'https://www.voursa.com/annonces.cfm?pdtid=336572&adtre=Toyota%20rav%204%202012',
#     'https://www.voursa.com/annonces.cfm?pdtid=337628&adtre=هيونداي%20اوتوماتيك%202014%20،ستار%20،كيصها%20فيه%20تعدال%20شوي'
#     'https://www.voursa.com/annonces.cfm?pdtid=336203&adtre=%D8%A8%D9%8A%D8%B9%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20vx%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=313763&adtre=Rav4%20model%202015%20diesel%20Manuel%204*4%20push%20start%20voursa',
#     'https://www.voursa.com/annonces.cfm?pdtid=334596&adtre=Range%20Rover%202015%20na4ive%20gasoil%20automatique%20mebyo2a%20hwe',
#     'https://www.voursa.com/annonces.cfm?pdtid=337636&adtre=Jeep%20Cherokee%20latitude%202015',
#     'https://www.voursa.com/annonces.cfm?pdtid=337597&adtre=Corolla%20Drogba%202005',
#     'https://www.voursa.com/annonces.cfm?pdtid=336572&adtre=Toyota%20rav%204%202012',

#     'https://www.voursa.com/annonces.cfm?pdtid=337629&adtre=اكسنت%20ما%20كط%20نسبقت%20مانيل%20نظيفة%20مزالت',
#     'https://www.voursa.com/annonces.cfm?pdtid=337629&adtre=%D8%A7%D9%83%D8%B3%D9%86%D8%AA%20%D9%85%D8%A7%20%D8%AE%D8%B7%20%D8%AA%D8%B3%D8%A8%D9%82%D8%AA%20%D9%85%D8%A7%D9%86%D9%8A%D9%84%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9%20%D9%85%D8%B2%D8%A7%D9%84%D8%AA',

#     'https://www.voursa.com/annonces.cfm?pdtid=336087&adtre=Accent%20gasoil%20en%20bon%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=337515&adtre=Range%20Rover%202014',
#     'https://www.voursa.com/annonces.cfm?pdtid=335777&adtre=Nissan%20Almera%202014%20Bo%C3%AEte%20automatique%20Essence',
#     'https://www.voursa.com/annonces.cfm?pdtid=337445&adtre=%D9%87%D9%8A%D9%88%D9%86%D8%AF%D8%A7%D9%8A%202014%20%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%D9%8A%D9%83%20%D9%85%D9%83%D9%8A%D9%86%D8%A9%20%D9%88%D8%A8%D9%88%D8%A7%D8%AA%20%D9%85%D8%A7%D9%83%D8%B7%20%D9%85%D8%AA%D8%B3%D9%88',
#     'https://www.voursa.com/annonces.cfm?pdtid=335983&adtre=Toyota%20Corolla%20LE%20Manuelle%20en%20EXCELLENTE%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=337474&adtre=GMC%20neuf%20et%20en%20bon%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=335171&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%',
# ] """

# main_url = ' https://www.voursa.com/Index.cfm?PN=4&gct=1&sct=11&gv=13 '

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=313518&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%86%D8%B6%D9%8A%D9%81%20%D8%A3%D8%AA%D9%88%D8%A7%D9%82%D8%B7%D9%87%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=309239&adtre=Corola%202015%20gazoil',
#     'https://www.voursa.com/annonces.cfm?pdtid=313410&adtre=Pegeot%20306',
#     'https://www.voursa.com/annonces.cfm?pdtid=311585&adtre=Voiture%20Toyota%20Corolla%202020',
#     'https://www.voursa.com/annonces.cfm?pdtid=312635&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D9%86%D8%B8%D9%8A%D9%81%D9%87%20%D9%85%D8%A7%D9%81%D9%8A%D9%87%20%D8%B4%DA%AF%D8%A7%D8%B1%D9%87%20%D9%85%D9%88%D9%84%D8%A7%D9%87%D8%A7%20%D8%A8%D8%A7%D9%8A%D8%B9%20%D9%88%D9%84%D8%A7%D9%87%D9%88%20%D9%85%D9%88%D8%B9%D8%B1%D9%87%20%D9%81%D8%B1%D8%B5%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=310695&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%86%D8%B8%D9%8A%D9%81%D9%87%20%D9%85%D8%A7%D9%83%D8%B7%20%D8%B3%D8%A8%D9%82%D8%AA',
#     'https://www.voursa.com/annonces.cfm?pdtid=308512&adtre=Corolla%202017%20SE',
#     'https://www.voursa.com/annonces.cfm?pdtid=308264&adtre=Toyota%20hulix',
#     'https://www.voursa.com/annonces.cfm?pdtid=308494&adtre=Raf%204%202014',
#     'https://www.voursa.com/annonces.cfm?pdtid=308195&adtre=Bon%20Hilux',
#     'https://www.voursa.com/annonces.cfm?pdtid=308062&adtre=Kawkaw%20mavat%20wra9met',
#     'https://www.voursa.com/annonces.cfm?pdtid=306815&adtre=%D9%87%D9%8A%D9%84%D9%8A%D9%83%D8%B3%20%D9%86%D8%B8%D9%8A%D9%81%D9%87%20%D9%85%D8%A7%D8%B9%D9%86%D8%AF%D9%87%20%D9%85%D8%B4%D9%83%D9%8A%D9%84%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=308061&adtre=%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%202008%20%D8%A7%D8%B3%D8%A7%D9%86%D8%B3%20%D8%AD%D8%A7%D9%84%D8%AA%D9%87%20%D8%B2%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=305236&adtre=%D8%A8%D9%8A%D8%B9%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%B1%D8%A7%D9%814/2015',
#     'https://www.voursa.com/annonces.cfm?pdtid=305104&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%202018%20Le%20%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=303742&adtre=%D8%A2%D9%81%D9%86%D8%B3%D9%8A%D8%B3%202.0d%20%D8%B2%D9%8A%D9%86%D9%87%20%D9%85%D8%B2%D8%A7%D9%84%D8%AA%20%D8%A7%D9%83%D9%84%D9%8A%D9%85%20%D9%88%D8%B5%D8%A7%D9%84%D9%88%D9%86%20%D8%B2%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=299175&adtre=Avensis%202.0%20vousa'
# ]

# main_url = ' https://www.voursa.com/index.cfm?PN=5&gct=1&sct=11&gv=13 '


# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=301495&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%202018%20xle%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9%20%D8%A7%D9%81%D9%88%D9%84%20%D8%A7%D8%A8%D9%8A%D8%B3%D9%8A%D9%88%D9%87%20%D8%AC%D8%A7%D9%86%D8%AA%D8%A7%D8%AA%20%D8%A7%D8%B3%D8%A8%D9%88%D8%B1',
#     'https://www.voursa.com/annonces.cfm?pdtid=297175&adtre=Hydain%20alentra%202013',
#     'https://www.voursa.com/annonces.cfm?pdtid=291122&adtre=Chevrolet%20captiva%202015',
#     'https://www.voursa.com/annonces.cfm?pdtid=299565&adtre=Bus%20FORD',
#     'https://www.voursa.com/annonces.cfm?pdtid=298206&adtre=%D9%88%D8%AA%D9%87%20%D9%85%D8%A7%D9%87%D9%8A%20%D9%85%D8%B4%D9%88%D9%83%D9%8A%D9%87%20%D9%88%D9%84%D8%A7%20%D9%81%D9%8A%D9%87%D8%A7%20%D9%85%D8%B4%D9%83%D9%8A%D9%84%D9%87%20%20%D9%85%D8%B1%D9%82%D9%85%D9%87%20%20%20full%20option',
#     'https://www.voursa.com/annonces.cfm?pdtid=299974&adtre=%D8%A8%D9%8A%D8%B9%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3D4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=299188&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%B1%D8%A7%D9%81%204%20full%20option',
#     'https://www.voursa.com/annonces.cfm?pdtid=296885&adtre=%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%20%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=296347&adtre=%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%D9%84%D9%84%D8%A8%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=295421&adtre=Toyota%20Avensis%202.0%20d4D',
#     'https://www.voursa.com/annonces.cfm?pdtid=280059&adtre=Toyota%20%20AURUS',
#     'https://www.voursa.com/annonces.cfm?pdtid=294389&adtre=%D8%B3%D9%8A%D9%84%D9%81%D8%B1%20%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D8%AC%D8%AF%D8%A7%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=289157&adtre=Prado%20%C3%A0%20vendre%20en%20bon%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=291116&adtre=%D9%83%D8%A7%D8%B1%20iveco%2010%20t',
#     'https://www.voursa.com/annonces.cfm?pdtid=291061&adtre=%D9%81%D8%B1%D8%B5%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=265850&adtre=Toyota%20Rav4%20boite%20automatique',
#     'https://www.voursa.com/annonces.cfm?pdtid=289794&adtre=%D8%A2%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20D4D%20%D9%86%D8%B8%D9%8A%D9%8A%D9%81%D9%87%20..%20%D9%85%D9%83%D9%8A%D9%81%20%D8%A8%D8%A7%D8%B1%D8%AF%20%20..%20%D8%A3%D9%88%D8%B1%D8%A7%D9%82%20%D9%85%D9%83%D8%AA%D9%85%D9%84%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=289732&adtre=%D9%87%D9%8A%D9%84%D9%83%D8%B3%20%D8%A3%D9%88%D8%B1%D8%A8%D9%8A%D8%A9%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9%20%D9%85%D8%A7%D9%87%20%D9%88%D8%A7%D8%B9%D8%B1%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=288844&adtre=Mercedes%20E220',
#     'https://www.voursa.com/annonces.cfm?pdtid=284619&adtre=%D9%81%D8%B1%D8%B5%D8%A9%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%AD%D8%AF%D9%8A%D8%AB%D8%A9%20SKODA%20KAMIG%202021',
#     'https://www.voursa.com/annonces.cfm?pdtid=286365&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A3%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%86%D9%88%D9%81%D9%88%20%D9%85%D8%AF%D9%84%20%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87%D8%A7%20%D8%AC%D9%8A%D8%AF%D9%87%20%D8%A7%D9%88%D8%AD%D8%B1%D9%83%D8%AA%D9%87%D8%A7%20%D8%B2%D9%8A%D9%86%D9%87'
# ]






# main_url = ' https://www.voursa.com/index.cfm?PN=10&gct=1&sct=11&gv=13 ' 
    

# annonce_urls = ['https://www.voursa.com/annonces.cfm?pdtid=229859&adtre=Nissan:%20ALMERA', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=226537&adtre=Avensis%20d4d%20voursa%20%207place%20arrivage', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=226896&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%20%D9%83%D8%A7%D8%AA%D8%B1%D9%8A%D9%86%D8%B1%20%D9%85%D9%88%D9%84%D8%A7%D9%87%D8%A7%20%D8%A8%D8%A7%D9%8A%D8%B9%20%D8%A7%D9%88%20%D8%B9%D8%AC%D9%84%D8%A7%D9%86%20%20toyota%20land%20cruis', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=224924&adtre=Nissan%20%20Rogue%202011', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=219248&adtre=Vends%204X4%20TOYOTA%20PRADO', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=219245&adtre=Toyota%20Prado%201KZ%20en%20excellent%20%C3%A9tat', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=199340&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D8%AC%D9%85%D8%B1%D9%83%D8%A9%20%D9%88%D8%AD%D8%A7%D9%84%D8%AA%D9%87%D8%A7%20%D8%A7%D9%84%D9%85%D9%8A%D9%83%D8%A7%D9%86%D9%8A%D9%83%D9%8A%D8%A9%20%D8%AC%D9%8A%D8%AF%D9%87', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=217273&adtre=%D8%A8%D9%8A%D8%B9%20%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%20%D8%A7%D9%81%D9%86%D8%B3%D9%8A%D8%B3', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=217161&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D9%88%D8%A3%D9%88%D8%B1%D8%A7%D9%82%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86%20Renault%20Megane', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=217138&adtre=TOYOTA%20CAMRY%20automatique%20AX%20en%20tr%C3%A9%20bon%20%C3%A9tat', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=212602&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D9%85%D8%B1%D8%B3%D8%AF%D8%B3%20200', 
#                 'https://www.voursa.com/annonces.cfm?pdtid=206746&adtre=%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20TATA%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20XENON%204X4%202016%20/%2057151km%20Moteur%20Ni']


# main_url = 'https://www.voursa.com/index.cfm?PN=11&gct=1&sct=11&gv=13 '

# annonce_urls = ['https://www.voursa.com/annonces.cfm?pdtid=209616&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%B4%D9%81%D8%B1%D9%88%D9%84%D9%8A%20%D9%83%D8%B1%D9%88%D8%B2%20%D9%85%D9%88%D8%AF%D9%8A%D9%84%202012', 'https://www.voursa.com/annonces.cfm?pdtid=205488&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%202018%20%D9%85%D8%A7%DA%AF%D8%B7%20%D8%B4%D9%88%D9%83%D8%A7%D8%AA%20%D9%81%D9%88%D9%84%20%D9%81%D8%AA%D8%AD', 'https://www.voursa.com/annonces.cfm?pdtid=199551&adtre=Hyundai%20Elantra%202015', 'https://www.voursa.com/annonces.cfm?pdtid=205749&adtre=Marque%20:%20Dodge%20-%20Mod%C3%A8le%20:%20Caliber%20-%20Boite%20vitesse%20:%20Au', 'https://www.voursa.com/annonces.cfm?pdtid=203568&adtre=Toyota%20Venza%202015', 'https://www.voursa.com/annonces.cfm?pdtid=204430&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D8%B1%D8%B3%D9%8A%D8%AF%D8%B3%20190', 'https://www.voursa.com/annonces.cfm?pdtid=199341&adtre=Hyundai%20Elantra%202015%20non%20accident%C3%A9%20En%20excellent%20%C3%A9tat', 'https://www.voursa.com/annonces.cfm?pdtid=198820&adtre=VENTE%20%20%20CARINA', 'https://www.voursa.com/annonces.cfm?pdtid=198940&adtre=Nissan%20Primera', 'https://www.voursa.com/annonces.cfm?pdtid=197623&adtre=%D9%86%D9%8A%D8%B3%D8%A7%D9%86%20p11%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9', 'https://www.voursa.com/annonces.cfm?pdtid=196643&adtre=Mercedes%20C220%20elegance%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D8%B1%D8%B3%D9%8A%D8%AF%D8%B3%20%D8%B3%D9%8A%D9%A2%D9%A2%D9%A0', 'https://www.voursa.com/annonces.cfm?pdtid=192922&adtre=%20%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%D9%87%20%D9%85%D8%B2%D8%A7%D9%84%D8%AA%20%20%20%20Toyota%20Corolla%202016']



# main_url = 'https://www.voursa.com/index.cfm?PN=12&gct=1&sct=11&gv=13'


# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=194191&adtre=RAV4%202016%20Gas-oil%204x4',
#     'https://www.voursa.com/annonces.cfm?pdtid=193867&adtre=Un%20camion%20a%20vendre',
#     'https://www.voursa.com/annonces.cfm?pdtid=188936&adtre=RAV4%20%202005%20EN%20BON%20ETAT',
#     'https://www.voursa.com/annonces.cfm?pdtid=188877&adtre=Kango%202012',
#     'https://www.voursa.com/annonces.cfm?pdtid=187735&adtre=%D8%A8%D9%8A%D8%B9%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20Nissan%20Primera',
#     'https://www.voursa.com/annonces.cfm?pdtid=161560&adtre=Toyota%20Prado%20en%20bon%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=184011&adtre=Toyota%20Corolla%202010',
#     'https://www.voursa.com/annonces.cfm?pdtid=177994&adtre=Hyundai%202013%20%C3%A9dition%20limit%C3%A9e%20pas%20encore%20immatricul%C3%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=179325&adtre=En%20bonne%20eta%20toyota%20Corolla%202015',
#     'https://www.voursa.com/annonces.cfm?pdtid=178511&adtre=%D9%83%D8%B1%D9%88%D9%84%D8%A7%20S',
#     'https://www.voursa.com/annonces.cfm?pdtid=176063&adtre=RANGE%20ROVER%20SPORT%20TRES%20BON%20ETAT',
#     'https://www.voursa.com/annonces.cfm?pdtid=173044&adtre=RAV4%20150%20D-CAT%20AWD%20FAP%20LIFE%20A(4*4)%20non%20immatricul%C3%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=169187&adtre=%D9%83%D8%A7%D8%B1%D9%8A%D9%86%D8%A7%20%D9%88%D8%A7%D9%81%D9%8A%20%D8%B9%D9%86%D9%87%D8%A7%20%D9%84%D9%83%D9%84%D8%A7%D9%85'
# ]



# main_url = 'https://www.voursa.com/index.cfm?PN=13&gct=1&sct=11&gv=13 '

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=162429&adtre=Toyota%20V8%20en%20bon%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=165729&adtre=TOYOTA%20V8%20modifi%C3%A9e',
#     'https://www.voursa.com/annonces.cfm?pdtid=164101&adtre=Camion%20MAN',
#     'https://www.voursa.com/annonces.cfm?pdtid=160859&adtre=Mercedes%20E320%20en%20exelent%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=158491&adtre=Voiture%20%20Fiat',
#     'https://www.voursa.com/annonces.cfm?pdtid=143832&adtre=%D9%83%D8%A7%D8%B1%D9%8A%D9%86%D8%A7%20%20%D8%B2%D9%8A%D9%86%D8%A9%20%D9%85%D9%88%D8%AF%D9%8A%D9%86%D9%87%20%D9%88%D8%AA%D9%88%D8%A7%D9%82%D8%B7%D9%87%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=144198&adtre=Toyota%20%204x4',
#     'https://www.voursa.com/annonces.cfm?pdtid=144785&adtre=Corolla%202013%20essence%20en%20bon%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=144439&adtre=%20Toyota%20Corolla%20LE%20%202016%20Essence',
#     'https://www.voursa.com/annonces.cfm?pdtid=140350&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%B7%D8%A7%D8%B4%20%D9%83%D8%B2%D9%88%D8%A7%D9%84'
# ]


# main_url = ' https://www.voursa.com/index.cfm?PN=14&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=139438&adtre=peugeot%20406%20hdi',
#     'https://www.voursa.com/annonces.cfm?pdtid=140185&adtre=Mercedes%20200',
#     'https://www.voursa.com/annonces.cfm?pdtid=139961&adtre=Nissan%20HARDBODY%20ne8ive',
#     'https://www.voursa.com/annonces.cfm?pdtid=139837&adtre=Corolla%20essence%20automatique',
#     'https://www.voursa.com/annonces.cfm?pdtid=139761&adtre=Nissane%20Primera',
#     'https://www.voursa.com/annonces.cfm?pdtid=139778&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%86%D9%8A%D8%B3%D8%A7%D9%86%20%D8%A8%D8%B1%D9%8A%D9%85%D8%B1%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=139569&adtre=Mercedes%20190',
#     'https://www.voursa.com/annonces.cfm?pdtid=139501&adtre=%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D8%AF%D9%83%D8%AF%20%D9%85%D9%83%D9%8A%D9%86%D9%87%20%D8%B2%D9%8A%D9%86%20%D9%88%D9%84%D8%A7%20%D9%83%D8%B7%20%D8%A7%D9%86%D8%B3%D8%A8%D9%82%D8%AA%20%D9%88%D8%AF%D9%8A%D9%88%D8%A7%D9%86%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=139467&adtre=TOYOTA%20COROLLA%20%202008',
#     'https://www.voursa.com/annonces.cfm?pdtid=138708&adtre=Toyota%20avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=139196&adtre=Avensis%20D4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=139192&adtre=Corolla%20LE%202016%20en%20tr%C3%A8s%20bon%20%C3%A9tat',
# ]

# main_url = 'https://www.voursa.com/index.cfm?PN=16&gct=1&sct=11&gv=13'


# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=139119&adtre=Vente%20une%20voiture%20Toyota%20verso%202012%20dedouan%C3%A8',
#     'https://www.voursa.com/annonces.cfm?pdtid=138808&adtre=AVENSIS',
#     'https://www.voursa.com/annonces.cfm?pdtid=138436&adtre=%20%D9%87%D9%8A%D9%84%D9%83%D8%B3%202014%20%D8%B2%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=138532&adtre=avensis%20nouveau%20model',
#     'https://www.voursa.com/annonces.cfm?pdtid=138505&adtre=elegance%20arivaj%20sous%20dwan',
#     'https://www.voursa.com/annonces.cfm?pdtid=138426&adtre=Nissan%20p11',
#     'https://www.voursa.com/annonces.cfm?pdtid=138399&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=138004&adtre=Kangoo%20nouveau%20mod%C3%A8le%202011%20%D9%83%D8%A7%D9%86%D9%82%D9%88',
#     'https://www.voursa.com/annonces.cfm?pdtid=137827&adtre=Voiture%20kangoo%20en%20bon%20%C3%A9tat'
# ]



# main_url = 'https://www.voursa.com/index.cfm?PN=16&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=136944&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D8%A7%D8%AA%D9%8A%D9%83%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=137437&adtre=HULUX',
#     'https://www.voursa.com/annonces.cfm?pdtid=137429&adtre=Toyota%20Rav%204%20diesel',
#     'https://www.voursa.com/annonces.cfm?pdtid=137400&adtre=Rav%204%20Na8ive%20mavihe%20chgare%20liljadin',
#     'https://www.voursa.com/annonces.cfm?pdtid=137399&adtre=%20%20%D9%85%D8%B1%D8%B3%D9%8A%D8%AF%D8%B3%20%20190%D9%84%D9%84%D8%A8%D9%8A%D8%B9%20%D8%B2%D9%8A%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=137158&adtre=elegance%20220',
#     'https://www.voursa.com/annonces.cfm?pdtid=136230&adtre=Toyota%20Prado%201KZ',
#     'https://www.voursa.com/annonces.cfm?pdtid=136295&adtre=Kango',
#     'https://www.voursa.com/annonces.cfm?pdtid=33862&adtre=%D9%85%D8%B1%D8%B3%D8%AF%D8%B3%20E%20250',
#     'https://www.voursa.com/annonces.cfm?pdtid=136503&adtre=%20Corolla%202012%20toute%20neuf%20%C3%A0%20vendre%20320000',
#     'https://www.voursa.com/annonces.cfm?pdtid=136580&adtre=Avensis%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=136465&adtre=HYUNDAI',
#     'https://www.voursa.com/annonces.cfm?pdtid=136419&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=136365&adtre=%20%D9%85%D8%B1%D8%B3%D8%AF%D8%B3%20190%20%D8%B2%D9%8A%D9%86%20%D8%A7%D9%88%20%D9%84%D8%A7%20%D8%B9%D9%86%D8%AF%D9%87%20%D9%85%D8%B4%D9%83%D9%84%D8%A9%20%D9%85%D8%AA%D9%83%D8%A7%D9%85%D9%84%D8%A9%20%D8%A7%D9%84%D8%A7%D9%88%D8%B1%D9%82',
#     'https://www.voursa.com/annonces.cfm?pdtid=136363&adtre=%D8%A7%D9%81%D9%86%D8%B3%D9%8A%D8%B3%20%D9%86%D9%88%D9%81%D9%88%20%D9%85%D9%88%D8%AF%D9%8A%D9%84'
# ]


# main_url = 'https://www.voursa.com/index.cfm?PN=17&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=136129&adtre=Rav4%202009%20en%20tr%C3%A8s%20bonne%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=135994&adtre=Voiture%20AVENSIS%20D4D',
#     'https://www.voursa.com/annonces.cfm?pdtid=135913&adtre=%20Nissan%20p11',
#     'https://www.voursa.com/annonces.cfm?pdtid=135889&adtre=Elegance%20far%20rond',
#     'https://www.voursa.com/annonces.cfm?pdtid=135807&adtre=Peugot',
#     'https://www.voursa.com/annonces.cfm?pdtid=91510&adtre=Mitsubishi%20Space%20wagon%2000AV.....%20Voursa',
#     'https://www.voursa.com/annonces.cfm?pdtid=135683&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%86%D9%8A%D8%B3%D8%A7%D9%86%204*4%D8%A8%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D8%AC%D8%AF%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=135697&adtre=%D8%A8%D9%8A%D8%AC%D9%88307',
#     'https://www.voursa.com/annonces.cfm?pdtid=135632&adtre=Vente%20voiture%20PAJERO%20SPORT',
#     'https://www.voursa.com/annonces.cfm?pdtid=135629&adtre=Rav4',
#     'https://www.voursa.com/annonces.cfm?pdtid=110981&adtre=Avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=135343&adtre=Yarus%20modele%202014',
#     'https://www.voursa.com/annonces.cfm?pdtid=135274&adtre=%D8%A7%D9%81%D9%86%D8%B3%D9%8A%D8%B3%20%D8%A3%D8%AA%D9%8A%D9%83%D8%A7%20D4D%20%20%D9%85%D9%83%D9%8A%D9%81%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=135147&adtre=Avensis%20DkD',
#     'https://www.voursa.com/annonces.cfm?pdtid=135111&adtre=Peugeot%20206',
#     'https://www.voursa.com/annonces.cfm?pdtid=128679&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D9%83%D8%A7%D9%86%D8%B5%20%D9%85%D8%A7%D9%87%D9%8A%20%D9%85%D8%AF%D9%8A%D9%88%D9%86%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=134988&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%86%D9%8A%D9%81%D9%88%20%20%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87%20%D8%B2%D8%A8%D9%86%D8%A9%20%D8%A7%D9%88%D9%83%D9%8A%D8%B5%D9%87%20%D8%B2%D9%8A%D9%86%20%D8%A7%D9%88%D8%B5%D8%A7%D9%84%D9%88%D9%87%20%D8%B2%D9%8A%D9%86'
# ]


# main_url = 'https://www.voursa.com/index.cfm?PN=18&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=134414&adtre=Golf3',
#     'https://www.voursa.com/annonces.cfm?pdtid=134795&adtre=%20Mercedes%20elegance%20%D8%A3%D9%84%D9%83%D8%A7%D9%86%D8%B5%20c220%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D9%87%20%D8%AC%D9%8A%D8%AF%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=134743&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%B7%D8%A7%D8%B4%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%20%D8%AD%D8%AA%20%D9%85%D8%A7%20%D9%81%D9%8A%D9%87%20%D8%A7%D8%B4%D9%83%D8%A7%D8%B1',
#     'https://www.voursa.com/annonces.cfm?pdtid=134604&adtre=Prado%205L%20%20d%E2%80%99etat%20moyenne',
#     'https://www.voursa.com/annonces.cfm?pdtid=134456&adtre=Rav4',
#     'https://www.voursa.com/annonces.cfm?pdtid=134408&adtre=Opel%20issance',
#     'https://www.voursa.com/annonces.cfm?pdtid=134386&adtre=%20Mercedes%20elegance%20%D8%A3%D9%84%D9%83%D8%A7%D9%86%D8%B5%20c220%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D9%87%20%D8%AC%D9%8A%D8%AF%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=134088&adtre=%D9%85%D8%B1%D8%B3%D9%8A%D8%AF%D8%B3%20190%20%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D8%AF%D9%8A%D9%88%D8%A7%D9%86%D8%A9%20%D8%B4%D8%B1%D8%B9%D9%8A%D8%A9%20%D8%AA%D9%86%D8%A8%D8%A7%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=133976&adtre=Mercedes%20200%20nouveau',
#     'https://www.voursa.com/annonces.cfm?pdtid=133922&adtre=%D8%A8%D9%8A%D8%B9%20%D8%B1%D8%A7%D9%814',
#     'https://www.voursa.com/annonces.cfm?pdtid=133927&adtre=Toyota%20Corola%202012',
#     'https://www.voursa.com/annonces.cfm?pdtid=133865&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D9%87%20%D9%85%D9%88%D9%86%D8%B7%D8%B1%D9%87%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D8%AC%D9%8A%D8%A8%20%D8%B4%D9%88%D8%B1%D9%83%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=133906&adtre=Prado%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=132523&adtre=avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=133782&adtre=Toyota%20Corola',
#     'https://www.voursa.com/annonces.cfm?pdtid=133764&adtre=AVENSIS%20NOUVEAU',
#     'https://www.voursa.com/annonces.cfm?pdtid=127689&adtre=contacter-nous'
# ]


# main_url = 'https://www.voursa.com/index.cfm?PN=19&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=133498&adtre=Corolla',
#     'https://www.voursa.com/annonces.cfm?pdtid=133236&adtre=Elegance',
#     'https://www.voursa.com/annonces.cfm?pdtid=132456&adtre=Prado%202008',
#     'https://www.voursa.com/annonces.cfm?pdtid=132853&adtre=Corolla%20s%20jdide',
#     'https://www.voursa.com/annonces.cfm?pdtid=132808&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20kangoo%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=132431&adtre=hyundai%20accent%202013',
#     'https://www.voursa.com/annonces.cfm?pdtid=132510&adtre=Hulix%202.4%20ressort%20en%20bonne%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=132463&adtre=Corolla%206ach%202013',
#     'https://www.voursa.com/annonces.cfm?pdtid=132548&adtre=%D9%83%D8%A7%D8%B1%20%D9%83%D8%A7%D9%86%DA%AF%D9%88%20%D8%B3%D9%88%20%D8%AF%D9%88%D8%A7%D9%86%20%D8%AC%D8%AF%D9%8A%D8%AF',
#     'https://www.voursa.com/annonces.cfm?pdtid=132434&adtre=RENAULT%2021',
#     'https://www.voursa.com/annonces.cfm?pdtid=132174&adtre=%D8%A2%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20D4D%D8%BA%D9%8A%D8%B1%20%D9%85%D8%AC%D9%85%D8%B1%D9%83%D8%A9%20%D8%B2%D9%8A%D9%86%20%D9%85%D8%A7%D8%B4%D8%A7%D8%A7%D9%84%D9%84%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=131749&adtre=%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A3%D9%84%D9%83%D8%A7%D9%86%D8%B3%20%D9%85%D8%AF%D9%88%D9%86%D8%A9%20%D9%85%D8%A7%20%D8%B9%D9%86%D8%AF%D9%87%20%D9%85%D8%B4%D9%83%D9%84%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=132126&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D8%AA%D9%88%D8%A7%D9%82%D8%B7%D9%87%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86%20%D9%88%D8%B2%D9%8A%D9%86%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=132018&adtre=Une%20voiture%20CARINA%20AN%20%C3%A0%20vendre'
# ]




# main_url = 'https://www.voursa.com/index.cfm?PN=20&gct=1&sct=11&gv=13 '

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=130458&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=131877&adtre=%D9%86%D9%8A%D8%B3%D8%A7%D9%86%20%D8%A7%D8%A8%D8%B1%D9%8A%D9%85%D9%8A%D8%B1%D8%A7%20p10%20%D8%AF%D9%88%D8%A7%D9%86%D9%87%20%D8%B4%D8%B1%D8%B9%D9%8A%D8%A9%20AL',
#     'https://www.voursa.com/annonces.cfm?pdtid=130838&adtre=%D8%A8%D8%B1%D8%A7%D8%AF%D9%88%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9%202008%20%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%D9%8A%D9%83',
#     'https://www.voursa.com/annonces.cfm?pdtid=131659&adtre=%D8%A3%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9%20%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D8%AC%D8%AF%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=131546&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%B7%D8%A7%D8%B4',
#     'https://www.voursa.com/annonces.cfm?pdtid=131542&adtre=D4D%20%D8%A7%D9%81%D9%8A%D9%86%D8%B3%D9%8A%D8%B3',
#     'https://www.voursa.com/annonces.cfm?pdtid=131276&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A8%D9%8A%D8%AC%D9%88205%D9%84%D8%A7%D8%A8%D8%A7%D8%B3%20%D8%A8%D9%8A%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=131193&adtre=toyota%20avensis%20zeyne%205%20port%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=130326&adtre=Toyota%20hilux%202013',
#     'https://www.voursa.com/annonces.cfm?pdtid=131087&adtre=%D9%83%D8%A7%D9%86%D9%83%D9%88%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=131087&adtre=%D9%83%D8%A7%D9%86%D9%83%D9%88%20%D9%84%D9%84%D8%A8%D9%8A%D8%B9',
#     'https://www.voursa.com/annonces.cfm?pdtid=131091&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3d4d%205%D8%A7%D8%A8%D9%88%D8%B1%D8%AA',
#     'https://www.voursa.com/annonces.cfm?pdtid=131100&adtre=Toyota%20prado%20%D9%81%D8%B1%D8%B5%D8%A9%20%D9%86%D8%A7%D8%AF%D8%B1%D8%A9%20-%20%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%20%D8%A8%D8%B1%D8%A7%D8%AF%D9%88',
#     'https://www.voursa.com/annonces.cfm?pdtid=131077&adtre=Toyota%20Avensis%202.0%20sous%20douane',
#     'https://www.voursa.com/annonces.cfm?pdtid=131070&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20%D9%86%D9%88%D9%81%D9%88%20%D9%85%D9%85%D8%AA%D8%A7%D8%B2%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=130864&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D9%87%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20jeeep%20%D9%87%D9%88%D9%8A%D9%86%20%D9%88%D8%AD%D8%A7%D9%84%D8%AA%D9%87%20%D8%B9%D8%A7%D8%AF%D9%8A',
#     'https://www.voursa.com/annonces.cfm?pdtid=130908&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202.0%D9%85%D9%88%D8%AA%D9%8A%D8%B1D4D',
#     'https://www.voursa.com/annonces.cfm?pdtid=130878&adtre=406%20Peugot%20Moteur',
#     'https://www.voursa.com/annonces.cfm?pdtid=130875&adtre=Mercedes%20E%20220',
#     'https://www.voursa.com/annonces.cfm?pdtid=130779&adtre=Avensis%20D4d'
# ]

# main_url = 'https://www.voursa.com/index.cfm?PN=21&gct=1&sct=11&gv=13'


# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=130640&adtre=Toyota%20carina',
#     'https://www.voursa.com/annonces.cfm?pdtid=130386&adtre=200%20%D8%A7%D8%AA%D9%88%D8%A7%D9%82%D8%B7%D9%87%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86%20%D9%86%D8%B8%D9%8A%D9%81%D8%A9%20%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87%20%D8%B2%D9%8A%D9%86%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=130246&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%87%D9%8A%D9%88%D9%86%D8%AF%D8%A7%D9%89',
#     'https://www.voursa.com/annonces.cfm?pdtid=130216&adtre=Toyota%20Corrola%202013',
#     'https://www.voursa.com/annonces.cfm?pdtid=129955&adtre=406%20sous%20douane',
#     'https://www.voursa.com/annonces.cfm?pdtid=127781&adtre=CITRO%C3%8BN%20C5%20HDI',
#     'https://www.voursa.com/annonces.cfm?pdtid=129635&adtre=Avensis%202.0%20mekinthe%20jdide%20arrivage',
#     'https://www.voursa.com/annonces.cfm?pdtid=129409&adtre=Corolla%20Tach%202012',
#     'https://www.voursa.com/annonces.cfm?pdtid=129224&adtre=Avensis%20D4D%20jdide',
#     'https://www.voursa.com/annonces.cfm?pdtid=129207&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D9%87%20ford',
#     'https://www.voursa.com/annonces.cfm?pdtid=127729&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D8%B1%D8%B3%D9%8A%D8%AF%D8%B3%20200%20%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%A9%20%D8%AC%D9%8A%D8%AF%D8%A9'
# ]


# main_url = ' https://www.voursa.com/index.cfm?PN=22&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=129150&adtre=%D9%83%D8%A7%D8%B1%D9%8A%D9%86%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=129142&adtre=%D8%A7%D9%81%D9%86%D8%B3%D9%8A%D8%B3%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=129045&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A8%D8%B1%D8%A7%D8%AF%D9%88%20%D9%A2%D9%A0%D9%A0%D9%A9%20%D8%A3%D9%85%D9%83%D9%88%D9%84%D9%8A%20%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=127565&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=128915&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D8%A7%D9%81%D9%86%D8%B3%D9%8A%D8%B3',
#     'https://www.voursa.com/annonces.cfm?pdtid=128884&adtre=%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%202008%20%D9%83%D8%B2%D9%88%D8%A7%D9%84%20%D9%85%D8%A7%D9%83%D8%B7%20%D9%86%D8%B3%D8%A8%D9%82%D8%AA%206%20%D9%81%D9%8A%D8%AA%D8%B3%20%D9%86%D8%B8%D9%8A%D9%81%D9%87%20%D8%AA%D8%A8%D8%A7%D8%B1%D9%83%20%D8%A7%D9%84%D9%84%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=128871&adtre=Citreon%20c5',
#     'https://www.voursa.com/annonces.cfm?pdtid=128846&adtre=Avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=128778&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A2%D9%81%D9%86%D8%B3%D9%8A%D8%B3%20%D8%B2%D9%8A%D9%86%20%D8%A7%D9%88%D8%B1%D8%A7%D9%82%D9%87%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86%20%D8%A7%D9%88%D8%AD%D8%B1%D9%83%D8%AA%D9%87%20%D8%B2%D9%8A%D9%86%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=128708&adtre=Golf%20plo%20s5',
#     'https://www.voursa.com/annonces.cfm?pdtid=128613&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D9%87%20%D8%B1%D9%8A%D9%86%D9%88%20%D8%A2%D9%84%D9%8A%D8%B2%D9%8A%20%D8%AF%D9%8A%D9%88%D8%A7%D9%86%D8%AA%D9%87%20%D8%B4%D8%B1%D8%B9%D9%8A%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=128357&adtre=Mitchibushi%20pajero%20GLX',
#     'https://www.voursa.com/annonces.cfm?pdtid=128505&adtre=TOYOTA%20HILUX',
#     'https://www.voursa.com/annonces.cfm?pdtid=128299&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%84%D8%A8%D9%8A%D8%AC%D9%88%20%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87%D8%A7%20%D8%B2%D9%8A%D9%86%20%D9%88%D9%85%D8%AF%D9%8A%D9%88%D9%86%D8%A7',
#     'https://www.voursa.com/annonces.cfm?pdtid=128165&adtre=%D8%A7%D9%84%D9%8A%D9%83%D8%A7%D9%86%D8%B5cdi',
#     'https://www.voursa.com/annonces.cfm?pdtid=128161&adtre=Avensis%20d4d',
#     'https://www.voursa.com/annonces.cfm?pdtid=127471&adtre=Toyota%20Corolla%202011',
#     'https://www.voursa.com/annonces.cfm?pdtid=128032&adtre=%20RENAULT%20EXPRES%20%D8%AD%D8%A7%D9%84%D8%AA%D9%87%20%D8%B2%D9%8A%D9%86%D8%A9%20%D9%88%D9%85%D9%83%D9%8A%D9%86%D8%AA%D9%87%20%D8%A7%D8%B1%D9%8A%D9%81%D8%A7%D8%AC%20%D9%88%D9%85%D8%AF%D9%8A%D9%88%D9%86%D8%A9'
# ]




# main_url = 'https://www.voursa.com/index.cfm?PN=23&gct=1&sct=11&gv=13 '

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=128004&adtre=Wolswagen%20jetta%20gasoil',
#     'https://www.voursa.com/annonces.cfm?pdtid=125353&adtre=Vente%20%20une%20voiture%20prado%202006',
#     'https://www.voursa.com/annonces.cfm?pdtid=126856&adtre=avensis%20nouveau%20jdide%20moudewne',
#     'https://www.voursa.com/annonces.cfm?pdtid=127845&adtre=Bmw%20x5',
#     'https://www.voursa.com/annonces.cfm?pdtid=127732&adtre=Toyota%20avensis%20%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=127555&adtre=%D9%86%D9%8A%D8%B3%D8%A7%D9%864\4',
#     'https://www.voursa.com/annonces.cfm?pdtid=127656&adtre=Avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=97745&adtre=Renault%20kangoo%20neuf%20avec%20assurance',
#     'https://www.voursa.com/annonces.cfm?pdtid=127447&adtre=Rav%204',
#     'https://www.voursa.com/annonces.cfm?pdtid=127305&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20200',
#     'https://www.voursa.com/annonces.cfm?pdtid=126929&adtre=Avensis%20D4d%20en%20bonne%20%C3%A9tat',
#     'https://www.voursa.com/annonces.cfm?pdtid=126407&adtre=Pajero%20a%20vendre%20%C3%A0%20bon%20prix'
# ]



# main_url = 'https://www.voursa.com/index.cfm?PN=24&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=126011&adtre=corolla',
#     'https://www.voursa.com/annonces.cfm?pdtid=126285&adtre=Avensis%20nouveau',
#     'https://www.voursa.com/annonces.cfm?pdtid=126303&adtre=Suzuki%20Alto',
#     'https://www.voursa.com/annonces.cfm?pdtid=126205&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20407%20%D9%85%D8%AF%D9%8A%D9%88%D9%86%D8%A7%20%20%D9%85%D9%83%D9%8A%D9%86%D8%A9%20%D8%B2%D9%8A%D9%86%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=125840&adtre=Marcedes%20bens%20190%20mezalt%20jdide',
#     'https://www.voursa.com/annonces.cfm?pdtid=125852&adtre=Hyundai%202014',
#     'https://www.voursa.com/annonces.cfm?pdtid=122909&adtre=%D9%87%D9%8A%D9%84%D9%83%D8%B3%20%D9%81%D9%8A%DA%A8%D9%88%20%D8%A3%D9%88%D8%B1%D8%A7%D9%82%D9%87%D8%A7%20%D8%AA%D8%A7%D9%85%D9%8A%D9%86%202019',
#     'https://www.voursa.com/annonces.cfm?pdtid=125625&adtre=Avensis%20nouveau%20model',
#     'https://www.voursa.com/annonces.cfm?pdtid=125444&adtre=190%20en%20bonne%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=125390&adtre=Avensis%205%20porte%20bone%20etat',
#     'https://www.voursa.com/annonces.cfm?pdtid=125401&adtre=%D9%83%D9%88%D9%84%D9%81%20%D8%B3%D8%B1%D9%8A%204%20%D9%85%D8%A7%D9%81%D9%8A%D9%87%D8%A7%20%D8%B4%D9%83%D8%A7%D8%B1%D9%87%20%D8%AD%D8%B1%D9%81%D9%87%D8%A7%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%20%D9%88%D8%A7%D9%84%D8%AD%D8%B1%D9%83%D9%87%20%D9%85%D9%85%D8%AA%D8%A7%D8%B2%D9%87',
#     'https://www.voursa.com/annonces.cfm?pdtid=125375&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202.0%20%D9%85%D8%A7%D9%83%D8%B7%20%D9%86%D8%B3%D8%A8%D9%82%D8%AA%20%D8%AD%D8%B1%D9%81%D9%87%D8%A7%20%D8%A7%D8%AC%D8%AF%D9%8A%D8%AF%2062..AU',
#     'https://www.voursa.com/annonces.cfm?pdtid=125271&adtre=190%D9%85%D8%B2%D8%A7%D9%84%D8%AA%20%D8%AC%D9%8A%D8%AF%D8%A9%20%D9%85%D8%B4%D8%A7%D8%A1%20%D8%A7%D9%84%D9%84%D9%87%20%D9%81%D8%B1%D8%B5%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=125183&adtre=corolla%201.8',
#     'https://www.voursa.com/annonces.cfm?pdtid=125180&adtre=avensis',
#     'https://www.voursa.com/annonces.cfm?pdtid=125159&adtre=%D9%83%D8%AF%D9%8A%D9%84%D9%83%20%D9%83%D8%B7%D8%B9%20%D9%84%D8%A7%2014000%20%D9%83%D9%8A%D9%84%20%D9%85%D9%88%D9%84%D8%A7%D9%87%20%D8%A8%D8%A7%D9%8A%D8%B9%D8%A7%D9%86%D9%88%D8%A7%D8%B1%20%D9%88%D8%AC%D8%AF%D9%8A%D8%AF'
# ]





# main_url = 'https://www.voursa.com/index.cfm?PN=25&gct=1&sct=11&gv=13'

# annonce_urls = [
#     'https://www.voursa.com/annonces.cfm?pdtid=125120&adtre=avensis%20nouveau%20jdide%20zeyne%20%20mavihe%20echgare%20moudewne',
#     'https://www.voursa.com/annonces.cfm?pdtid=124980&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D9%83%D9%88%D8%B1%D9%88%D9%84%D8%A7%20%D8%AF%D9%8A%D9%88%D8%A7%D9%86%D8%AA%D9%87%20%D8%B4%D8%B1%D8%B9%D9%8A%D9%87%20%D9%88%D9%84%D8%A7%20%D8%B9%D9%86%D8%AF%D9%87%20%20%D9%85%D8%B4%D9%83%20%20D.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=124234&adtre=%D8%A8%D9%8A%D8%B9%20%D8%A3%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%20D4D',
#     'https://www.voursa.com/annonces.cfm?pdtid=122336&adtre=MEGANE',
#     'https://www.voursa.com/annonces.cfm?pdtid=124444&adtre=Hyndaiy%20accent',
#     'https://www.voursa.com/annonces.cfm?pdtid=124443&adtre=Toyota%20avensis%202.0',
#     'https://www.voursa.com/annonces.cfm?pdtid=124316&adtre=%D8%A7%D9%81%D8%A7%D9%86%D8%B3%D9%8A%D8%B3%202.0%20%D9%86%D8%B8%D9%8A%D9%81%D9%87%20%D9%85%D8%A7%D9%81%D9%8A%D9%87%20%D8%A7%D8%B4%D9%83%D8%A7%D8%B1',
#     'https://www.voursa.com/annonces.cfm?pdtid=123518&adtre=Nissan%20MAXIMA',
#     'https://www.voursa.com/annonces.cfm?pdtid=124156&adtre=%D9%83%D8%A7%D8%B1%D9%8A%D9%86%D8%A7%20%D8%A8%D8%AD%D8%A7%D9%84%D8%A9%20%D9%85%D9%85%D8%AA%D8%A7%D8%B2%D8%A9',
#     'https://www.voursa.com/annonces.cfm?pdtid=123594&adtre=406%20peugeot',
#     'https://www.voursa.com/annonces.cfm?pdtid=124016&adtre=V8%202014',
#     'https://www.voursa.com/annonces.cfm?pdtid=123843&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D8%A7%D9%88%D8%A8%D9%84',
#     'https://www.voursa.com/annonces.cfm?pdtid=121328&adtre=%D8%B1%D9%8A%D9%86%D9%88%20%D9%85%D9%8A%D9%83%D8%A7%D9%86',
#     'https://www.voursa.com/annonces.cfm?pdtid=123226&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9Rav4',
#     'https://www.voursa.com/annonces.cfm?pdtid=123795&adtre=%D8%AA%D9%88%D9%8A%D9%88%D8%AA%D8%A7%20%D8%A8%D9%8A%D9%83%20%D8%A2%D8%A8'
# ]





main_url = 'https://www.voursa.com/index.cfm?PN=26&gct=1&sct=11&gv=13'

annonce_urls = [
    'https://www.voursa.com/annonces.cfm?pdtid=123732&adtre=avensis%20nouveau%20moudewne%20mezalet%20zeyne',
    'https://www.voursa.com/annonces.cfm?pdtid=123701&adtre=%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20(%20Elegance%20)',
    'https://www.voursa.com/annonces.cfm?pdtid=122954&adtre=%D9%86%D9%8A%D8%B3%D8%A7%D9%86%20%D8%A8%D8%B1%D9%8A%D9%85%D9%8A%D8%B1%D8%A7',
    'https://www.voursa.com/annonces.cfm?pdtid=123479&adtre=Nissan%20primeira',
    'https://www.voursa.com/annonces.cfm?pdtid=123035&adtre=Pegoet%20206%20%20mekinteha%20ma%20te6lsse%20papier%20complet',
    'https://www.voursa.com/annonces.cfm?pdtid=122997&adtre=%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B1%D8%A9%20%D9%85%D9%86%20%D9%86%D9%88%D8%B9%20%D9%87%D8%A7%D9%8A%D9%84%D9%88%D9%83%D8%B3',
    'https://www.voursa.com/annonces.cfm?pdtid=122837&adtre=avensis%20nouveau%20mezalet%20zeyne%20mou%20w%20mekinethe%20ejdide%20'
]


for annonce_url in annonce_urls:
    download_images_from_annonce(annonce_url)



