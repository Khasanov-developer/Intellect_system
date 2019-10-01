from rules_container import RulesContainer
import re

def get_facts(choice, rules):
    return reverse_logic_output(choice, rules)

def get_list_from_str(str):
    factsList = re.findall(r'<.*?<', str)
    factsList = [i.strip('<') for i in factsList]
    return factsList

def reverse_logic_output(choice, rules):
    facts = []
    for rule in rules:
        if rule.get_rule_result() in choice:
            facts = get_list_from_str(rule.get_rule_condition())
            break
    return facts

def recurse_choice(choice, outputLst, rules):
    if '_' in choice:
        return choice
    else:
        lst = get_facts(choice, rules)
        outputLst.extend(lst)
        for fact in lst:
            outputLst.append(recurse_choice(fact, outputLst, rules))


if __name__ == '__main__':
    path = 'rules.yml'
    rules = RulesContainer(path).rules
    output = []
    choice = input('Input rule result: ')
    recurse_choice(choice, output, rules)
    for rem in range(output.count(None)):
        output.remove(None)

    i = 0
    while i < len(output):
        if '_' in output[i]:
            output.pop(i)
        else:
            i += 1

    output = set(output)

    print('Факты:')
    for fact in output:
        print(fact)
