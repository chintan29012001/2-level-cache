import math

def integer_to_binary(x,off):
    y=x
    ans=""
    while(y>0):
        ans+=str(y%2)
        y=y//2
    ans=ans[::-1]
    while(len(ans)<off):
        ans="0"+ans
    return ans

def decimal_to_binary(x,off):
    ans=""
    for i in range(0,off):
        x=x*2
        if(x>=1):
            ans+="1"
            x-=1
        else:
            ans+="0"
    return ans

def binary_to_integer(x):
    x=x[::-1]
    sum=0
    for i in range(0,len(x)):
        sum+=int(x[i])*math.pow(2,i)
    return sum

def binary_to_decimal(x):
    sum=0
    for i in range(1,len(x)+1):
        sum+=int(x[i-1])*math.pow(2,-i)
    return sum     

def binary_to_float(x):
    if(int(x)!=0):
        exponent=binary_to_integer(x[1:12])-1023
        mantissa=x[12:]
        number=binary_to_integer("1"+mantissa[:int(exponent)])
        decimal=binary_to_decimal(mantissa[int(exponent):])
        ans=number+decimal
        if(x[0]=="1"):
            ans= -1*ans
        return ans
    else:
        return 0

def floating_to_binary(x):
    if(x!=0):
        ans=""
        sign="0"
        if(x<0):
            sign="1"
        x=abs(x)
        integer_part=integer_to_binary(int(x),1)
        mantissa=decimal_to_binary(x-int(x),53-len(integer_part))
        normalised_mantissa=""
        if(len(integer_part)>1):
            normalised_mantissa=integer_part[1:]+mantissa
        else:
            normalised_mantissa=mantissa
        exponent=len(integer_part)-1+1023
        exponent=integer_to_binary(exponent,11)
        ans=sign+exponent+normalised_mantissa
        return ans
    else:
        return "0"*64
    

    
def initialize_main_memory(main_memory,no_of_blocks,size_of_block):
    if(main_memory=={}):    
        for i in range(0,int(no_of_blocks)):
            b={}
            for j in range(0,int(size_of_block)):
                w="0"*64
                b[integer_to_binary(j,math.log2(size_of_block))]=w
            main_memory[integer_to_binary(i,math.log2(no_of_blocks))]=b


    
def print_main_memory(main_memory):
    print("main memory")
    for i in main_memory:
        for j in main_memory[i]:
            print(i+" "+j,end=" ")
            print(main_memory[i][j])
        print()

def search_in_main_memory(main_memory,no_of_blocks):
    address=input()
    x=main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]
    print(x)
    print(binary_to_float(x))


    
