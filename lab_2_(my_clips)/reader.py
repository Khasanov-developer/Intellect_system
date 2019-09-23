from abc import ABC, abstractmethod
import yaml
from rule import Rule

class Reader(ABC):
    @abstractmethod
    def load(self, path):
        pass

    @abstractmethod
    def transform_to_rule_object(self, dictObject):
        pass


class YamlReader(Reader):
    def load(self, path):
        with open(path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            rules = self.__transform_to_rule_object(data)
        return rules

    def __transform_to_rule_object(self, dictObject):
        ruleList = []
        for ruleName in dictObject:
            ruleList.append(Rule(ruleName, dictObject[ruleName]))
        return ruleList


class XmlReader(Reader):
    def load(self, path):
        pass

    def __transform_to_rule_object(self, dictObject):
        ruleList = []
        for ruleName in dictObject:
            ruleList.append(Rule(ruleName, dictObject[ruleName]))
        return ruleList

class JsonReader(Reader):
    def load(self, path):
        pass

    def __transform_to_rule_object(self, dictObject):
        ruleList = []
        for ruleName in dictObject:
            ruleList.append(Rule(ruleName, dictObject[ruleName]))
        return ruleList