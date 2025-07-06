email=input("Email your Email : ")#g@g.in , 1scube@gmail.com
k,j,d=0,0,0
if len(email)>=6: #1
    if email[0].isalpha(): #2
        if("@" in email) and (email.count("@")==1): #3
            if(email[-4]==".") ^ (email[-3]=="."): #4
                for i in email:
                    if i == i.ispace(): #5
                        k = 1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue 
                    else:
                        d=1

                    if k==1 or j==1 or d==1:
                       print("Wrong Email")
                else:
                    print("Email is valid")
            else:
                print("Wrong Email(Invalid '.' position)")
        else:
            print("Wrong Email(Invalid @)")
    else:
        print("Wrong Email(Must start with alphabet)")
else:
    print("Wrong Email(Too short)")                                     