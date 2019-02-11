"""Parameters and definitions file"""

# Seed for random number generators used
RANDOM_SEED = 0

# Validation set size
VAL_SET_SIZE = 0.2

# Maximum number of features for TF-IDF vectorizer
TF_MAX_FEATURES = 50000

# Maximum words in a question (Keras)
MAX_WORDS = 125

# Defines the models directory
MODELS_DIR = "models/"

# Defines the names for all the models
SVM_MODEL = MODELS_DIR + "model-svm.pkl"
LOG_MODEL = MODELS_DIR + "model-log.pkl"
MLP_MODEL = MODELS_DIR + "model-mlp.pkl"
ADA_MODEL = MODELS_DIR + "model-ada.pkl"
LSTM_MODEL = MODELS_DIR + "LSTM.h5"
LSTM_TOKENIZER = MODELS_DIR + "LSTM_tokenizer.pkl"
