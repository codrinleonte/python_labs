def validate_dict(rules, dictionary):
    keysList = []
    rulesDict = {}
    middle = ""
    prefix = ""
    suffix = ""
    for rule in rules:
        keysList.append(rule[0])
        rulesDict.setdefault(rule[0], rule)
    for key in dictionary:
        if key not in keysList:
            return False
        prefix = dictionary[key][:len(rulesDict[key][1])]
        suffix = dictionary[key][-len(rulesDict[key][3]):]

        if len(rulesDict[key][3]) == 0:
            middle = dictionary[key][len(rulesDict[key][1]):]
        else:
            middle = dictionary[key][len(rulesDict[key][1]):-len(rulesDict[key][3])]

        if  prefix != rulesDict[key][1]:
            return False
        if len(rulesDict[key][3]) > 0 and suffix != rulesDict[key][3]:
            return False
        if rulesDict[key][2] not in middle:
            return False

    return True


print(validate_dict(
    [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
    {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside","key3": "this is not valid"}))
