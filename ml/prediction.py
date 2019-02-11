import pickle

from ml.utils.preprocess import *
from ml.utils.vectorizer import build_TF
from ml.utils.definitions import *

from keras.models import load_model

import pandas as pd


def predict(s, model):
    """Loads the selected model and tokenizer into memory and
    performs a prediction for a given string.

    Examples:
        predict("Wine is red", "svm")
        predict("Wine is red", "log")
        predict("Wine is red", "mlp")
        predict("Wine is red", "ada")

    Args:
        s: Input string
        model: Model used to predict (svm, log, mlp, ada)

    Returns:
            0: Sincere
            1: Insincere
            None: Error occurred
    """
    # Placeholder variables
    model_file = None
    library = None

    # Relate model requested with model file
    if model == "svm":
        model_file = SVM_MODEL
    elif model == "log":
        model_file = LOG_MODEL
    elif model == "mlp":
        model_file = MLP_MODEL
    elif model == "ada":
        model_file = ADA_MODEL

    # Make sure model_file is not empty
    assert model_file

    # Scikit-learn model - pickle file
    if model_file.endswith(".pkl"):
        library = "sklearn"
    elif model_file.endswith(".h5"):
        library = "keras"

    # Make sure that file is of appropriate type
    assert library == "sklearn" or library == "keras"

    # Load the model into memory
    if library == "sklearn":
        try:
            with open(model_file, 'rb') as f:
                vectorizer, model = pickle.load(f)
                df = pd.DataFrame.from_dict({"question_text": [s]})
                df_train = build_TF(preprocess_data(df, "question_text"), vectorizer)
                return model.predict(df_train)[0]
        except Exception as ex:
            print("Problem accessing model file. Reason: {}".format(str(ex)))
    elif library == "keras":
        model = load_model(model_file)
