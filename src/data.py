from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def load_data(n_samples=500, n_features=10, random_state=42):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=6,
        n_redundant=2,
        n_classes=2,
        flip_y=0.01,
        random_state=random_state,
    )
    return train_test_split(X, y, test_size=0.2, random_state=random_state)
