ifade = input("Ifadeyi girin: ")
dizi = (ifade.replace(" ",""))
#print(dizi)
stack = []


def operand(a):
    return a.isdigit()

def operator(a):
    return (a=="+" or a=="-" or a=="*" or a=="/")

def isValidExpression(dizi):
    l = len(dizi)
    print(l)
    acikparantez=0
    kapaliparantez=0
    
    for a in range(l):
        #print(dizi[a])
        if(operand(dizi[a])):
            #print("ture")    
            stack.append(dizi[a])
        elif(operator(dizi[a]) and (operand(dizi[a+1]) or dizi[a+1]=="(" ) ):
            stack.append(dizi[a])
            #print("evet")
        elif(dizi[a]=="("): 
            if(operand(dizi[a+1]) or dizi[a+1]=="(" ):
                acikparantez += 1
            else:
                return False        
        elif(dizi[a]==")" or (operand(dizi[a-1]) or dizi[a+1] != "(")):
            kapaliparantez += 1
        else:
            return False
        

    if((acikparantez!=kapaliparantez) or (dizi[a]=='/' and dizi[a+1]=='0') or (operator(dizi[0]) or operator(dizi[l-1]))):
        return False
        
    print(acikparantez)
    print(kapaliparantez)
    return True


if(isValidExpression(dizi)):
    print("Girilen ifade matematiksel ifadedir")
else:
    print("Girilen ifade matematiksel ifade degildir")

print(stack)

