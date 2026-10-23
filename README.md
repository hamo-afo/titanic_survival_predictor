# Titanic Survival Predictor

This project uses a Support Vector Classifier (SVC) to predict whether a
passenger would survive the Titanic disaster. It includes the notebook used
for the analysis, the encoded training and testing data, model predictions,
and a Streamlit web application for interactive predictions.

## Project contents

- `Titanic_Passenger_Survival_Recommended.ipynb` - data preparation,
  model-training, evaluation, and prediction workflow.
- `training-data-encoded.csv` and `testing-data-encoded.csv` - encoded
  datasets used by the model.
- `model-predictions.csv` - predictions generated for the test data.
- `sample-data.csv` and related encoded/output files - sample input and
  prediction data.
- `svc_trained_model.pkl` - trained SVC model used by the notebook.
- `streamlit-app/` - deployable Streamlit application and its model copy.

## Features

The app accepts the following passenger details:

- Passenger class: First, Second, or Third
- Gender: Male or Female
- Siblings/spouses aboard: Zero, One, Two, or Three
- Port of embarkation: Southampton, Cherbourg, or Queenstown

The model was trained on a simplified 100-row teaching dataset. The app
reports approximately 80% accuracy on the held-out test data, so its
predictions are intended for educational demonstration rather than historical
analysis.

## Run the Streamlit app locally

From the project root:

```powershell
cd streamlit-app
python -m pip install -r requirements.txt
streamlit run app.py
```

The application will open at the local Streamlit URL shown in the terminal.

The project is currently aligned with the installed scikit-learn version used for model persistence. If the model file needs to be refreshed, run:

```powershell
cd streamlit-app
python retrain_model.py
```

The included `runtime.txt` specifies Python 3.14 for hosted deployments, and the model is regenerated against the current scikit-learn runtime to avoid pickle-version mismatches.

## Run the notebook

Install the packages listed in `streamlit-app/requirements.txt`, then open
`Titanic_Passenger_Survival_Recommended.ipynb` in Jupyter Notebook, JupyterLab,
or VS Code and run the cells from top to bottom.

## License

This project is provided for educational use.
