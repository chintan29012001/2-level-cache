import math
from helpercode import *
#uses first in first out
#chech write for all mappings
def initialize_cache_memory(cache_memory,no_of_lines,no_of_blocks,size_of_block,enter_sequence):
    if(cache_memory==[]):
        for i in range(0,int(no_of_lines)):
            l={}#line simulation`
            for j in range(0,int(size_of_block)):
                l[integer_to_binary(j,math.log2(size_of_block))]="0"*64
            cache_memory.append([integer_to_binary(i,math.log2(no_of_blocks)),l]) #adding block to line
    return 0

def increase_index(index,no_of_lines):
    index+=1
    index=index%no_of_lines
    return int(index)
def decrease_index(index,no_of_lines):
    index-=1
    if(index<0):
        index+=no_of_lines
    return int(index)

def input_main_memory(main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks,index_l1,index_l2,no_of_lines,size_of_block,address="",word=""):
    #assuming written in main memory
    #block address + bloack offset
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                if(address_check(address)):
                        break
                else:
                    print("invalid address")
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
        word=float(input("Enter the number:"))#should be an integer or floating point
    index_l1=input_cache_memory(main_memory,cache_memory_l1,no_of_blocks, no_of_lines/2,size_of_block,index_l1,1,address,word)
    index_l2=input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,index_l2,1,address,word)
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=floating_to_binary(word)
    return index_l1,index_l2

def input_cache_memory(main_memory,cache_memory,no_of_blocks, no_of_lines,size_of_block,index,flag=1,address="",word=""):
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                if(address_check(address)):
                        break
                else:
                    print("invalid address")
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    if(word==""):
        word=float(input("Enter the number:"))#should be an integer or floating point
    
    tag=address[:int(math.log2(no_of_blocks))]
    block_offset=address[int(math.log2(no_of_blocks)):]
    m=floating_to_binary(word)
    flag2=0
    
    for i in range(0,len(cache_memory)):
        if(cache_memory[i][0]==tag):
            cache_memory[i][1][block_offset]=m
            flag2=1
    if(flag2==0 and flag==0):
        index=import_block_from_main_memory(index,no_of_blocks,no_of_lines,cache_memory,main_memory,address)
        cache_memory[int(decrease_index(index,no_of_lines))][1][block_offset]=m
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=m
    return index


def input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block,index_l1,index_l2):
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            if(address_check(address)):
                    break
            else:
                print("invalid address")
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    word=float(input("Enter the number:"))#should be an integer or floating point
    index_l1=input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,index_l1, 0,address,word)
    index_l2=input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,index_l2, 0,address,word)
    return index_l1,index_l2

def input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block,index_l1,index_l2):
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            if(address_check(address)):
                    break
            else:
                print("invalid address")
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    word=float(input("Enter the number:"))#should be an integer or floating point
    index_l2= input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,index_l2,0,address,word)
    index_l1= input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,index_l1,1, address,word)
    return index_l1,index_l2

def print_cache_memory(cache_memory):
    print("cache memory")
    for i in range(0,len(cache_memory)):
        for j in cache_memory[i][1]:
            print(cache_memory[i][0]+" "+j+" "+cache_memory[i][1][j])
        print()


def import_block_from_main_memory(index,no_of_blocks,no_of_lines,cache_memory,main_memory,x=""):
    if(x==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                if(address_check(address)):
                        break
                else:
                    print("invalid address")
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    else:
        address=x
    block_address=address[:int(math.log2(no_of_blocks))]
    tag=address[:int(math.log2(no_of_blocks))]
    flag2=0
    for i in range(0,len(cache_memory)):
        if(cache_memory[i][0]==tag):
            flag2=1
    if(flag2==0):
        cache_memory[int(index)][0]=block_address
        cache_memory[int(index)][1]=main_memory[block_address]
        
        index=int(increase_index(index,no_of_lines))
    return index

def import_block_from_l2_cache_memory(index_l1,index_l2,no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,main_memory):#lines of l2 cache
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            if(address_check(address)):
                    break
            else:
                print("invalid address")
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    tag=address[:int(math.log2(no_of_blocks))]
    index_l1=import_block_from_main_memory(index_l1,no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,address)
    flg=0
    for i in range(0,len(cache_memory_l2)):
        if(cache_memory_l2[i][0]==tag):
            flg=1
            break
    if(flg==0):
        index_l2=import_block_from_main_memory(index_l2,no_of_blocks,no_of_lines,cache_memory_l2,main_memory,address)
    return index_l1,index_l2

def search_in_cache_memory_l1(index_l1,index_l2,no_of_blocks,no_of_lines,cache_memory,main_memory,cache_memory2,address=""):
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                if(address_check(address)):
                        break
                else:
                    print("invalid address")
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    tag=address[:int(math.log2(no_of_blocks))]
    block_offset=address[int(math.log2(no_of_blocks)):]
    flag2=0
    for i in range(0,len(cache_memory)):
        if(cache_memory[i][0]==tag):
            x=cache_memory[i][1][block_offset]
            flag2=1
            print(x)
            print(binary_to_float(x))
            break
    if(flag2==0):
        print("cache miss")
        index_l2=search_in_cache_memory_l2(index_l2,no_of_blocks,no_of_lines*2,cache_memory2,main_memory,address)
        block_address=address[:int(math.log2(no_of_blocks))]
        tag=address[:int(math.log2(no_of_blocks))]
        cache_memory[index_l1][0]=tag
        cache_memory[index_l1][1]=main_memory[block_address]
        x=cache_memory[index_l1][1][block_offset]
        index_l1=int(increase_index(index_l1,no_of_lines))
    return index_l1,index_l2

def search_in_cache_memory_l2(index_l2,no_of_blocks,no_of_lines,cache_memory,main_memory,address=""):
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                if(address_check(address)):
                        break
                else:
                    print("invalid address")
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    tag=address[:int(math.log2(no_of_blocks))]
    block_offset=address[int(math.log2(no_of_blocks)):]
    flag2=0
    for i in range(0,len(cache_memory)):
        if(cache_memory[i][0]==tag):
            x=cache_memory[i][1][block_offset]
            flag2=1
            print(x)
            print(binary_to_float(x))
            break
    if(flag2==0):
        print("cache miss")
        block_address=address[:int(math.log2(no_of_blocks))]
        tag=address[:int(math.log2(no_of_blocks))]
        cache_memory[index_l2][0]=tag
        cache_memory[index_l2][1]=main_memory[block_address]
        x=cache_memory[index_l2][1][block_offset]
        index_l2=int(increase_index(index_l2,no_of_lines))
        print(x)
        print(binary_to_float(x))
    return index_l2




def fully_associative_map_cache():
    while(True):
        try:
            while(True):
                size_of_cache=int(input("enter size of cache:"))    
                if(math.log2(size_of_cache)!=int(math.log2(size_of_cache))):
                    print("size of cache is not in power of 2")
                else:
                    break
            
            while(True):
                size_of_block=int(input("enter size of block:"))    
                if(math.log2(size_of_block)!=int(math.log2(size_of_block))):
                    print("size of block is not in power of 2")
                else:
                    break
            
            while(True):
                size_of_main_memory=int(input("enter size of main memory:"))    
                if(math.log2(size_of_main_memory)!=int(math.log2(size_of_main_memory))):
                    print("size of block is not in power of 2")
                else:
                    break
            if(size_of_main_memory<size_of_block):
                print("size of main memory cannot be smaller than size of block")
                continue
            if(size_of_cache<size_of_block):
                print("size of cache cannot be smaller than size of block")
                continue
            break
        except:
            print("invalid character in input")
    word_size=64#no of bits in 1 word also type of cache and memory
    no_of_lines=size_of_cache/size_of_block
    no_of_blocks=size_of_main_memory/size_of_block
    block_offset_bytes=math.log(size_of_block,2)
    main_memory={}
    cache_memory_l2=[]
    cache_memory_l1=[]
    enter_sequence_l2=0
    enter_sequence_l1=0
    initialize_cache_memory(cache_memory_l2,no_of_lines,no_of_blocks,size_of_block,enter_sequence_l2)
    initialize_cache_memory(cache_memory_l1,no_of_lines/2,no_of_blocks,size_of_block,enter_sequence_l1)
    initialize_main_memory(main_memory,no_of_blocks,size_of_block)
    while(True):
        print("Menu")
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
        a=input("Enter the option:")
        try:
            a=int(a)
        except:
            pass
        if(a==1):
            enter_sequence_l1,enter_sequence_l2=input_main_memory(main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks,enter_sequence_l1,enter_sequence_l2,no_of_lines,size_of_block)
        elif(a==2):
            enter_sequence_l1,enter_sequence_l2=input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block,enter_sequence_l1,enter_sequence_l2)
        elif(a==3):
            enter_sequence_l1,enter_sequence_l2=input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block,enter_sequence_l1,enter_sequence_l2)
        elif(a==4):
            search_in_main_memory(main_memory,no_of_blocks)
        elif(a==5):
            enter_sequence_l1,enter_sequence_l2=search_in_cache_memory_l1(enter_sequence_l1,enter_sequence_l2,no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,cache_memory_l2)
        elif(a==6):
            enter_sequence_l2=search_in_cache_memory_l2(enter_sequence_l2,no_of_blocks,no_of_lines,cache_memory_l2,main_memory)
        elif(a==7):
            enter_sequence_l2=import_block_from_main_memory(enter_sequence_l2,no_of_blocks,no_of_lines,cache_memory_l2,main_memory)
        elif(a==8):
            enter_sequence_l1,enter_sequence_l2=import_block_from_l2_cache_memory(enter_sequence_l1,enter_sequence_l2,no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,main_memory)
        elif(a==9):
            print_cache_memory(cache_memory_l1)
        elif(a==10):
            print_cache_memory(cache_memory_l2)
        elif(a==11):
            print_main_memory(main_memory)
        elif(a==12):
            break

fully_associative_map_cache()
