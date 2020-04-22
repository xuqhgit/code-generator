


def property_to_field(prop):
    if prop.find("_")==-1:
        return prop.isupper() and prop.lower() or prop
    field = ''
    length = len(prop)
    prop = prop.lower()
    flag = False
    for i in range(0, length):
        if prop[i] == '_' and i < length:
            flag = True
        else:
            if flag:
                flag = False
                field = field + prop[i].upper()
            else:
                field = field + prop[i]
    return field


def field_to_property(field):
    prop = ''
    length = len(field)
    for i in range(0, length):
        if field[i].isupper():
            prop = prop + "_" + field[i]
    return prop.upper()


