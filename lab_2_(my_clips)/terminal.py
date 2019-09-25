from rules_container import RulesContainer

if __name__ == '__main__':
    rulePath = 'rules.yml'
    ruleCont = RulesContainer(rulePath)
    result = ''
    facts = [0,]
    while result == '':
        for rule in ruleCont.rules:
            print(rule.process_rule(facts))
        pass

