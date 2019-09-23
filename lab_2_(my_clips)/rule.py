

class Rule:
    def __init__(self, ruleName, ruleBody):
        self.ruleName = ruleName
        self.ruleCondition = self.__get_condition(ruleBody)
        self.ruleQuestion = self.__get_question(ruleBody)
        self.ruleResult = self.__get_result(ruleBody)

    def __get_condition(self, ruleBody):
        return ruleBody['if']

    def __get_result(self, ruleBody):
        return ruleBody['then']['resultFact']

    def __get_question(self, ruleBody):
        return ruleBody['then']['question']