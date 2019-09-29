from rules_container import RulesContainer
import re

def ask_question(rule):
    print(rule.get_rule_question())
    answer = input('Input your answer: ').lower().strip()
    answerList = re.findall(r'\((.*)/(.*)\)', rule.get_rule_question())
    if answer not in answerList[0]:
        return None
    else:
        return " " + answer

def show_rule(rule):
    print()
    print('RuleName:',rule.ruleName)
    print('RulePriority:',rule.get_rule_priority())
    print('RuleCondition:',rule.get_rule_condition())
    print('RuleQuestion:',rule.get_rule_question())
    print('RuleResult:',rule.get_rule_result())
    print()

if __name__ == '__main__':
    rulePath = 'rules.yml'
    ruleCont = RulesContainer(rulePath)
    rules = ruleCont.rules
    result = ''
    facts = []
    while 'choose' not in result:
        i = 0
        while i < len(rules):
            print('Facts:', facts)
            show_rule(rules[i])
            newFact = rules[i].process_rule(facts)

            if newFact != None:
                if 'choose' in newFact:
                    result = newFact
                    break

            if newFact == None:
                i+=1
                continue

            elif rules[i].get_rule_question() == None and newFact != None and newFact not in facts:
                facts.append(newFact)
                rules.remove(rules[i])
                break

            if rules[i].get_rule_question() != None:
                while True:
                    ans = ask_question(rules[i])
                    if ans == None:
                        print('Enter correct value!')
                    else:
                        newFact += ans
                        break

                if newFact not in facts:
                    facts.append(newFact)
                    rules.remove(rules[i])
                    break



    print(result)

