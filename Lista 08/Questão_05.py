def inverte_string(string):
    if (string == ""):
        return ""
    else:
        return inverte_string(string[1:])+string[0]
    
print(inverte_string("amor"))