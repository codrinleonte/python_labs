def build_xml_element(tag, content, **dict):
    result = ' < ' + tag
    for e in dict:
        result = result +  ' ' + e + ' = "' + dict[e] + '" '
    result += '/>'
    result += content
    result += '</' + tag + '>'
    return result


print(build_xml_element("a", "Hello there", id="ana"))

