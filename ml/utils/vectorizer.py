def build_TF(dt_train, vectorizer):
    """Builds the TF-IDF matrix."""
    return vectorizer.transform(dt_train['question_text'])
