import yaml

def read_yaml(filename = 'rules.yml'):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


if __name__ == '__main__':
    print(read_yaml())
