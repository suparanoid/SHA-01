import numpy as np
import tkinter as tk
from tkinter import simpledialog
from decimal import *

def mdp():
    momdp = simpledialog.askstring("password", "enter the password. no accentuated letters:", show="*")
   
    if momdp:
        
            binn = ""
            ww= len(str(momdp))
            strnb= (''.join(format(ord(char), '08b') for char in momdp)).zfill(448)
            binn += bin(ww)[2:].zfill(64)
            
            www=[]
            www =strnb+binn
            text = www
            chunk_size = 32
            parts = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
                  
            def rightrotate(arr, k):
                if not arr:
                    return arr  
                k = k % len(arr)  
                return arr[-k:] + arr[:-k]  
            
            
            fract=parts
            def rotate():
                for i in range(0,15):
                    my_list = parts[i]
                    rotated_list = rightrotate(my_list, i+1)
                    fract.append(rotated_list)
            rotate()
            
            
            def rotatwo():
                for i in range(0,15):
                    my_listt = parts[i]
                    rotatad_list = rightrotate(my_listt, 3)
                    fract.append(rotatad_list)
            rotatwo()
            
            
            def rotathree():
                for i in range(0,15):
                    my_lisstt = parts[i]
                    ratatad_list = rightrotate(my_lisstt, 1)
                    fract.append(ratatad_list)
            rotathree()
            
            
            def rotafour():
                for i in range(12,15):
                    my_llisstt = parts[i]
                    megaratatad_list = rightrotate(my_llisstt, -2)
                    fract.append(megaratatad_list)
            rotafour()
            
            
            
            
            
            
            
            
            prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
                    173, 179, 181, 191, 193, 197, 199, 211, 223]
            
            
            def squaree(i):
                return i**0.5
            result= map(squaree, prime)  
            resultt= (list(result))   
            
            
            modulo=[]
            def get_dec():
                for i in range(1,48):
                    decNum = resultt[i]
                    frac = decNum % 1
                    modulo.append(frac) 
            get_dec()
            
            
            def poww(n):
                return n*(2**31)
            pow = map(poww,modulo)
            powpow = (list(pow))
            
            
            def get_out(u):
                return int(u)
            intt= map(get_out, powpow)
            inttt = (list(intt))
            
            
            def bina(y):  
                return bin(y)[2:]
            binna=map(bina, inttt)
            binar = (list(binna))
            
            
            fractwo = []
            def new():
                
                for i in range (1,16):
                    r=fract[i]
                    fractwo.append(r)
            new()
            
            
            primefract = []
            def newp():
                for i in range (1,16):
                    r=binar[i]
                    primefract.append(r)       
            newp()
            

            texxt = str(fractwo).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace(" ", "")
            chunk_sizee = 1
            partss = [texxt[i:i+chunk_sizee] for i in range(0, len(texxt), chunk_sizee)]
            
            teexxt = str(primefract).replace("'", "").replace("[", "").replace("]", "").replace(",","").replace(" ", "")
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
            #print("chunks:",(parts))  
            #print("binary code:",(www))
            print ("password:",(momdp))
            # print ('fract:', (fract))
            #print ('binary:', (binar))
            print ('resuult:', (end))
            #print ("frac", (hexaend))
            #print ("primefrac", (partsss))
            #print ("parts",(texxt))
            '''number_of_elements = len(fract)
            print("Number of elements in the list:", number_of_elements)'''
            
    
        
    else:
        print("Thus, you didn't pass.")


panel= tk.Tk()
panel.title("YOU SHALL NOT PASS")
bouton = tk.Button(panel, text="password", command=mdp)
bouton.pack(padx=20, pady=20)
panel.mainloop()

