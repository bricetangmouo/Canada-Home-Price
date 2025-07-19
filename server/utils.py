import json
import pickle
__all_columns_unclassified = None

def load_all_function():
    with open("./columns_without_classification.json") as f:
        __all_columns_unclassified = json.load(f)

def get_all_columns_data() -> json:
    all_data_columns = None
    with open('./columns.json', 'r') as f:
        all_data_columns = json.load(f)
    return all_data_columns

def get_estimation_price(allData:dict):
    model = None
    with open('./price_prediction_model.pickle', 'rb') as f:
        model = pickle.load(f)
    

if __name__ == '__main__':
    print(get_all_columns_data())