# -*- coding: utf-8 -*-
"""
Génération du rapport PDF complet — Projet Deep Learning EMSI 2025-2026
Couvre les 3 parties : MLP, CNN, RNN/LSTM/GRU/Seq2Seq
"""

from fpdf import FPDF
import os

class RapportPDF(FPDF):
    """Classe personnalisée pour le rapport PDF."""

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "Projet Deep Learning - EMSI 2025-2026", align="C")
            self.ln(4)
            self.set_draw_color(0, 102, 204)
            self.set_line_width(0.5)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(6)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-20)
            self.set_draw_color(0, 102, 204)
            self.set_line_width(0.3)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(3)
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def titre_principal(self, texte):
        self.set_font("Helvetica", "B", 24)
        self.set_text_color(0, 51, 153)
        self.multi_cell(0, 14, texte, align="C")
        self.ln(4)

    def sous_titre_principal(self, texte):
        self.set_font("Helvetica", "", 14)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 10, texte, align="C")
        self.ln(2)

    def titre_partie(self, numero, texte):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(0, 102, 204)
        self.multi_cell(0, 12, f"Partie {numero} - {texte}")
        self.ln(2)
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def titre_section(self, texte):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 51, 102)
        self.multi_cell(0, 10, texte)
        self.ln(2)

    def titre_sous_section(self, texte):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(51, 51, 51)
        self.multi_cell(0, 8, texte)
        self.ln(2)

    def paragraphe(self, texte):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6, texte)
        self.ln(3)

    def point_liste(self, texte):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        x = self.get_x()
        self.cell(8, 6, chr(8226))  # bullet point
        self.multi_cell(0, 6, texte)
        self.ln(1)

    def code_block(self, texte):
        self.set_font("Courier", "", 8)
        self.set_text_color(0, 0, 0)
        self.set_fill_color(240, 240, 245)
        # Calculer la hauteur
        lines = texte.split("\n")
        for line in lines:
            self.cell(0, 5, line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def tableau_simple(self, headers, rows):
        """Dessine un tableau simple."""
        nb_cols = len(headers)
        col_w = (self.w - 20) / nb_cols

        # En-tetes
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(0, 102, 204)
        self.set_text_color(255, 255, 255)
        for h in headers:
            self.cell(col_w, 8, h, border=1, fill=True, align="C")
        self.ln()

        # Lignes
        self.set_font("Helvetica", "", 9)
        self.set_text_color(30, 30, 30)
        fill = False
        for row in rows:
            if fill:
                self.set_fill_color(230, 240, 255)
            else:
                self.set_fill_color(255, 255, 255)
            for cell_val in row:
                self.cell(col_w, 7, str(cell_val), border=1, fill=True, align="C")
            self.ln()
            fill = not fill
        self.ln(4)

    def info_box(self, texte):
        """Boite d'information mise en evidence."""
        self.set_fill_color(230, 245, 255)
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.3)
        y = self.get_y()
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(0, 51, 102)
        self.multi_cell(0, 6, texte, border=1, fill=True)
        self.ln(4)


def generer_rapport():
    pdf = RapportPDF()
    pdf.alias_nb_pages()

    # ===== PAGE DE GARDE =====
    pdf.add_page()
    
    # Logo EMSI
    logo_path = os.path.join(os.path.dirname(__file__), "emsi_logo.png")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=65, y=20, w=80)
        pdf.ln(50)
    else:
        pdf.ln(40)
        
    pdf.titre_principal("Rapport de Projet")
    pdf.titre_principal("Deep Learning")
    pdf.ln(10)
    pdf.sous_titre_principal("EMSI - Annee Universitaire 2025-2026")
    pdf.ln(15)

    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 8, (
        "Ce rapport presente les travaux realises dans le cadre du projet\n"
        "de Deep Learning. Il couvre trois parties principales :\n\n"
        "Partie I : MLP et PyTorch\n"
        "Partie II : CNN et Vision par Ordinateur\n"
        "Partie III : RNN, LSTM, GRU et Seq2Seq"
    ), align="C")

    pdf.ln(20)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 8, "Elabore par : Yassir Ouahla", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Technologies utilisees : Python, PyTorch, scikit-learn, NumPy, Matplotlib", align="C")

    # ===== TABLE DES MATIERES =====
    pdf.add_page()
    pdf.titre_principal("Table des Matieres")
    pdf.ln(5)

    toc = [
        ("Partie I - MLP et PyTorch", [
            "1.1 Objectif",
            "1.2 Dataset : Breast Cancer Wisconsin",
            "1.3 Preprocessing des donnees",
            "1.4 Architecture du MLP",
            "1.5 Entrainement et evaluation",
            "1.6 Comparaison des techniques d'initialisation",
            "1.7 Analyse critique et conclusion",
        ]),
        ("Partie II - CNN et Vision par Ordinateur", [
            "2.1 Objectif",
            "2.2 Dataset : Fashion-MNIST",
            "2.3 Operations fondamentales (Convolution, Pooling)",
            "2.4 Architecture du CNN",
            "2.5 Entrainement et evaluation",
            "2.6 Analyse critique et conclusion",
        ]),
        ("Partie III - RNN, LSTM, GRU et Seq2Seq", [
            "3.1 Objectif",
            "3.2 Dataset : 20 Newsgroups",
            "3.3 Pretraitement du texte et vocabulaire",
            "3.4 Architectures : RNN, LSTM, GRU",
            "3.5 Entrainement et comparaison",
            "3.6 Mini modele Seq2Seq",
            "3.7 Analyse critique et conclusion",
        ]),
    ]

    for partie_title, sections in toc:
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(0, 51, 153)
        pdf.cell(0, 10, partie_title, new_x="LMARGIN", new_y="NEXT")
        for sec in sections:
            pdf.set_font("Helvetica", "", 11)
            pdf.set_text_color(60, 60, 60)
            pdf.cell(15, 7, "")
            pdf.cell(0, 7, sec, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(3)

    # ==========================================
    # PARTIE I : MLP et PyTorch
    # ==========================================
    pdf.add_page()
    pdf.titre_partie("I", "MLP et PyTorch")

    pdf.titre_section("1.1 Objectif")
    pdf.paragraphe(
        "Dans cette premiere partie, l'objectif est de :\n"
        "- Preparer un dataset tabulaire reel pour la classification binaire\n"
        "- Construire un Perceptron Multicouche (MLP) avec PyTorch\n"
        "- Entrainer et evaluer le modele avec des metriques pertinentes\n"
        "- Comparer differentes techniques d'initialisation des poids\n"
        "- Sauvegarder et recharger le modele entraine"
    )

    pdf.titre_section("1.2 Dataset : Breast Cancer Wisconsin")
    pdf.paragraphe(
        "Le dataset utilise est le Breast Cancer Wisconsin, disponible via scikit-learn. "
        "Il contient 569 echantillons avec 30 caracteristiques numeriques chacun. "
        "La tache consiste a classer les tumeurs comme malignes (0) ou benignes (1)."
    )
    pdf.tableau_simple(
        ["Propriete", "Valeur"],
        [
            ["Nombre d'echantillons", "569"],
            ["Nombre de features", "30"],
            ["Classes", "2 (malin, benin)"],
            ["Split Train/Test", "80% / 20%"],
            ["Stratification", "Oui"],
        ]
    )

    pdf.titre_section("1.3 Preprocessing des donnees")
    pdf.paragraphe(
        "Les etapes de preprocessing appliquees sont :\n"
        "- Separation train/test (80/20) avec stratification\n"
        "- Normalisation avec StandardScaler (moyenne=0, ecart-type=1)\n"
        "- Conversion en tenseurs PyTorch (float32 pour X, long pour y)\n"
        "- Envoi vers le device (CPU ou GPU)"
    )
    pdf.info_box(
        "La normalisation est essentielle pour la stabilite de l'apprentissage "
        "car les features ont des echelles tres differentes (ex: mean radius vs mean fractal dimension)."
    )

    pdf.titre_section("1.4 Architecture du MLP")
    pdf.paragraphe(
        "Le modele MLP est defini comme une classe heritant de nn.Module avec :"
    )
    pdf.tableau_simple(
        ["Couche", "Entree", "Sortie", "Activation"],
        [
            ["fc1 (Linear)", "30", "64", "ReLU"],
            ["fc2 (Linear)", "64", "32", "ReLU"],
            ["fc3 (Linear)", "32", "2", "-"],
        ]
    )
    pdf.paragraphe(
        "Fonction de cout : CrossEntropyLoss\n"
        "Optimiseur : Adam (lr=0.001)\n"
        "Nombre d'epochs : 100"
    )

    pdf.titre_section("1.5 Entrainement et Evaluation")
    pdf.paragraphe(
        "Le modele est entraine pendant 100 epochs. Les resultats montrent une "
        "convergence rapide de la loss et une accuracy d'entrainement atteignant 99.12% "
        "a l'epoch 100."
    )

    pdf.titre_sous_section("Resultats sur le jeu de test")
    pdf.tableau_simple(
        ["Metrique", "Valeur"],
        [
            ["Accuracy", "0.9561"],
            ["Precision", "0.9718"],
            ["Recall", "0.9583"],
            ["F1-Score", "0.9650"],
        ]
    )
    pdf.paragraphe(
        "La matrice de confusion montre que le modele classe correctement la grande "
        "majorite des echantillons, avec tres peu de faux positifs et faux negatifs."
    )

    pdf.titre_section("1.6 Comparaison des Techniques d'Initialisation")
    pdf.paragraphe(
        "Quatre techniques d'initialisation ont ete comparees sur le meme modele MLP :"
    )
    pdf.tableau_simple(
        ["Initialisation", "Test Accuracy", "Test Precision", "Test Recall", "Test F1"],
        [
            ["Xavier", "0.9561", "0.9718", "0.9583", "0.9650"],
            ["He (Kaiming)", "0.9386", "0.9851", "0.9167", "0.9496"],
            ["Random Uniform", "0.9298", "0.9324", "0.9583", "0.9452"],
            ["Normal", "0.9298", "0.9444", "0.9444", "0.9444"],
        ]
    )
    pdf.paragraphe(
        "L'initialisation Xavier donne les meilleurs resultats globaux. "
        "L'initialisation He est optimisee pour ReLU et montre la meilleure precision. "
        "Les initialisations aleatoires (Random et Normal) sont les moins performantes."
    )

    pdf.titre_section("1.7 Analyse Critique et Conclusion")
    pdf.paragraphe(
        "Cette implementation demontre qu'un MLP constitue une solution efficace "
        "pour la classification de donnees tabulaires. Les points cles sont :\n\n"
        "- L'importance du preprocessing (normalisation)\n"
        "- Le role crucial de l'initialisation des poids\n"
        "- L'impact des fonctions d'activation\n"
        "- L'utilisation correcte de PyTorch et de l'API nn.Module\n\n"
        "Le modele sauvegarde peut etre recharge et reutilise pour des predictions "
        "futures, demontrant la persistance des modeles PyTorch."
    )

    # ==========================================
    # PARTIE II : CNN et Vision par Ordinateur
    # ==========================================
    pdf.add_page()
    pdf.titre_partie("II", "CNN et Vision par Ordinateur")

    pdf.titre_section("2.1 Objectif")
    pdf.paragraphe(
        "Cette deuxieme partie vise a :\n"
        "- Comprendre les operations de convolution et de pooling\n"
        "- Construire un CNN (Convolutional Neural Network) avec PyTorch\n"
        "- Entrainer le modele sur un dataset d'images reelles\n"
        "- Evaluer et analyser les performances"
    )

    pdf.titre_section("2.2 Dataset : Fashion-MNIST")
    pdf.paragraphe(
        "Le dataset Fashion-MNIST est utilise, contenant 70 000 images en niveaux "
        "de gris de 28x28 pixels reparties en 10 categories de vetements et accessoires."
    )
    pdf.tableau_simple(
        ["Propriete", "Valeur"],
        [
            ["Train samples", "60 000"],
            ["Test samples", "10 000"],
            ["Taille des images", "28 x 28 x 1"],
            ["Nombre de classes", "10"],
            ["Batch size", "64"],
        ]
    )
    pdf.paragraphe(
        "Les 10 categories sont : T-shirt, Trouser, Pullover, Dress, Coat, "
        "Sandal, Shirt, Sneaker, Bag, Ankle boot."
    )

    pdf.titre_section("2.3 Operations Fondamentales")
    pdf.titre_sous_section("Convolution 2D (corr2d)")
    pdf.paragraphe(
        "Une implementation manuelle de la correlation croisee 2D a ete realisee "
        "pour illustrer le fonctionnement des filtres convolutionnels. Cette operation "
        "applique un noyau (kernel) sur une matrice d'entree pour extraire des features."
    )
    pdf.titre_sous_section("Max Pooling 2D")
    pdf.paragraphe(
        "Le max pooling reduit la dimension spatiale en gardant la valeur maximale "
        "dans chaque fenetre. Cela permet de reduire les parametres et d'apporter "
        "une invariance aux petites translations."
    )

    pdf.titre_section("2.4 Architecture du CNN")
    pdf.paragraphe(
        "Le CNN utilise l'architecture suivante :"
    )
    pdf.tableau_simple(
        ["Couche", "Configuration", "Sortie"],
        [
            ["Conv2d #1", "1->32 filtres, 3x3, pad=1", "32 x 28 x 28"],
            ["ReLU + MaxPool", "2x2", "32 x 14 x 14"],
            ["Conv2d #2", "32->64 filtres, 3x3, pad=1", "64 x 14 x 14"],
            ["ReLU + MaxPool", "2x2", "64 x 7 x 7"],
            ["Flatten", "-", "3136"],
            ["Linear #1", "3136 -> 128", "128"],
            ["ReLU", "-", "128"],
            ["Linear #2", "128 -> 10", "10"],
        ]
    )

    pdf.titre_section("2.5 Entrainement et Evaluation")
    pdf.paragraphe(
        "Le modele est entraine pendant 5 epochs avec Adam (lr=0.001) et CrossEntropyLoss."
    )
    pdf.tableau_simple(
        ["Epoch", "Loss", "Train Accuracy"],
        [
            ["1", "0.4713", "82.93%"],
            ["2", "0.2969", "89.24%"],
            ["3", "0.2500", "90.80%"],
            ["4", "0.2237", "91.80%"],
            ["5", "0.1957", "92.77%"],
        ]
    )
    pdf.paragraphe(
        "Test Accuracy finale : ~91.5%\n\n"
        "Le modele montre une convergence rapide et atteint de bonnes performances "
        "en seulement 5 epochs. Le classification report detaille montre des variations "
        "de performance selon les categories, certaines (comme Trouser) etant plus faciles "
        "a classifier que d'autres (comme Shirt)."
    )

    pdf.titre_section("2.6 Analyse Critique et Conclusion")
    pdf.paragraphe(
        "Points positifs :\n"
        "- Le CNN extrait automatiquement des features spatiales pertinentes\n"
        "- Performance elevee avec une architecture relativement simple\n"
        "- Convergence rapide grace a Adam et au batch processing\n\n"
        "Limites :\n"
        "- Pas d'augmentation de donnees appliquee\n"
        "- Architecture simple (2 couches conv) - des architectures plus profondes "
        "(ResNet, VGG) pourraient ameliorer les resultats\n"
        "- Pas de regularisation (Dropout, BatchNorm)\n\n"
        "Le modele CNN est sauvegarde et peut etre recharge pour une utilisation future."
    )

    # ==========================================
    # PARTIE III : RNN, LSTM, GRU et Seq2Seq
    # ==========================================
    pdf.add_page()
    pdf.titre_partie("III", "RNN, LSTM, GRU et Seq2Seq")

    pdf.titre_section("3.1 Objectif")
    pdf.paragraphe(
        "Cette troisieme partie vise a :\n"
        "- Comprendre les modeles sequentiels (RNN, LSTM, GRU)\n"
        "- Preparer des donnees textuelles reelles\n"
        "- Implementer et comparer les trois architectures\n"
        "- Construire un mini systeme Seq2Seq"
    )

    pdf.titre_section("3.2 Dataset : 20 Newsgroups")
    pdf.paragraphe(
        "Le dataset 20 Newsgroups de scikit-learn est utilise. Il contient environ "
        "18 846 messages provenant de 20 groupes de discussion Usenet. "
        "Pour cette tache de classification, 4 categories sont selectionnees :"
    )
    pdf.tableau_simple(
        ["Categorie", "Domaine"],
        [
            ["sci.space", "Science / Espace"],
            ["rec.sport.hockey", "Sport / Hockey"],
            ["comp.graphics", "Informatique / Graphisme"],
            ["talk.politics.mideast", "Politique / Moyen-Orient"],
        ]
    )
    pdf.paragraphe(
        "Le nettoyage automatique des metadonnees (headers, footers, quotes) est applique "
        "lors du chargement pour eviter les biais."
    )
    pdf.info_box(
        "Ce dataset reel contient ~2 300 echantillons d'entrainement et ~1 500 de test, "
        "ce qui constitue un defi plus realiste qu'un petit dataset synthetique."
    )

    pdf.titre_section("3.3 Pretraitement du Texte et Vocabulaire")
    pdf.paragraphe(
        "Les etapes de pretraitement sont :\n"
        "1. Conversion en minuscules\n"
        "2. Suppression des caracteres speciaux et chiffres (regex)\n"
        "3. Tokenisation par mots\n"
        "4. Filtrage des mots trop courts (< 2 caracteres)\n"
        "5. Construction du vocabulaire (mots freq >= 2)\n"
        "6. Encodage en sequences d'indices avec padding/troncature\n\n"
        "Le vocabulaire contient plusieurs milliers de mots. "
        "L'index 0 est reserve au padding (<PAD>) et l'index 1 aux mots inconnus (<UNK>). "
        "La longueur maximale des sequences est fixee a 200 tokens."
    )

    pdf.titre_section("3.4 Architectures : RNN, LSTM, GRU")
    pdf.paragraphe(
        "Les trois architectures partagent une structure commune :"
    )
    pdf.tableau_simple(
        ["Composant", "Configuration"],
        [
            ["Embedding", "vocab_size x 64"],
            ["Couche recurrente", "64 -> 128 (2 layers)"],
            ["Dropout", "0.3"],
            ["Linear", "128 -> 4 (classes)"],
        ]
    )

    pdf.titre_sous_section("Differences entre les architectures")
    pdf.tableau_simple(
        ["Critere", "RNN", "LSTM", "GRU"],
        [
            ["Complexite", "Faible", "Elevee", "Moyenne"],
            ["Parametres", "Le moins", "Le plus", "Intermediaire"],
            ["Memoire long terme", "Mauvaise", "Tres bonne", "Bonne"],
            ["Vanishing gradient", "Problematique", "Resolu", "Resolu"],
            ["Vitesse", "Rapide", "Lente", "Intermediaire"],
        ]
    )

    pdf.titre_section("3.5 Entrainement et Comparaison")
    pdf.paragraphe(
        "Les trois modeles sont entraines pendant 15 epochs avec :\n"
        "- Optimiseur : Adam (lr=0.001)\n"
        "- Fonction de cout : CrossEntropyLoss\n"
        "- Gradient clipping (max_norm=1.0)\n"
        "- Batch size : 64\n\n"
        "Le gradient clipping est essentiel pour stabiliser l'entrainement "
        "des modeles recurrents et eviter l'explosion du gradient."
    )
    pdf.paragraphe(
        "Les resultats montrent generalement que le LSTM et le GRU obtiennent "
        "de meilleures performances que le RNN simple, grace a leurs mecanismes "
        "de portes (gates) qui controlent le flux d'information."
    )
    pdf.paragraphe(
        "L'evaluation detaillee inclut le classification report (precision, recall, f1 par classe), "
        "les matrices de confusion, et les courbes de loss/accuracy."
    )
    pdf.titre_sous_section("Tableau Comparatif des Performances")
    pdf.tableau_simple(
        ["Modele", "Parametres", "Train Acc", "Test Acc", "Train Loss"],
        [
            ["RNN", "1,122,180", "43.70%", "28.69%", "1.0833"],
            ["LSTM", "1,295,748", "50.19%", "42.23%", "1.0858"],
            ["GRU", "1,237,892", "59.16%", "47.75%", "0.9763"],
        ]
    )

    pdf.titre_section("3.6 Mini Modele Seq2Seq")
    pdf.paragraphe(
        "Un modele Seq2Seq (Sequence-to-Sequence) est implemente avec un "
        "encodeur et un decodeur bases sur LSTM."
    )
    pdf.titre_sous_section("Architecture")
    pdf.paragraphe(
        "Encodeur : Embedding + LSTM (32 dim, 64 hidden)\n"
        "Decodeur : Embedding + LSTM (32 dim, 64 hidden) + Linear\n"
        "Teacher forcing ratio : 0.5"
    )
    pdf.titre_sous_section("Tache")
    pdf.paragraphe(
        "La tache choisie est l'inversion de sequences de nombres (1-9). "
        "Par exemple :\n"
        "- Entree :  [3, 7, 1, 5, 2]\n"
        "- Sortie :  [2, 5, 1, 7, 3]\n\n"
        "Le modele est entraine sur 5 000 sequences et teste sur 500. "
        "Apres 30 epochs, il atteint une accuracy par token elevee, "
        "montrant la capacite du Seq2Seq a apprendre des transformations "
        "sequentielles."
    )

    pdf.titre_section("3.7 Analyse Critique et Conclusion")
    pdf.paragraphe(
        "Avantages des LSTM / GRU :\n"
        "- Bonne gestion des dependances a long terme\n"
        "- Mecanisme de portes controlant le flux d'information\n"
        "- Reduction significative du vanishing gradient\n"
        "- Le GRU est plus leger que le LSTM avec des performances comparables\n\n"
        "Limites :\n"
        "- Temps d'entrainement eleve\n"
        "- Traitement sequentiel (pas de parallelisation comme les Transformers)\n"
        "- Difficultes sur les tres longues sequences\n"
        "- Sensibilite aux hyperparametres"
    )

    # ===== CONCLUSION GENERALE =====
    pdf.add_page()
    pdf.titre_partie("", "Conclusion Generale")
    pdf.paragraphe(
        "Ce projet de Deep Learning couvre trois familles fondamentales "
        "de reseaux de neurones profonds :\n\n"
        "1. Les MLP (Perceptrons Multicouches) pour les donnees tabulaires, "
        "demonstrant l'importance du preprocessing et de l'initialisation des poids.\n\n"
        "2. Les CNN (Reseaux de Neurones Convolutionnels) pour la vision par ordinateur, "
        "montrant la puissance de l'extraction automatique de features spatiales.\n\n"
        "3. Les RNN/LSTM/GRU pour les donnees sequentielles textuelles, "
        "illustrant les avantages des mecanismes de memoire pour la classification de texte, "
        "ainsi que le paradigme Seq2Seq pour les transformations sequence-a-sequence.\n\n"
        "Chaque partie utilise des datasets reels et des methodologies rigoureuses "
        "d'evaluation, incluant des metriques variees (accuracy, precision, recall, F1), "
        "des visualisations (courbes de loss/accuracy, matrices de confusion), "
        "et des comparaisons entre differentes configurations.\n\n"
        "Les outils utilises (PyTorch, scikit-learn, NumPy, Matplotlib) constituent "
        "un ecosysteme complet et professionnel pour le Deep Learning en Python."
    )

    # ===== SAUVEGARDE =====
    output_path = os.path.join(os.path.dirname(__file__), "Rapport_Deep_Learning_EMSI.pdf")
    pdf.output(output_path)
    print(f"Rapport genere avec succes : {output_path}")


if __name__ == "__main__":
    generer_rapport()
