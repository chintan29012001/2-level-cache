import math
from helpercode import *

def initialize_cache_memory(cache_memory,k,no_of_lines,no_of_blocks,size_of_block,pointers):
    if(cache_memory=={}):
        for i in range(0,k):
            pointers[integer_to_binary(i,math.log2(k))]=0
        for i in range(0,int(k)):
            s=[]#block simulation`
            for j in range(0,int(no_of_lines/k)):
                l={}
                for m in range(0,size_of_block):
                    l[integer_to_binary(m,math.log2(size_of_block))]="0"*64
                s.append([integer_to_binary(j,math.log2(no_of_blocks/k)),l])
            cache_memory[integer_to_binary(i,math.log2(k))]=s #adding block to line

def print_cache_memory(cache_memory):
    print("cache memory")
    for i in cache_memory:
        for j in range(0,len(cache_memory[i])):
            for k in cache_memory[i][j][1]:
                print(cache_memory[i][j][0]+" "+i+" "+k +" "+cache_memory[i][j][1][k])
        print()
    # print(cache_memory)

def increase_index(index,no_of_lines):
    index+=1
    index=index%no_of_lines
    return int(index)

def decrease_index(index,no_of_lines):
    index-=1
    if(index<0):
        index+=no_of_lines
    return int(index)

def input_main_memory(k,main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks, no_of_lines,size_of_block,pointers_l1,pointers_l2,address="",word=""):
    #assuming written in main memory
    #block address + bloack offset
    if(address==""):
        address=input("Enter the address where data is to be stored:")
        word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks, no_of_lines/2,size_of_block,pointers_l1,k,1,address,word)
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks, no_of_lines,size_of_block,pointers_l2,k,1,address,word)
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=floating_to_binary(word)

def input_cache_memory(main_memory,cache_memory,no_of_blocks, no_of_lines,size_of_block,pointers,k,flag=1,address="",word=""):
    if(address==""):
        address=input("Enter the address where data is to be stored:")
    if(word==""):
        word=float(input("Enter the number:"))#should be an integer or floating point
    tag=address[:int(math.log2(no_of_blocks/k))]
    set_no=address[int(math.log2(no_of_blocks/k)):int(math.log2(no_of_blocks))]
    block_offset=address[int(math.log2(no_of_blocks)):]
    m=floating_to_binary(word)
    flag2=0
    for i in range(0,len(cache_memory[set_no])):
        if(cache_memory[set_no][i][0]==tag):
            cache_memory[set_no][i][1][block_offset]=m
            flag2=1
    if(flag2==0 and flag==0):
        import_block_from_main_memory(pointers,k,no_of_blocks,no_of_lines,cache_memory,main_memory,address)
        cache_memory[set_no][int(decrease_index(pointers[set_no],no_of_lines/k))][1][block_offset]=m
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=m

def input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,no_of_blocks,size_of_block):
    address=input("Enter the address where data is to be stored:")
    word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,pointers_l1,k,0,address,word)
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,pointers_l2,k,0,address,word)

def input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,no_of_blocks,size_of_block):
    address=input("Enter the address where data is to be stored:")
    word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,pointers_l2,k,0,address,word)
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,pointers_l1,k,1,address,word)    




def import_block_from_main_memory(pointers,k,no_of_blocks,no_of_lines,cache_memory,main_memory,x=""):
    if(x==""):
        address=input("Enter the address: ")
    else:
        address=x
    set_no=address[int(math.log2(no_of_blocks/k)):int(math.log2(no_of_blocks))]
    tag=address[:int(math.log2(no_of_blocks/k))]
    flag2=0
    for i in range(0,len(cache_memory[set_no])):
        if(cache_memory[set_no][i][0]==tag):
            flag2=1
    if(flag2==0):
        cache_memory[set_no][pointers[set_no]][0]=tag
        cache_memory[set_no][pointers[set_no]][1]=main_memory[address[:int(math.log2(no_of_blocks))]]
        pointers[set_no]=increase_index(pointers[set_no],no_of_lines/k)

def import_block_from_l2_cache_memory(no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,main_memory):#lines of l2 cache
    address=input("Enter the address: ")
    tag=address[:int(math.log2(no_of_blocks/k))]
    line_no=address[int(math.log2(no_of_blocks/k)):int(math.log2(no_of_blocks))]
    import_block_from_main_memory(pointers_l1,k,no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,address)
    flg=0
    for i in range(0,len(cache_memory_l2[line_no])):
        if(cache_memory_l2[line_no][i][0]==tag):
            flg=1
            break
    if(flg==0):
        import_block_from_main_memory(pointers_l2,k,no_of_blocks,no_of_lines,cache_memory_l2,main_memory,address)

def search_in_cache_memory(no_of_blocks,no_of_lines,cache_memory,main_memory,pointers_l1,k,pointers_l2=[],cache_memory_2={},cache_type="l2",address=""):
    if(address==""):
        address=input("Enter the address: ")
    tag=address[:int(math.log2(no_of_blocks/k))]
    block_offset=address[int(math.log2(no_of_blocks)):]
    flag2=0
    for i in cache_memory:
        for j in range(0,len(cache_memory[i])):
            if(cache_memory[i][j][0]==tag):
                x=cache_memory[i][j][1][block_offset]
                flag2=1
                print(x)
                print(binary_to_float(x))
                break
    if(flag2==0):
        print("cache miss")
        if(cache_type=="l1"):
            search_in_cache_memory(no_of_blocks,no_of_lines*2,cache_memory_2,main_memory,pointers_l2,k,[],{},"l2",address)
        block_address=address[:int(math.log2(no_of_blocks))]
        tag=address[:int(math.log2(no_of_blocks/k))]
        set_no=address[int(math.log2(no_of_blocks/k)):int(math.log2(no_of_blocks))]
        if(cache_type=="l1"):
            cache_memory[set_no][pointers_l1[set_no]][0]=tag
            cache_memory[set_no][pointers_l1[set_no]][1]=main_memory[block_address]
            x=cache_memory[set_no][pointers_l1[set_no]][1][block_offset]
            pointers_l1[set_no]=increase_index(pointers_l1[set_no],no_of_lines/k)
        else:
            cache_memory[set_no][pointers_l1[set_no]][0]=tag
            cache_memory[set_no][pointers_l1[set_no]][1]=main_memory[block_address]
            x=cache_memory[set_no][pointers_l1[set_no]][1][block_offset]
            pointers_l1[set_no]=increase_index(pointers_l1[set_no],no_of_lines/k)
        if(cache_type!="l1"):
            print(x)
            print(binary_to_float(x))

    
    


def k_associative_map_cache():
    size_of_cache=int(input("enter size of cache:"))
    size_of_block=int(input("enter size of block:"))
    k=int(input("enter k :"))
    size_of_main_memory=int(input("enter size of main memory:"))
    pointers_l1={}
    pointers_l2={}
    word_size=64#no of bits in 1 word also type of cache and memory
    no_of_lines=size_of_cache/size_of_block
    no_of_blocks=size_of_main_memory/size_of_block
    block_offset_bytes=math.log(size_of_block,2)
    main_memory={}
    cache_memory_l1={}
    cache_memory_l2={}
    initialize_cache_memory(cache_memory_l1,k,no_of_lines/2,no_of_blocks,size_of_block,pointers_l1)
    initialize_cache_memory(cache_memory_l2,k,no_of_lines,no_of_blocks,size_of_block,pointers_l2)
    initialize_main_memory(main_memory,no_of_blocks,size_of_block)
    while(True):
        print()
        print("1. Write to main memory")
        print("2. Write to cache memory L1")
        print("3. Write to cache memory L2")
        print("4. Search from main memory")
        print("5. Search from cache memory L1")
        print("6. Search from cache memory L2")
        print("7. Import block from main memory to cache L2")
        print("8. Import block from cache L2 to cache L1")
        print("9. Print cache memory L1")
        print("10. Print cache memory L2")
        print("11. Print main memory")
        print("12. exit")
        a=input("Enter the option: ")
        temp=0
        try:
            a=int(a)
        except:
            pass
        if(a==1):
            input_main_memory(k,main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,pointers_l1,pointers_l2)
        elif(a==2):
            input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,no_of_blocks,size_of_block)
        elif(a==3):
            input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,no_of_blocks,size_of_block)
        elif(a==4):
            search_in_main_memory(main_memory,no_of_blocks)
        elif(a==5):
            search_in_cache_memory(no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,pointers_l1,k,pointers_l2,cache_memory_l2,"l1")
        elif(a==6):
            search_in_cache_memory(no_of_blocks,no_of_lines,cache_memory_l2,main_memory,pointers_l2,k)
        elif(a==7):
            import_block_from_main_memory(pointers_l2,k,no_of_blocks,no_of_lines,cache_memory_l2,main_memory)
        elif(a==8):
            import_block_from_l2_cache_memory(no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,pointers_l1,pointers_l2,k,main_memory)
        elif(a==9):
            print_cache_memory(cache_memory_l1)
        elif(a==10):
            print_cache_memory(cache_memory_l2)
        elif(a==11):
            print_main_memory(main_memory)
        elif(a==12):
            break

