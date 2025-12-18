# TextTool

## Description
TextTool est un outil en ligne de commande permettant d'effectuer des opérations sur des chaînes de caractères.

## Fonctionnalités
- **upper** : Convertit le texte en majuscules
- **lower** : Convertit le texte en minuscules
- **length** : Affiche la longueur du texte
- **count-words** : Compte le nombre de mots dans le texte
- **prefix** : Affiche les 10 premiers caractères du texte

## Utilisation
```bash
echo "votre texte" | python texttool.py <operation>
```

## Exemples
```bash
echo "Bonjour le monde" | python texttool.py upper
# Résultat: BONJOUR LE MONDE

echo "HELLO WORLD" | python texttool.py lower
# Résultat: hello world

echo "Bonjour le monde" | python texttool.py length
# Résultat: 16

echo "Bonjour le monde" | python texttool.py count-words
# Résultat: 3

echo "Bonjour le monde" | python texttool.py prefix
# Résultat: Bonjour le
```
