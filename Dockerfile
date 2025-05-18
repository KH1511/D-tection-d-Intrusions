# Étape 1 : Image de base légère avec Python
FROM python:3.10-slim

# Étape 2 : Répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers dans le conteneur
COPY requirements.txt .
COPY app.py .
COPY XGBoost_model.pkl .

# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port utilisé par Streamlit
EXPOSE 8501

# Étape 6 : Lancer l'application
CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.port=8501"]
