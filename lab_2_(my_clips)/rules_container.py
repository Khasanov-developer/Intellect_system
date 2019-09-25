from reader import YamlReader, XmlReader, JsonReader

class RulesContainer:
    def __init__(self, path):
        self.rules = self.__load(path)
        self.rules.sort(key = lambda rule: rule.get_rule_priority(), reverse = True)

    def __create_reader(self, path):
        if 'yml' or 'yaml' in path:
            return YamlReader()
        elif 'xml' in path:
            return XmlReader()
        elif 'json' in path:
            return JsonReader()


    def __load(self, path):
        reader = self.__create_reader(path)
        return reader.load(path)



