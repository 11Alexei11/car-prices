import pickle as pkl
import os
import uuid
import json


def save_bin(model, path_to_save) -> None:
    if path_to_save and os.path.exists(path_to_save):
        with open(path_to_save, 'wb') as f:
            pkl.dump(model, f)

class Experiment:
    def __init__(self, experiment_name, experimen_dir):
        self._experiment_name = experiment_name + '-' + str(uuid.uuid4())[:4]
        self._experiment_dir = experimen_dir

        self.__reset_experiment()

    def __reset_experiment(self):
        self.path_to_specific_experiment = os.path.join(self._experiment_dir, self._experiment_name)

        os.makedirs(self.path_to_specific_experiment, exist_ok=True)
        os.makedirs(os.path.join(self.path_to_specific_experiment, 'visualize'), exist_ok=True)
        os.makedirs(os.path.join(self.path_to_specific_experiment, 'metrics'), exist_ok=True)
        os.makedirs(os.path.join(self.path_to_specific_experiment, 'params'), exist_ok=True)
        os.makedirs(os.path.join(self.path_to_specific_experiment, 'models'), exist_ok=True)

        print(f'experiment with name: {self._experiment_name} was created')
    
    def log_metrics(self, metrics_dict: dict):
        with open(os.path.join(self.path_to_specific_experiment, 'metrics/metrics.json'), 'w')as f:
            json.dump(metrics_dict, f)
        print('metrics were saved')
    
    def log_params(self, params: dict):
        pass