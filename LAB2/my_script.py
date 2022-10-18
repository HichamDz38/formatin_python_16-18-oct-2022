import matplotlib.pyplot as plt
#############################################################
##                 Choisir 5 coutry                        ##
#############################################################

countries = ["Algeria","Canada","China","Italy","Palestine"]


###############################################################
##    Afficher le nombres des cas total par coutry          ###
###############################################################
total_case = {}

for country in countries:
    total_case[country] = []

F = open("owid-covid-data.csv")
data = F.readlines()
data = data[1:]
F.close()

for l in data:
    L = l.split(",")
    try:
        c =  L[2]
        if L[4]:
            total = int(float(L[4]))
            if c in countries:
                total_case[c] = total
        else:
            total = 0
    except Exception as e:
        print(e)
        print(L[2], L[4])
        break
    
print(total_case)

############################################################################
## Pour chaque payer afficher le nombre de nouveau cas dans chaque mois  ###
############################################################################


monthly_cases = {}

for country in countries:
    monthly_cases[country] = {}

for l in data:
    L = l.split(",")
    c =  L[2]
    if L[5]:
        total = int(float(L[5]))
    else:
        total = 0
    date_ = L[3][:-3]

    if c in countries:
        if date_ in monthly_cases[c].keys():
            monthly_cases[c][date_] += total
        else:
            monthly_cases[c][date_] = total
print(monthly_cases)


############################################################################
## Pour chaque payer afficher le nombre de nouveau cas dans chaque jour  ###
############################################################################


daily_cases = {}

for country in countries:
    daily_cases[country] = {}

for l in data:
    L = l.split(",")
    c =  L[2]
    if L[5]:
        total = int(float(L[5]))
    else:
        total = 0
    date_ = L[3]

    if c in countries:
        if date_ in daily_cases[c].keys():
            daily_cases[c][date_] += total
        else:
            daily_cases[c][date_] = total

values = daily_cases["Algeria"]

X = values.keys()
Y = values.values()
plt.plot(X, Y)
plt.show()