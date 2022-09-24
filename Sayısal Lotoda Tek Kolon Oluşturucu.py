import random
sayisal_loto = set()

while len(sayisal_loto) < 8:
    sayisal_loto.add(random.randint(1, 49))

print(f"Bu haftaki şanslı numaralarınız : {sayisal_loto}")
