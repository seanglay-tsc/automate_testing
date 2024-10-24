import json, random

def generate_company_name():
    return random.choice(json.load(open('company_name.json', encoding='utf-8')))