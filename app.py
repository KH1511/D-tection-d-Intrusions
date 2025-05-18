import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement du modèle XGBoost préalablement entraîné
@st.cache_resource
def load_model():
    with open("XGBoost_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Colonnes attendues par le modèle (41 colonnes sans 'attack' et 'level')
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate']

# Dictionnaire des attaques
attack_names = {
    0: 'normal', 1: 'neptune', 2: 'warezclient', 3: 'satan', 4: 'ipsweep', 5: 'smurf', 6: 'teardrop',
    7: 'pod', 8: 'back', 9: 'land', 10: 'ftp_write', 11: 'guess_passwd', 12: 'imap', 13: 'multihop',
    14: 'phf', 15: 'spy', 16: 'warezmaster', 17: 'snmpgetattack', 18: 'httptunnel', 19: 'sendmail',
    20: 'named', 21: 'smokeping', 22: 'buffer_overflow', 23: 'loadmodule', 24: 'perl', 25: 'rootkit',
    26: 'sqlattack', 27: 'xterm', 28: 'ps', 29: 'apache2', 30: 'netcat', 31: 'satan', 32: 'nmap',
    33: 'rpc', 34: 'spybot', 35: 'wget', 36: 'unreachable', 37: 'kerberos', 38: 'phf',
    39: 'cross_site_scripting', 40: 'infiniband'
}

# Interface Streamlit
st.title("🔐 Interface de Détection d'Intrusions")

uploaded_file = st.file_uploader("📁 Importer un fichier CSV contenant des données réseau", type="csv")

if uploaded_file:
    try:
        # Lire les données
        data = pd.read_csv(uploaded_file, header=None)

        # Vérification du nombre de colonnes
        if data.shape[1] == len(columns):
            data.columns = columns
        else:
            st.error(f"Erreur : Le fichier CSV a {data.shape[1]} colonnes, mais on attend {len(columns)} colonnes.")
            st.stop()

        # Aperçu des données
        st.subheader("📊 Aperçu des données importées")
        st.dataframe(data.head())

        # Colonnes catégorielles
        categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

        # Encodage
        le = LabelEncoder()
        for col in categorical_columns:
            data[col] = le.fit_transform(data[col])

        # Vérification post-encodage
        if data.select_dtypes(include=['object']).shape[1] > 0:
            st.error("❌ Il y a encore des colonnes catégorielles non encodées.")
            st.stop()

        # Prédictions
        X = data
        attack_predictions = model.predict(X)
        attack_names_predictions = [attack_names.get(pred, "Inconnue") for pred in attack_predictions]

        # Résultats
        result_df = data.copy()
        result_df['attack'] = attack_names_predictions

        # Affichage des résultats
        st.subheader("🔍 Résultats des prédictions")
        st.dataframe(result_df)

        # 📈 Diagramme des types d'attaques
        st.subheader("📈 Diagramme des types d'attaques détectés")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='attack', data=result_df, hue='attack', palette='Set2', ax=ax)
        ax.set_title("Distribution des types d'attaques détectés", fontsize=20, weight='bold', color='darkblue')
        ax.set_xlabel("Type d'attaque", fontsize=15, color='black')
        ax.set_ylabel("Nombre", fontsize=15, color='black')
        plt.xticks(rotation=45, fontsize=12, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(fig)

        # 📥 Bouton de téléchargement
        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger les résultats au format CSV", data=csv, file_name='predictions.csv')

    except Exception as e:
        st.error(f"Erreur lors du traitement : {e}")
