# coucouCliqueur

application qui clic automatiquement sur "Coucou" dans messenger
Vesrion en Python

## Setup

1. dans le fichier credentials remplacer :
    - ``Your_fb_username`` par votre username messenger, soit une adresse email, soit un numero de telephone
    - ``Your_fb_password`` par votre mot de passe messenger
    - ``1234567890123456`` par l'identifiant de groupe qui se trouve dan l'url de messenger `https://www.messenger.com/t/{ID}`, c'est un chiffre a 16 caracteres
    - ``Your_name_in_groupe`` par votre nom / surnom dans le groupe en question
1. télécharger les dependances avec ``pip install -r requirements.txt``
1. télécharger le driver pour FireFox : https://github.com/mozilla/geckodriver/releases/
1. lancer le programme avec ``python Auto_clic_react.py``