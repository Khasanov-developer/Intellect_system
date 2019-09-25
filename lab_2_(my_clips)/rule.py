import re

class Rule:
    def __init__(self, ruleName, ruleBody):
        self.ruleName = ruleName
        self.__rulePriority = self.__get_priority(ruleBody)
        self.__ruleCondition = self.__get_condition(ruleBody)
        self.__ruleQuestion = self.__get_question(ruleBody)
        self.__ruleResult = self.__get_result(ruleBody).strip()

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
            return int(ruleBody['priority'])
        else:
            return 0

    def __get_condition(self, ruleBody):
        return ruleBody['if']

    def __get_result(self, ruleBody):
        return ruleBody['then']['resultFact']

    def __get_question(self, ruleBody):
        if 'question' in ruleBody['then']:
            return ruleBody['then']['question']
        else:
            return None

    def __get_polish_notation(self, test_str):

        factsList = re.findall(r'<.*?<', test_str)

        output_str = test_str
        for index, fact in enumerate(factsList):
            output_str = re.sub(fact, str(index), output_str)

        output_str = re.sub(r'or', '+', output_str)
        output_str = re.sub(r'and', '*', output_str)
        output_str = re.sub(r'not', '-', output_str)

        rez = ''
        for char in output_str:
            if char != ' ':
                rez += char
        output_str = rez

        openBrkList = []
        closeBrkList = []

        output = ''
        bufStack = 'z'

        index = 0
        while index < len(output_str):
            # print('char: ', output_str[index])
            # print('output: ', output)
            # print('stack: ', bufStack)
            # print()

            if (output_str[index] == '('):
                bufStack += output_str[index]
                index += 1
                continue

            if (output_str[index] == '-'):
                bufStack += output_str[index]
                index += 1
                continue

            if (output_str[index] < '0' or output_str[index] > '9') and len(output) > 0:
                output += ','
            else:
                output += output_str[index]
                index += 1
                continue

            if (output_str[index] == '*'):
                if (bufStack[-1] == '*' or bufStack[-1] == '-'):
                    output += bufStack[-1]
                    bufStack = bufStack[0:len(bufStack) - 1]
                else:
                    bufStack += output_str[index]
                    index += 1
                continue

            if (output_str[index] == '+'):
                if (bufStack[-1] == '+' or bufStack[-1] == '*' or bufStack[-1] == '-'):
                    output += bufStack[-1]
                    bufStack = bufStack[0:len(bufStack) - 1]
                else:
                    bufStack += output_str[index]
                    index += 1
                continue

            if (output_str[index] == ')'):
                if bufStack[-1] == '(':
                    index += 1
                else:
                    output += bufStack[-1]
                bufStack = bufStack[0:len(bufStack) - 1]
                continue

        for i in range(len(bufStack) - 1, 0, -1):
            if bufStack[i] == '+' or bufStack[i] == '*' or bufStack[i] == '-':
                output += ',' + bufStack[i]

        output = output.split(',')

        while ("" in output):
            output.remove("")

        for index in range(len(output)):
            if output[index] == '+':
                output[index] = 'or'
                continue
            elif output[index] == '*':
                output[index] = 'and'
                continue
            elif output[index] == '-':
                output[index] = 'not'
                continue
            else:
                # print(factsList[int(output[index])])
                output[index] = factsList[int(output[index])]
        #print(output)
        output = [i.strip('<') for i in output]
        return output


    def process_rule(self, inMemoryFacts):
        pnList = self.__get_polish_notation(self.__ruleCondition)
        if self.__eval_pn(pnList, inMemoryFacts):
            #print(self.__ruleResult)
            return self.__ruleResult

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
                elif pnList[i - 2] in facts and pnList[i - 1] in facts:
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
                elif pnList[i - 1] in facts or pnList[i - 2] in facts:
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
        print(pnList[0])
        return pnList[0]