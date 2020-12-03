import random
import sys
sys.setrecursionlimit(10**6) 

p=int(input("Enter first prime no:"))
q=int(input("Enter second prime no:"))
n=p*q
euler_totient=(p-1)*(q-1)
print(n)
print(euler_totient)
def find_gcd(a, b): 
    if (a==0 or b==0): 
        return 0   
    if (a==b): 
        return a 
    if (a>b):  
        return find_gcd(a-b,b) 
    return find_gcd(a,b-a) 

def coprime(a, b):
    if ( find_gcd(a, b) == 1): 
        return True
    else:
        return False
list_of_coprime=[]
for i in range(2,n-1):
    
    if coprime(i,euler_totient)==True:
        list_of_coprime.append(i)
print(list_of_coprime)

e=random.choice(list_of_coprime)
print(e)
for i in range(1,n): 
    x=1+i*euler_totient 
    if x%e==0: 
        d=int(x/e) 
        break

print(d)
public_key=[e,n]
private_key=[d,n]
print("Private Key:",private_key)
print("Public Key:",public_key)

list_char=[]
plain=input("Enter the plain text:")
for i in range(0,len(plain)):
    list_char.append(ord(plain[i]))

list_of_cipher_text=[]
list_of_plain_text=[]
def encryption():
    global list_of_cipher_text
    for i in list_char:
        cipher=(i**e)%n
        list_of_cipher_text.append(cipher)
    return list_of_cipher_text

def decryption():
    global list_of_plain_text
    for i in list_of_cipher_text:
        plain=(i**d)%n
        list_of_plain_text.append(chr(plain))

def listToString(s):  
    str1 = "" 
    for ele in s:  
        str1 += ele      
    return str1 


while True:
    choice=int(input("Select your choice:\n1. Encryption\n2. Decryption\n3. Exit\nEnter your choice:"))
    if choice==1:
        cipher_t=encryption()
        print("Cipher no generated:",cipher_t)
    elif choice==2:
        decryption()
        plain_t=listToString(list_of_plain_text)
        print("Plain text decrypted:",plain_t)
    elif choice==3:
        exit()
