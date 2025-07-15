import json

def get_city():
    all_city = None
    with open("./columns.json", 'r') as f:
        all_city = json.load(f)['city']
    return all_city

def get_province():
    all_province = None
    with open('./columns.json', 'r') as f:
        all_province = json.load(f)['province']
    return all_province

def get_type_home():
    all_home_type = None
    with open('./columns.json', 'r') as f:
        all_home_type = json.load(f)['type']
    return all_home_type

def get_smoking_type():
    all_smoking_type = None
    with open('./columns.json', 'r') as f:
        all_smoking_type = json.load(f)['is_smoking']
    return all_smoking_type

if __name__ == '__main__':
    print(get_smoking_type())