def vigenere(p,mot_cle):
    message_code = ""
    for i,c in enumerate(p):
        d = mot_cle[i]
        d = ord(d)-65
        e=ord(c)-65
        if(i%2!=0):
            message_code += chr(65+((e+d)%26))
        else:
            if(e-d>=0):
                message_code += chr(65+(e-d))
            else:
                message_code += chr(65+(e-d+26))

    return message_code

n=input()
t=input()
print(vigenere(n,t))