from sklearn.neural_network import MLPRegressor
from logger import get_logger

logger = get_logger(__name__)

def train_model(X_train, y_train):
    try:
        model = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=500, random_state=42)
        model.fit(X_train, y_train)
        logger.info("Model trained successfully.")
        return model
    except Exception as e:
        logger.error("Error in model training", exc_info=True)
        raise e
