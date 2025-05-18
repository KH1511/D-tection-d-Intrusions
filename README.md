
# 🔐 Détection d'Intrusions avec XGBoost et Streamlit

Ce projet propose une interface intuitive de détection d'intrusions réseau basée sur le jeu de données **NSL-KDD**. Il utilise un modèle **XGBoost** pré-entraîné pour prédire les types d'attaques et affiche les résultats de manière interactive grâce à **Streamlit**.

## 📁 Structure du Projet

├── app.py # Interface Streamlit
├── generate-dataset.py # Script pour générer un fichier CSV de test
├── test_data.csv # Fichier csv generé par generate-dataset.py
├── XGBoost_model.pkl # Modèle IA entraîné (XGBoost)
├── requirements.txt # Dépendances pour l'environnement Python
├── Dockerfile # Pour le déploiement via Docker
├── README.md # Ce fichier


## 🚀 Démarrer l'application

### 🔧 1. Cloner le dépôt

```bash
git clone https://github.com/KH1511/D-tection-d-Intrusions.git
cd D-tection-d-Intrusions
2. Installer les dépendances (sans Docker)
Crée un environnement virtuel si souhaité :

python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
Installe les paquets requis :

pip install -r requirements.txt

3. Lancer l’application Streamlit

streamlit run app.py

Déploiement avec Docker
Construction de l’image Docker

docker build -t detection-intrusion-app .

Lancement du conteneur

docker run -p 8501:8501 detection-intrusion-app
L'application sera accessible sur http://localhost:8501

🧠 Description du modèle IA
Le modèle utilisé est XGBoost, entraîné sur le dataset NSL-KDD, permettant la classification de différentes attaques réseau.

Entrées : 41 caractéristiques du réseau

Sortie : Type d'attaque (normal, neptune, smurf, etc.)

Génération de données de test
Un script generate-dataset.py est fourni pour générer un fichier .csv de test. Il simule les données d'entrée attendues par le modèle.

python generate-dataset.py
Un fichier test_data.csv sera généré pour être utilisé avec l'interface.

Fonctionnalités de l'interface
Import d’un fichier CSV

Affichage des données

Encodage automatique des variables catégorielles

Prédiction du type d’attaque

Diagramme de distribution des attaques

Téléchargement des résultats

Fichier requirements.txt
Extrait des dépendances utilisées :


streamlit
pandas
scikit-learn
xgboost
seaborn
matplotlib

