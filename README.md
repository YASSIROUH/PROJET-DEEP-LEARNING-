# Projets de Deep Learning - EMSI

Bienvenue dans ce dépôt ! Ce projet regroupe différentes implémentations d'architectures de réseaux de neurones (MLP, CNN, RNN/LSTM/GRU/Seq2Seq) développées avec PyTorch. 

L'objectif est d'explorer progressivement le Deep Learning, de la classification de données tabulaires au traitement du langage naturel (NLP) en passant par la vision par ordinateur.

---

## 📑 Contenu Détaillé du Repository

### 📓 1. Multilayer Perceptron (MLP)
**Fichier :** `Partie1_MLP_PyTorch_EMSI.ipynb`

Dans cette première partie, l'objectif est de maîtriser les concepts fondamentaux des réseaux de neurones denses.
- **Jeu de données :** *Breast Cancer Wisconsin* de scikit-learn (Classification binaire : tumeurs malignes vs bénignes à partir de 30 variables).
- **Architecture :** Un réseau de neurones multicouches personnalisé (30 -> 64 -> 32 -> 2) avec fonctions d'activation ReLU.
- **Concepts clés :** Prétraitement et normalisation (StandardScaler), test de différentes initialisations de poids (Xavier, He), boucle d'entraînement PyTorch (Adam, CrossEntropyLoss), et évaluation (Accuracy, Precision, Recall, F1 Score).

### 🖼️ 2. Réseaux de Neurones Convolutifs (CNN)
**Fichier :** `Partie2_CNN_Vision_EMSI.ipynb`

Cette partie est dédiée à la vision par ordinateur (Computer Vision) pour la classification d'images.
- **Jeu de données :** *FashionMNIST* de torchvision (Classification de vêtements en 10 catégories, images en niveaux de gris 28x28).
- **Architecture :** Classe `CNN` comprenant deux couches de convolutions (`Conv2d`) suivies de Max Pooling (`MaxPool2d`) et de couches linéaires denses (Fully Connected).
- **Concepts clés :** Transformation des données en tenseurs, architectures convolutives pour l'extraction de caractéristiques d'images, et manipulation des DataLoaders.

### 📝 3. Réseaux Récurrents (RNN, LSTM, GRU) et Seq2Seq
**Fichier :** `Partie3_RNN_LSTM_GRU_Seq2Seq_EMSI.ipynb`

Ici, on s'attaque au traitement de données séquentielles, tout particulièrement appliqué au texte (NLP).
- **Jeu de données :** Petit dataset textuel personnalisé pour l'analyse de sentiment (classification binaire : phrases positives/négatives).
- **Architectures :** 
  - `RNNModel` (Utilisation de `nn.RNN`)
  - `LSTMModel` (Utilisation de `nn.LSTM`)
  - `GRUModel` (Utilisation de `nn.GRU`)
  - Initiation modèle Encodeur pour une architecture *Sequence-to-Sequence (Seq2Seq)*.
- **Concepts clés :** Création d'un vocabulaire manuel, tokenisation, encodage des séquences, ajout de *Padding*, et utilisation de couches d'`Embedding`.

---

## 💾 Modèles Sauvegardés (`.pth`)

Pendant l'entraînement, les meilleurs poids ont été enregistrés localement. Vous pouvez les recharger via la méthode `model.load_state_dict()` de PyTorch :
- `best_model.pth` : Poids du meilleur modèle MLP.
- `best_model_he_init.pth` : Poids du MLP utilisant l'initialisation de He.
- `best_model_xavier_init.pth` : Poids du MLP utilisant l'initialisation de Xavier.
- `cnn_model.pth` : Modèle Convolutif entraîné sur le dataset FashionMNIST.
- `lstm_model.pth` : Modèle LSTM entraîné sur l'analyse de sentiment de la partie 3.

---

## 📁 Architecture du Dossier

- **`data/`** : Répertoire prévu pour sauvegarder les téléchargements de datasets (comme les images de FashionMNIST).
- **`.venv/`** : L'environnement virtuel Python du projet.

---

## 🚀 Guide de Démarrage

1. **Activation de l'environnement virtuel** :
   ```bash
   # Sous Windows
   .venv\Scripts\activate
   ```
2. **Installation des dépendances** (si nécessaire) :
   Assurez-vous d'avoir installé `torch`, `torchvision`, `numpy`, `pandas`, `scikit-learn` et `matplotlib`.
3. **Lancement de Jupyter** :
   ```bash
   jupyter notebook
   ```
4. **Exécution** :
   Sélectionnez simplement l'un des trois notebooks (`Partie1_...`, `Partie2_...`, ou `Partie3_...`) et lancez les cellules séquentiellement pour voir les modèles s'entraîner !
