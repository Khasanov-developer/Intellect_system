from rules_container import RulesContainer

def ask_question(rule):
    print(rule.get_rule_question())
    answer = input('Input your answer: ').lower().strip()
    return " " + answer

def show_rule(rule):
    print()
    print(rule.ruleName)
    print(rule.get_rule_priority())
    print(rule.get_rule_condition())
    print(rule.get_rule_question())
    print(rule.get_rule_result())
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
                newFact += ask_question(rules[i])

                if newFact not in facts:
                    facts.append(newFact)
                    rules.remove(rules[i])
                    break



    print(result)

