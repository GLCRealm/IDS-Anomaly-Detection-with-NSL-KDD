import pandas as pd
import joblib
import os


def load_model():
    model_path = 'ebest_model.pkl'
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("Model loaded successfully!")
        return model
    else:
        print(f"Error: Model file not found at {model_path}")
        exit()


def preprocess_data(raw_data):
    # Define feature columns based on the training file structure

    columns = ['duration',
               'protocol_type',
               'service',
               'flag',
               'src_bytes',
               'dst_bytes',
               'land',
               'wrong_fragment',
               'urgent',
               'hot',
               'num_failed_logins',
               'logged_in',
               'num_compromised',
               'root_shell',
               'su_attempted',
               'num_root',
               'num_file_creations',
               'num_shells',
               'num_access_files',
               'num_outbound_cmds',
               'is_host_login',
               'is_guest_login',
               'count',
               'srv_count',
               'serror_rate',
               'srv_serror_rate',
               'rerror_rate',
               'srv_rerror_rate',
               'same_srv_rate',
               'diff_srv_rate',
               'srv_diff_host_rate',
               'dst_host_count',
               'dst_host_srv_count',
               'dst_host_same_srv_rate',
               'dst_host_diff_srv_rate',
               'dst_host_same_src_port_rate',
               'dst_host_srv_diff_host_rate',
               'dst_host_serror_rate',
               'dst_host_srv_serror_rate',
               'dst_host_rerror_rate',
               'dst_host_srv_rerror_rate',
               'class',
               'target']

    features = pd.DataFrame(raw_data, columns=columns )
    col = [
        'src_bytes',
        'dst_bytes',
        'count',
        'srv_count',
        'num_failed_logins',
        'num_compromised',
        'serror_rate',
        'rerror_rate',
        'num_file_creations',
        'num_shells', ]

    # Calculate protocol_attack_probability using training data distribution
    columns = pd.read_csv("dataset/kddcup.names", names=['names'])
    data_train = pd.read_csv("dataset/KDDTrain+.txt", names=columns["names"])
    labels = data_train['class'].apply(lambda x: 0 if x == 'normal' else 1)
    data_train['label'] = labels
    attack_counts = data_train[data_train['label'] == 1].groupby('protocol_type').size()
    total_counts = data_train.groupby('protocol_type').size()
    probability_of_attack = (attack_counts / total_counts).fillna(0)

    # Map protocol probabilities to the raw data
    features['protocol_attack_probability'] = features['protocol_type'].map(probability_of_attack)

    # Retain only required features
    processed_features = features[col]
    return processed_features


def test_model(model, test_data):
    predictions = model.predict(test_data)
    print("\nPredictions:")
    for i, pred in enumerate(predictions):
        print(f"Sample {i + 1}: Predicted {'Anomaly' if pred == 1 else 'Normal'}")


if __name__ == "__main__":
    raw_data = [
        [0, 'ftp', 'private', 'SF', 28, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0.00, 0.00, 0.00, 0.00,
         1.00, 0.00, 0.00, 22, 2, 0.09, 0.14, 0.09, 0.00, 0.00, 0.00, 0.00, 0.00, 'nwarezmaster', 12],
        [0, 'tcp', 'http', 'SF', 215, 295, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 0.00, 0.00, 0.00,
         0.00, 1.00, 0.00, 0.00, 45, 245, 1.00, 0.00, 0.02, 0.06, 0.00, 0.00, 0.00, 0.00, 'normal', 21],
        [0, 'tcp', 'pop_3', 'S0', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1.00, 1.00, 0.00, 0.00,
         1.00, 0.00, 1.00, 15, 52, 0.33, 0.20, 0.07, 0.04, 1.00, 0.10, 0.00, 0.88, 'mscan', 13],
        [0, 'udp', 'private', 'SF', 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0.00, 0.00, 0.00, 0.00,
         1.00, 0.00, 0.00, 255, 255, 1.00, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 'snmpguess', 17],
        [0, 'tcp', 'finger', 'RSTO', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 11, 0.00, 0.00, 1.00,
         1.00, 0.29, 0.11, 0.00, 255, 58, 0.23, 0.11, 0.01, 0.00, 0.00, 0.00, 0.99, 1.00, 'neptune', 18],
        [0, 'tcp', 'http', 'SF', 342, 2477, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 29, 0.00, 0.00, 0.00,
         0.03, 1.00, 0.00, 0.24, 255, 255, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 'normal', 21]
    ]

    # Load model
    model = load_model()

    # Preprocess data
    preprocessed_data = preprocess_data(raw_data)

    # Test model
    test_model(model, preprocessed_data)