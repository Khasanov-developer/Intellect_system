
class Rule:
    def __init__(self, ruleName, ruleBody):
        self.ruleName = ruleName
        self.__rulePriority = self.__get_priority(ruleBody)
        self.__ruleCondition = self.__get_condition(ruleBody)
        self.__ruleQuestion = self.__get_question(ruleBody)
        self.__ruleResult = self.__get_result(ruleBody)

    def get_rule_priority(self):
        return self.__rulePriority

    def get_rule_condition(self):
        return self.__ruleCondition

    def get_rule_question(self):
        return self.__ruleQuestion

    def get_rule_result(self):
        return self.__ruleResult

    def __get_priority(self, ruleBody):
        if 'priority' in ruleBody:
            return ruleBody['priority']
        else:
            return 0

    def __get_condition(self, ruleBody):
        return ruleBody['if']

    def __get_result(self, ruleBody):
        return ruleBody['then']['resultFact']

    def __get_question(self, ruleBody):
        if 'question' in ruleBody:
            return ruleBody['then']['question']
        else:
            return None

    def __get_polish_notation(self, ruleCondition):
        pass

    def process_rule(self, inMemoryFacts):
        pnList = self.__get_polish_notation(self.__ruleCondition)
        if self.__eval_pn(pnList, inMemoryFacts):
            pass

    def __eval_pn(self, polishNotationList, inMemoryFacts):
        pnList = polishNotationList.copy()
        facts = inMemoryFacts.copy()
        i = 0
        while i < len(pnList):
            if pnList[i] not in ('and', 'not', 'or'):
                i += 1
                continue
            elif pnList[i] == 'and':
                if (pnList[i - 2] == True or pnList[i - 2] == False) and type(pnList[i - 1]) is str:
                    oper = pnList[i - 2]
                    fact = pnList[i - 1]
                    if oper == True and fact in facts:
                        pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                        i -= 1
                        continue
                    else:
                        pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                        i -= 1
                        continue
                elif (pnList[i - 1] == True or pnList[i - 1] == False) and type(pnList[i - 2]) is str:
                    oper = pnList[i - 1]
                    fact = pnList[i - 2]
                    if oper == True and fact in facts:
                        pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                        i -= 1
                        continue
                    else:
                        pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                        i -= 1
                        continue
                elif pnList[i - 1] == True and pnList[i - 2] == True:
                    pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                    i -= 1
                    continue
                elif pnList[i - 2] and pnList[i - 1] in facts:
                    pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                    i -= 1
                    continue
                else:
                    pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                    i -= 1
                    continue

            elif pnList[i] == 'or':
                if pnList[i - 2] == True or pnList[i - 2] == False:
                    oper = pnList[i - 2]
                    fact = pnList[i - 1]
                    if oper == True or fact in facts:
                        pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                        i -= 1
                        continue
                    else:
                        pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                        i -= 1
                        continue
                elif pnList[i - 1] == True or pnList[i - 1] == False:
                    oper = pnList[i - 1]
                    fact = pnList[i - 2]
                    if oper == True or fact in facts:
                        pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                        i -= 1
                        continue
                    else:
                        pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                        i -= 1
                        continue
                elif pnList[i - 1] or pnList[i - 2] in facts:
                    pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                    i -= 1
                    continue
                elif pnList[i - 1] == True or pnList[i - 2] == True:
                    pnList = pnList[:i - 2] + [True, ] + pnList[i + 1:]
                    i -= 1
                    continue
                else:
                    pnList = pnList[:i - 2] + [False, ] + pnList[i + 1:]
                    i -= 1
                    continue

            elif pnList[i] == 'not':
                if pnList[i - 1] == True:
                    pnList = pnList[:i - 1] + [False, ] + pnList[i + 1:]
                    continue
                elif pnList[i - 1] == False:
                    pnList = pnList[:i - 1] + [True, ] + pnList[i + 1:]
                    continue
                elif pnList[i - 1] not in facts:
                    pnList = pnList[:i - 1] + [True, ] + pnList[i + 1:]
                    continue
                else:
                    pnList = pnList[:i - 1] + [False, ] + pnList[i + 1:]
                    continue
        return pnList[0]