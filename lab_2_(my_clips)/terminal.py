from rules_container import RulesContainer

if __name__ == '__main__':
    rulePath = 'rules.yml'
    rulesContainer = RulesContainer(rulePath)
    for rule in rulesContainer.rules:
        print(rule.ruleCondition)

