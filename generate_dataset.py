import pandas as pd
import numpy as np

# Colonnes attendues par le modèle
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate']

# Générer des données simulées
n_samples = 100  # Nombre d'exemples pour tester

data = {
    'duration': np.random.randint(0, 2000, size=n_samples),
    'protocol_type': np.random.choice(['tcp', 'udp', 'icmp'], size=n_samples),
    'service': np.random.choice(['http', 'ftp', 'smtp', 'dns', 'telnet'], size=n_samples),
    'flag': np.random.choice(['SF', 'S0', 'REJ'], size=n_samples),
    'src_bytes': np.random.randint(0, 5000, size=n_samples),
    'dst_bytes': np.random.randint(0, 5000, size=n_samples),
    'land': np.random.choice([0, 1], size=n_samples),
    'wrong_fragment': np.random.randint(0, 100, size=n_samples),
    'urgent': np.random.randint(0, 10, size=n_samples),
    'hot': np.random.randint(0, 100, size=n_samples),
    'num_failed_logins': np.random.randint(0, 10, size=n_samples),
    'logged_in': np.random.choice([0, 1], size=n_samples),
    'num_compromised': np.random.randint(0, 10, size=n_samples),
    'root_shell': np.random.choice([0, 1], size=n_samples),
    'su_attempted': np.random.randint(0, 5, size=n_samples),
    'num_root': np.random.randint(0, 5, size=n_samples),
    'num_file_creations': np.random.randint(0, 10, size=n_samples),
    'num_shells': np.random.randint(0, 5, size=n_samples),
    'num_access_files': np.random.randint(0, 10, size=n_samples),
    'num_outbound_cmds': np.random.randint(0, 10, size=n_samples),
    'is_host_login': np.random.choice([0, 1], size=n_samples),
    'is_guest_login': np.random.choice([0, 1], size=n_samples),
    'count': np.random.randint(0, 500, size=n_samples),
    'srv_count': np.random.randint(0, 500, size=n_samples),
    'serror_rate': np.random.uniform(0, 1, size=n_samples),
    'srv_serror_rate': np.random.uniform(0, 1, size=n_samples),
    'rerror_rate': np.random.uniform(0, 1, size=n_samples),
    'srv_rerror_rate': np.random.uniform(0, 1, size=n_samples),
    'same_srv_rate': np.random.uniform(0, 1, size=n_samples),
    'diff_srv_rate': np.random.uniform(0, 1, size=n_samples),
    'srv_diff_host_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_count': np.random.randint(0, 500, size=n_samples),
    'dst_host_srv_count': np.random.randint(0, 500, size=n_samples),
    'dst_host_same_srv_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_diff_srv_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_same_src_port_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_srv_diff_host_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_serror_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_srv_serror_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_rerror_rate': np.random.uniform(0, 1, size=n_samples),
    'dst_host_srv_rerror_rate': np.random.uniform(0, 1, size=n_samples)
}

# Créer un DataFrame
df = pd.DataFrame(data, columns=columns)

# Sauvegarder le fichier CSV
df.to_csv("test_data.csv", index=False)

print("Le fichier test_data.csv a été généré avec succès.")
