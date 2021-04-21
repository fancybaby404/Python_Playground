name1 = "JULIAN MACATO"
name2 = "NICOLE DIVERS"

name1_lower = name1.lower()
name2_lower = name2.lower()

name1_score = name1.count("T") + name1.count("R") + name1.count("U") + name1.count("E")

name2_score = name2.count("L") + name2.count("O") + name2.count("V") + name2.count("E")

final_score = name1_score + name2_score

print (f"name 1 score = {name1_score})
print (f"name 2 score = {name2_score})
print(final_score)
