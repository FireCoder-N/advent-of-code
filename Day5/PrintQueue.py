def read_data():
    with open('Day5/data.txt') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line == "\n":
            return lines[:i], lines[i+1:]
        
def thieves_list(rules):
    for i, rule in enumerate(rules):
        rules[i] = [int(a) for a in rule.strip().split("|")]
    
    return rules

def check_updates(rules, updates):
    total = 0
    for update in updates:
        update = [int(a) for a in update.strip().split(",")]
        total += check_update(rules, update)

    return total


def check_update(rules, update):
    if len(update) == 1:
        return True
    
    root = update[0]
    new_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    for rule in new_rules:
        if rule[1] == root:
            return False

    if check_update(new_rules, update[1:]):
        return update[int(len(update)/2)]
    else:
        return 0
    

def fix_update(rules, update):
    if len(update) == 1:
        return True
    
    root = update[0]
    new_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    for rule in new_rules:
        if rule[1] == root:
            return False

    if check_update(new_rules, update[1:]):
        return update[int(len(update)/2)]
    else:
        return 0
        

if __name__ == "__main__":
    rules, updates = read_data()
    rules = thieves_list(rules)
    print(check_updates(rules, updates))
