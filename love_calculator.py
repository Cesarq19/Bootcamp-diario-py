# love calculator
name1 = input("Ingrese el primer nombre: ")
name2 = input("Ingrese el segundo nombre: ")

nombres_juntos = name1+name2
num_true = 0
num_lov = 0
for a in "true":
    num_true += nombres_juntos.lower().count(a)
for b in "love":
    num_lov += nombres_juntos.lower().count(b)
score = num_lov + num_true*10
if 10 <= score and score >= 90:
    print("Your score is ",str(score),", you go together like coke and mentos.")
elif 40 <= score <= 50:
    print("Your score is ",str(score),", you are alright together.")
else:
    print("Your score is ",str(score))