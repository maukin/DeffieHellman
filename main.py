import random

g = random.randint(0, 1000)
n = random.randint(0, 1000)

print("Public: \tg =", g)
print("Public: \tn =", n)

Alice_num = random.randint(0, 1000)
Bob_num = random.randint(0, 1000)

print("Private: \tAlice number =", Alice_num)
print("Private: \tBob number =", Bob_num)

Alice_key1 = (g ** Alice_num) % n
Bob_key1 = (g ** Bob_num) % n

print("Private: \tAlice key1 =", Alice_key1)
print("Private: \tBob key1 =", Bob_key1)

Alice_key_final = (g ** (Alice_key1 * Bob_key1)) % n
Bob_key_final = (g ** (Alice_key1 * Bob_key1)) % n

print("Public: \tAlice key final =", Alice_key_final)
print("Public: \tBob key final =", Bob_key_final)

if Alice_key_final == Bob_key_final:
    print("\t\tSuccess!")
else:
    print("Fail!")






