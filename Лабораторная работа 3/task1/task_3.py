src = not False and True or False and not True

# result = True and True or False and False
# ибавились от not
# result = True or False
# убрали and - (False and False = False)
# result = True

result = True

print(src == result)
