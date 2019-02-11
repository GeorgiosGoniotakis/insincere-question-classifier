"""Parameters and definitions file"""

# Seed for random number generators used
RANDOM_SEED = 0

# Validation set size
VAL_SET_SIZE = 0.2

# Maximum number of features for TF-IDF vectorizer
TF_MAX_FEATURES = 50000

# Defines the models directory
MODELS_DIR = "models/"

# Defines the names for all the models
SVM_MODEL = MODELS_DIR + "model-svm.pkl"
LOG_MODEL = MODELS_DIR + "model-log.pkl"
MLP_MODEL = MODELS_DIR + "model-mlp.pkl"
