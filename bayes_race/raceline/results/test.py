from numpy import load

data = load(r'F:\PyCharm Projects\bayesrace\bayes_race\tracks\src\MAP2_raceline.npz')
lst = data.files
print(lst)
# print(len(lst))
for count,item in enumerate(lst):
    print("*****************",item,"*******************************************************************************")
    # print(len(item))
    print(data[item])
    # print(len(data[item][0]))