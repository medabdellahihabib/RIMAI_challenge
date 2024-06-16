





# import os
# import requests
# import json
# import re
# from urllib.parse import urlparse

# # Chemin vers le fichier JSON contenant les liens des photos
# json_file = r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_17-14-19-076 (1).json'

# # Dossier de sortie pour enregistrer les photos
# output_folder = 'photos_photos1'

# # Créer le dossier de sortie s'il n'existe pas
# os.makedirs(output_folder, exist_ok=True)

# # Charger les données depuis le fichier JSON
# with open(json_file, 'r') as f:
#     data = json.load(f)

# # Parcourir chaque élément dans les données
# for index, item in enumerate(data, start=1):
#     url = item.get('image')  # Obtenir l'URL de l'élément
#     if url:
#         parsed_url = urlparse(url)
#         filename = os.path.basename(parsed_url.path)
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Construire le chemin de sortie avec un nom de fichier propre
#             clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
#             output_path = os.path.join(output_folder, f'photo_{index}_{clean_filename}')
#             # Enregistrer l'image dans le dossier de sortie
#             with open(output_path, 'wb') as img_file:
#                 img_file.write(response.content)
#             print(f"Photo {index} téléchargée avec succès.")
#         else:
#             print(f"Échec du téléchargement de la photo {index}.")
#     else:
#         print(f"Aucune URL trouvée pour la photo {index}.")

# print("Téléchargement terminé.")







# import os
# import requests
# import json
# import re
# from urllib.parse import urlparse

# # Chemin vers le fichier JSON contenant les liens des photos
# json_file = r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_17-21-18-591.json'


# # Dossier de sortie pour enregistrer les photos
# output_folder = 'photos_photos2'

# # Créer le dossier de sortie s'il n'existe pas
# os.makedirs(output_folder, exist_ok=True)

# # Charger les données depuis le fichier JSON
# with open(json_file, 'r') as f:
#     data = json.load(f)

# # Parcourir chaque élément dans les données
# for index, item in enumerate(data, start=1):
#     url = item.get('image')  # Obtenir l'URL de l'élément
#     if url:
#         parsed_url = urlparse(url)
#         filename = os.path.basename(parsed_url.path)
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Construire le chemin de sortie avec un nom de fichier propre
#             clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
#             output_path = os.path.join(output_folder, f'photo_{index}_{clean_filename}')
#             # Enregistrer l'image dans le dossier de sortie
#             with open(output_path, 'wb') as img_file:
#                 img_file.write(response.content)
#             print(f"Photo {index} téléchargée avec succès.")
#         else:
#             print(f"Échec du téléchargement de la photo {index}.")
#     else:
#         print(f"Aucune URL trouvée pour la photo {index}.")

# print("Téléchargement terminé.")







# import os
# import requests
# import json
# import re
# from urllib.parse import urlparse

# # Chemin vers le fichier JSON contenant les liens des photos
# json_file = r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_17-29-02-183.json'


# # Dossier de sortie pour enregistrer les photos
# output_folder = 'photos_photos3'

# # Créer le dossier de sortie s'il n'existe pas
# os.makedirs(output_folder, exist_ok=True)

# # Charger les données depuis le fichier JSON
# with open(json_file, 'r') as f:
#     data = json.load(f)

# # Parcourir chaque élément dans les données
# for index, item in enumerate(data, start=1):
#     url = item.get('image')  # Obtenir l'URL de l'élément
#     if url:
#         parsed_url = urlparse(url)
#         filename = os.path.basename(parsed_url.path)
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Construire le chemin de sortie avec un nom de fichier propre
#             clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
#             output_path = os.path.join(output_folder, f'photo_{index}_{clean_filename}')
#             # Enregistrer l'image dans le dossier de sortie
#             with open(output_path, 'wb') as img_file:
#                 img_file.write(response.content)
#             print(f"Photo {index} téléchargée avec succès.")
#         else:
#             print(f"Échec du téléchargement de la photo {index}.")
#     else:
#         print(f"Aucune URL trouvée pour la photo {index}.")

# print("Téléchargement terminé.")







# import os
# import requests
# import json
# import re
# from urllib.parse import urlparse

# # Chemin vers le fichier JSON contenant les liens des photos
# json_file = r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_22-32-11-750.json'


# # Dossier de sortie pour enregistrer les photos
# output_folder = 'photos_photos4'

# # Créer le dossier de sortie s'il n'existe pas
# os.makedirs(output_folder, exist_ok=True)

# # Charger les données depuis le fichier JSON
# with open(json_file, 'r') as f:
#     data = json.load(f)

# # Parcourir chaque élément dans les données
# for index, item in enumerate(data, start=1):
#     url = item.get('image')  # Obtenir l'URL de l'élément
#     if url:
#         parsed_url = urlparse(url)
#         filename = os.path.basename(parsed_url.path)
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Construire le chemin de sortie avec un nom de fichier propre
#             clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
#             output_path = os.path.join(output_folder, f'photo_{index}_{clean_filename}')
#             # Enregistrer l'image dans le dossier de sortie
#             with open(output_path, 'wb') as img_file:
#                 img_file.write(response.content)
#             print(f"Photo {index} téléchargée avec succès.")
#         else:
#             print(f"Échec du téléchargement de la photo {index}.")
#     else:
#         print(f"Aucune URL trouvée pour la photo {index}.")

# print("Téléchargement terminé.")




import os
import requests
import json
import re
from urllib.parse import urlparse
from time import sleep

json_files = [
    r'C:\Users\Dell\Downloads\dataset_google-images-scraper_2024-05-17_16-40-55-138.json',
    r'C:\Users\Dell\Downloads\dataset_google-images-scraper_2024-05-17_15-11-13-903.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_22-54-15-610.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-16_16-35-38-672.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_00-55-14-051.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_00-57-53-721.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-01-45-031.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-04-07-647.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-06-47-906.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-08-28-492.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-10-24-345.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-11-50-965.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-13-52-758.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-18-52-057.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-24_01-20-42-584.json',
    r'C:\Users\Dell\Downloads\dataset_facebook-photos-scraper_2024-05-25_19-35-57-160.json',
    r'C:\Users\Dell\Downloads\dataset_google-images-scraper_2024-05-21_22-05-59-584.json'
]

# Dossier de sortie pour enregistrer les photos
output_folder = 'photos_photos6'

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

photo_index = 1  # Initialiser un index pour les photos

# Fonction pour télécharger une image avec plusieurs tentatives
def download_image(url, output_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_path, 'wb') as img_file:
                    img_file.write(response.content)
                return True
            else:
                print(f"Échec du téléchargement de la photo, statut: {response.status_code}")
        except requests.ConnectionError as e:
            print(f"Erreur de connexion: {e}. Tentative {attempt + 1}/{max_retries}")
            sleep(2)  # Attendre avant de réessayer
    return False

# Parcourir chaque fichier JSON dans la liste
for json_file in json_files:
    # Charger les données depuis le fichier JSON avec l'encodage UTF-8
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Parcourir chaque élément dans les données
    for item in data:
        url = item.get('image')  # Obtenir l'URL de l'élément
        if url:
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            clean_filename = re.sub(r'[<>:"/\\|?*]', '', filename)
            output_path = os.path.join(output_folder, f'photo_{photo_index}_{clean_filename}')
            
            # Tenter de télécharger l'image
            if download_image(url, output_path):
                print(f"Photo {photo_index} téléchargée avec succès.")
            else:
                print(f"Échec du téléchargement de la photo {photo_index} après plusieurs tentatives.")
                
            photo_index += 1  # Incrémenter l'index des photos
        else:
            print(f"Aucune URL trouvée pour la photo {photo_index}.")

print("Téléchargement terminé.")


