# DragonBallGame

## Description

**DragonBallGame** est un projet en Python inspiré de l'univers de Dragon Ball. Il s'agit d'un jeu où les joueurs peuvent créer et entraîner des guerriers, participer à des combats, et affronter une série de boss pour tester leurs compétences. Le jeu implémente divers design patterns pour gérer la création des personnages, les techniques, les objets spéciaux, ainsi que les évolutions de combat. Le projet a été cree dans le but dapprendre les design pattern

### Fonctionnalités principales :

- **Création de guerriers** : Choix du nom, du type, et des techniques de base.
- **Système d'entraînement** : Amélioration des compétences des guerriers via un système basé sur le pattern Decorator.
- **Système de combat** : Combat tour par tour contre un ennemie avec une mécanique de "Amelioration" en function de son perso pour booster les stats du joueur.
- **Gestion des objets spéciaux** : Utilisation d'objets comme les SenzuBeans pour guérir et autres objets spéciaux pour améliorer les capacités.
- **Entraînement personnalisé** : Possibilité de choisir les techniques à améliorer au fil du jeu.

## Installation

### Prérequis

- **Python 3.10+**

Aucune dependance n'est neccesaire

## Lancer le projet

Clone le dépôt GitHub puis lance le jeu :

```bash
git clone https://github.com/math-pixel/DragonBallGame.git
cd DragonBallGame
python main.py
```

### Flux utilisateur

1. **Écran d'accueil** : "Bienvenue dans DragonBallGame"
2. **Création de personnage** : Choisis le type de guerrier, saisis le nom,  et un object special.
3. **Menu principal** :
   - 1. Combattre
   - 2. S'entraîner
   - 3. Quitter

## Fonctionnement des combats

Les combats sont basés sur un système au tour par tour où tu affrontes un ennemie a la fois. Chaque combat commence avec le choix d'attaquer, d'utiliser un objet, ou d'activer la "transformation". Gagne les combats pour faire évoluer ton personnage !

## Design patterns utilisés

Ce projet implémente plusieurs patterns de conception :

- **Singleton** : Pour gérer la salle du temps alias le training.
- **Factory** : Pour la création des guerriers.
- **Builder** : Pour la construction des personnages et de leurs capacités.
- **State** : Pour gérer les etat des guerriers et leur evolution.
- **Decorator** : Pour appliquer des boost a lentrainement et avoir un entrainement plus approfondie.
- **Observer** : Alerte l'arene si un combat est fini.
- **Command, Composite, Memento, Proxy** (en option pour futures améliorations).

## Contributions

Les contributions sont les bienvenues ! Si tu souhaites ajouter de nouvelles fonctionnalités ou améliorer le code existant, n'hésite pas à ouvrir une issue ou une pull request.