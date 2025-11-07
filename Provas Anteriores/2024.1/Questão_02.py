def somatorio(num = 20):
    if num == 0:
        return 0
    else:
        return num+somatorio(num-2)
print(somatorio())