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
    total1 = 0
    total2 = 0

    for update in updates:
        update = [int(a) for a in update.strip().split(",")]
        total1 += check_update(rules, update)

        new_update = fix_update(rules, update.copy())
        if new_update != update:
            total2 += new_update[int(len(new_update)/2)]

    return total1, total2


def check_update(rules, update):
    if len(update) == 1:
        return True
    
    new_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    for rule in new_rules:
        if rule[1] == update[0]:
            return False

    if check_update(new_rules, update[1:]):
        return update[int(len(update)/2)]
    else:
        return 0
    

def fix_update(rules, update):
    if len(update) == 1:
        return update
  
    new_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    while True:
        for rule in new_rules:
            if rule[1] == update[0]:
                for i in range(len(update)):
                    if update[i] == rule[0]:
                        update[i] = rule[1]
                update[0] = rule[0]
                break
        else:
            break

    return [update[0]] + fix_update(new_rules, update[1:])
    
        

if __name__ == "__main__":
    rules, updates = read_data()
    rules = thieves_list(rules)
    print(check_updates(rules, updates))
