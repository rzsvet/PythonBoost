def mineralFormation(matrix):
    stalactitesLine = sum(matrix[0])
    stalagmitesLine = sum(matrix[len(matrix)-1])
    if(stalactitesLine > 0 and stalagmitesLine > 0):
        return "both"
    elif(stalactitesLine > 0):
      return "stalactites"
    elif(stalagmitesLine > 0):
      return "stalagmites"
    else:
      return "none"


result = mineralFormation([
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]) # "stalactites"
print(result)
result = mineralFormation([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]) # "stalagmites"
print(result)
result = mineralFormation([
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]) # "both"
print(result)