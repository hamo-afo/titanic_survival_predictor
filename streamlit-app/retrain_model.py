from pathlib import Path
import pickle

import pandas as pd
from sklearn.svm import SVC

ROOT = Path(__file__).resolve().parent.parent
TRAINING_DATA = ROOT / "training-data-encoded.csv"
MODEL_OUTPUTS = [
    ROOT / "svc_trained_model.pkl",
    ROOT / "streamlit-app" / "svc_trained_model.pkl",
]


def main() -> None:
    df = pd.read_csv(TRAINING_DATA)
    X = df.drop(columns=["Survived"])
    y = df["Survived"]

    model = SVC(gamma="auto", random_state=0)
    model.fit(X, y)

    for output_path in MODEL_OUTPUTS:
        with output_path.open("wb") as fh:
            pickle.dump(model, fh)
        print(f"Saved updated model to {output_path}")


if __name__ == "__main__":
    main()
