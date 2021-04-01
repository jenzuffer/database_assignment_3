import json
from pprint import pprint

def main():
    file_json = open("abstract_syntax_tree.json", )
    data = json.load(file_json)
    pprint(data)

if __name__ == "__main__":
    main()
