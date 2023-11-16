import numpy as np
import tkinter as tk
from tkinter import simpledialog
from decimal import *

def get_password():
    password = simpledialog.askstring("password", "enter the password. no accentuated letters:", show="*")
   
    if password:
        
            bin_len_password = ""
            len_password= len(str(password))
            bin_password= (''.join(format(ord(char), '08b') for char in password)).zfill(448)
            bin_len_password += bin(len_password)[2:].zfill(64)
            
            bin_password_list=[]
            bin_password_list =bin_password+bin_len_password
            text = bin_password_list
            chunk_size = 32
            words = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
                  
            def rightrotate(arr, k):
                if not arr:
                    return arr  
                k = k % len(arr)  
                return arr[-k:] + arr[:-k]  
            
            
            fract=words
            def rotation_one():
                for i in range(0,15):
                    list_rotation_one = words[i]
                    rotated_list_one = rightrotate(list_rotation_one, i+1)
                    fract.append(rotated_list_one)
            rotation_one()
            
            
            def rotation_two():
                for i in range(0,15):
                    list_rotation_two = words[i]
                    rotated_list_two = rightrotate(list_rotation_two, 3)
                    fract.append(rotated_list_two)
            rotation_two()
            
            
            def rotation_three():
                for i in range(0,15):
                    list_rotation_three = words[i]
                    rotated_list_three = rightrotate(list_rotation_three, 1)
                    fract.append(rotated_list_three)
            rotation_three()
            
            
            def rotation_four():
                for i in range(12,15):
                    list_rotation_four = words[i]
                    rotated_list_four = rightrotate(list_rotation_four, -2)
                    fract.append(rotated_list_four)
            rotation_four()
            
            
            
            
            
            
            
            
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
                    173, 179, 181, 191, 193, 197, 199, 211, 223]
            
            
            def squared(i):
                return i**0.5
            result= map(squared, primes)  
            squareroot_primes= (list(result))   
            
            
            modulo=[]
            def decimals_squareroot_primes():
                for i in range(1,48):
                    decNum = squareroot_primes[i]
                    fract_part_primes = decNum % 1
                    modulo.append(fract_part_primes) 
            decimals_squareroot_primes()
            
            
            def raise_pow(n):
                return n*(2**31)
            apply_raise_pow = map(raise_pow,modulo)
            list_pow = (list(apply_raise_pow))
            
            
            def int_part_primes(u):
                return int(u)
            apply_int_part_primes= map(int_part_primes, list_pow)
            squareroot_primes_int = (list(apply_int_part_primes))
            
            
            def convert_primes_bin(y):  
                return bin(y)[2:]
            apply_convert_primes_bin=map(convert_primes_bin, squareroot_primes_int)
            primes_bin = (list(apply_convert_primes_bin))
            
            
            fract_words = []
            def new_words():
                
                for i in range (1,16):
                    r=fract[i]
                    fract_words.append(r)
            new_words()
            
            
            fract_primes = []
            def new_primes():
                for i in range (1,16):
                    r=primes_bin[i]
                    fract_primes.append(r)       
            new_primes()
            

            texxt = str(fract_words).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace(" ", "")
            chunk_sizee = 1
            partss = [texxt[i:i+chunk_sizee] for i in range(0, len(texxt), chunk_sizee)]
            
            teexxt = str(fract_primes).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace(" ", "")
            partsss = [teexxt[i:i+chunk_sizee] for i in range(0, len(teexxt), chunk_sizee)]
            
            resuult = []
            def inter(n, m):
                
                minlength = min(len(n), len(m))
                for i in range(minlength):
                    resuult.append(n[i])
                    resuult.append(m[i])


                if len(n) > minlength:
                    resuult.extend(n[minlength:])
                elif len(m) > minlength:
                    resuult.extend(m[minlength:])
                return resuult
        


            inter(partss, partsss)
            hexa = str(resuult).replace("'", "").replace(",", "").replace(" ", "").replace("[", "").replace("]", "")
            hexaend= int(hexa, base=10)
            end = hex(hexaend)[2:]          
            
            

            
            
            

            #print(modulo)
            #print("chunks:",(words))  
            #print("binary code:",(bin_password_list))
            print ("password:",(password))
            # print ('fract:', (fract))
            #print ('binary:', (primes_bin))
            print ('resuult:', (end))
            #print ("fract_part_primes", (hexaend))
            #print ("primefrac", (partsss))
            #print ("words",(texxt))
            '''number_of_elements = len(fract)
            print("Number of elements in the list:", number_of_elements)'''
            
    
        
    else:
        print("Thus, you didn't pass.")


panel= tk.Tk()
panel.title("YOU SHALL NOT PASS")
bouton = tk.Button(panel, text="password", command=get_password)
bouton.pack(padx=20, pady=20)
panel.mainloop()

