# Générateur de mot de passe sécurisés
Ce projet est mené par Arnaud Nicolas et Alexandre Proust.

## Objectif
Le but est de créer une interface utilisateur permettant à un utilisateur de générer un mot avec une longueur choisie et la possibilité d'ajouter un hashage.
Le deuxième objectif est de garantir une suite de tests sur cette application.

## Structure des tests fonctionnels
| Nom du cas de test | Objectif | Préconditionnement | ID du test | Action attendu de l'utilisateur | Action du système attendue | Données de test | Critère de réussite | Statut du test |
|-------|--------|-------|--------|-------|--------|-------|--------|--------|
| Test de la taille de la génération de mdp | Affichage d'un mot de passe de la taille renseigné, entre 5 et 25 caractères | Importation de unittest, Installation de Python 3.11.5 | 1.1.1 | L'utilisateur choisi une taille entre 5 et 25 dans le champ: 'Number of caracters' | Le textField en bas de page montre un mot de passe avec le nombre exacte de caractère renseigné | N/A | Un mot de passe est généré et affiché de la taille exacte renseigné par l'utilisateur | OK |
| Test de la taille de la génération de mdp de taille positive inférieur à 5 | Empêcher la création de mot de passe si la taille n'est pas entre 5 et 25 | Importation de unittest, Installation de Python 3.11.5 | 1.1.2 | L'utilisateur choisi une taille entre 5 et 25 dans le champ: 'Number of caracters' | Le mot de passe généré est 'error', et est instantanément vidé | N/A | Un message d'erreur est affiché | OK |
| Test de la taille de la génération de mdp de taille positive supérieure à 25 | Empêcher la création de mot de passe si la taille n'est pas entre 5 et 25 | Importation de unittest, Installation de Python 3.11.5 | 1.1.3 | L'utilisateur choisi une taille entre 5 et 25 dans le champ: 'Number of caracters' | Le mot de passe généré est 'error', et est instantanément vidé | N/A | Un message d'erreur est affiché | OK |
| Test de la taille de la génération de mdp de taille négative | Empêcher la création de mot de passe si la taille n'est pas entre 5 et 25 | Importation de unittest, Installation de Python 3.11.5 | 1.1.4 | L'utilisateur choisi une taille entre 5 et 25 dans le champ: 'Number of caracters' | Le mot de passe généré est 'error', et est instantanément vidé | N/A | Un message d'erreur est affiché | OK |
| Test de la taille de la génération de mdp de taille 0 | Empêcher la création de mot de passe si la taille n'est pas entre 5 et 25 | Importation de unittest, Installation de Python 3.11.5 | 1.1.5 | L'utilisateur choisi une taille entre 5 et 25 dans le champ: 'Number of caractertexts' | Le mot de passe généré est 'error', et est instantanément vidé | N/A | Un message d'erreur est affiché | OK |
| Test de la présence de minuscules dans la génération de mdp | Vérifier la présence de lettres minuscules dans le mot de passe si la case 'Lowercase' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.2 | L'utilisateur coche la case 'Lowercase' | Le textField en bas de page montre un mot de passe avec au moins une lettre minuscule | N/A | Un mot de passe contenant des lettres minuscules est généré | OK |
| Test de la présence de majuscules dans la génération de mdp | Vérifier la présence de lettres minuscules dans le mot de passe si la case 'Uppercase' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.3 | L'utilisateur coche la case 'Uppercase' | Le textField en bas de page montre un mot de passe avec au moins une lettre majuscule | N/A | Un mot de passe contenant des lettres majuscules est généré | OK |
| Test de la présence de chiffres dans la génération de mdp | Vérifier la présence de chiffres dans le mot de passe si la case 'Digits' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.4 | L'utilisateur coche la case 'Digits' | Le textField en bas de page montre un mot de passe avec au moins un chiffre | N/A | Un mot de passe contenant des chiffres est généré | OK |
| Test de la présence de caractères spéciaux dans la génération de mdp | Vérifier la présence de caractères spéciaux dans le mot de passe si la case 'Symbols' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.5 | L'utilisateur coche la case 'Symbols' | Le textField en bas de page montre un mot de passe avec au moins un symbole | N/A | Un mot de passe contenant des caractères spéciaux est généré | OK |
| Test de la présence d'option dans la génération de mdp | Empêcher la création de mot de passe si aucun paramêtre n'est coché | Importation de unittest, Installation de Python 3.11.5 | 1.6 | L'utilisateur ne coche aucune cases | Le systeme empeche la création  du mot de passe | N/A | Un message d'erreur est affiché | OK |
| Test du hashage SHA-256 dans la génération de mdp | Vérifier la conformité du hashage par rapport au hashage 'SHA-256' si la case 'SHA-256' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.7.1 | L'utilisateur sélectionne le radioButton 'SHA-256' | Le textField en bas de page montre un mot de passe hashé respectant le protocole 'SHA-256' | N/A | Un mot de passe hashé conforme au format 'SHA-256' est généré | OK |
| Test du hashage MD5 dans la génération de mdp | Vérifier la conformité du hashage par rapport au hashage 'MD5' si la case 'MD5' est cochée | Importation de unittest, Installation de Python 3.11.5 | 1.7.2 | L'utilisateur sélectionne le radioButton 'MD5' | Le textField en bas de page montre un mot de passe hashé respectant le protocole 'MD5' | N/A | Un mot de passe hashé conforme au format 'MD5' est généré | OK |
| Test automatique du titre de l'application | Vérifier que le titre de l'application est le bon | Importation de unittest et de tkinter, Installation de Python 3.11.5 | 1.8.1 | Automatique | Lancement de l'application | N/A | Le titre attendu est le même que celui de l'application | OK |
| Test automatique d'instanciation des éléments | Vérifier que les éléments de l'interface s'instancient | Importation de unittest et de tkinter, Installation de Python 3.11.5 | 1.8.2 | L'utilisateur vérifie que tous les champs soient disposés sur l'interface | Vérification de la création de tous les éléments de l'interface | N/A | Tous les éléments sont présent sur l'applciation | OK |
| Test automatique des checkbox des options de mdp | Vérifier que les deux premières checkbox sont cochées par défaut | Importation de unittest et de tkinter, Installation de Python 3.11.5 | 1.8.3 | L'utilisateur regarde si les deux premières option de mdp soient cochées | Vérifier que seul les checkbox pour les minuscule et les majuscules soient activées | N/A | Les deux checkbox sont selectionnées au lancement | OK |
| Test automatique du bouton radio de hashage | Vérifier que le bouton radio du hash SHA-256 est activé par défaut | Importation de unittest et de tkinter, Installation de Python 3.11.5 | 1.8.4 | L'utilisateur regarde si le premier élément des choix de hashage est sélectionné | Vérifier que seul le premier bouton radio pour le premier hash soit activé | N/A | Le bouton radio "SHA-256" est sélectionné au lancement de l'application | OK |

## Bugs rencontrés:

### Bug 1:
#### Description:
Lors de la génération d'un mot de passe, lorsque le label d'évaluation prend la valeur "Très faible", et que par la suite, lors de la regénération d'un mot de passe, le label prend la valeur "Faible", le précédent label reste affiché en arrière plan.
#### Cause:
Le label n'est pas vidé lors de la regénération d'un mot de passe.
#### Correction:
Vidage du label lors de la regénération d'un mot de passe. Puis affichage du nouveau label.

### Bug 2:
#### Description:
Lors du démarage de l'application, les deux radioButton liés au hashage sont sélectionnés.
#### Cause:
Pas de choix par défault pour les radioButton.
#### Correction:
Mettre le radioButton "MD5" sélectionné par défaut.

### Bug 3:
#### Description:
Si aucun nombre n'est tapé dans le Texfield de choix du nombre de caractère, aucun message d'erreur n'est affiché
#### Cause:
Le message d'erreur n'est pas affiché si le nombre de caractère est égal à 0.
#### Correction:
Ajout d'une condition pour afficher le message d'erreur si le nombre de caractère est égal à 0.

### Bug 4:
#### Description:
Si les caractère tapé dans le Texfield de choix du nombre de caractère ne sont pas des chiffres, aucun message d'erreur n'est affiché
#### Cause:
Le message d'erreur n'est pas affiché si le nombre de caractère n'est pas un nombre.
#### Correction:
Ajout d'une condition pour afficher le message d'erreur si le nombre de caractère n'est pas un nombre.

## Commandes
Pour lancer l'application :
```
python main.py
```

Pour lancer un fichier de test :
```
python -m unittest [nom_du_fichier]
```