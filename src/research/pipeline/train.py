
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from src.research.pipeline.config import Config
from src.research.pipeline.utils import save_bin, load_bin


def main():
    config = Config()
    model = LinearRegression()

    # load preprocessed dataset
    X_preprocessed_train = load_bin(config.preprocess_x_train_preprocessed_path)
    y_preprocessed_train = load_bin(config.preprocess_y_train_preprocessed_path)

    model.fit(X_preprocessed_train, y_preprocessed_train)

    # save model
    save_bin(artifact=model, path_to_save=config.train_model_path)


if __name__=="__main__":
    main()
