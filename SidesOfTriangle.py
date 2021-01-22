def hypotenus(opposite, adjacent):
    a = (opposite**2 + adjacent**2)**0.5
    print ("The Hypotenus of the Triangle is: ",a)

def opposite(hypotenus, adjacent):
    a = (hypotenus**2 - adjacent**2)**0.5
    print ("The Opposite of the Triangle is: ",a)

def adjacent(hypotenus, opposite):
    a = (hypotenus**2 - opposite**2)**0.5
    print ("The Adjacent of the Triangle is: ",a)

side = input ("What side of the Triangle do you want to calculate? hypo, opp or adj: ")
if side == "hypotenus":
    opp = int(input("Enter the opposite: "))
    adj = int(input("Enter the adjacent: "))
    hypotenus(opp, adj)
else:
    if side == "opposite":
        hypo = int(input("Enter the hypotenus: "))
        adj = int(input("Enter the adjacent: "))
        opposite(hypo, adj)
    else:
        if side == "adjacent":
            hypo = int(input("Enter the hypotenus: "))
            opp = int(input("Enter the opposite: "))
            adjacent(hypo, opp)
done = input("Would you like to continue (yes/no): ")
if done == no:
    exit()
else:
    if done == yes:
        side = input ("What side of the Triangle do you want to calculate? hypo, opp or adj: ")
        if side == "hypotenus":
            opp = int(input("Enter the opposite: "))
            adj = int(input("Enter the adjacent: "))
            hypotenus(opp, adj)
    else:
        if side == "opposite":
            hypo = int(input("Enter the hypotenus: "))
            adj = int(input("Enter the adjacent: "))
            opposite(hypo, adj)
        else:
            if side == "adjacent":
                hypo = int(input("Enter the hypotenus: "))
                opp = int(input("Enter the opposite: "))
                adjacent(hypo, opp)
done = input("Would you like to continue (yes/no): ")
