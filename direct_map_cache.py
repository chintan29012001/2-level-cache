import math
# to do handle the
# not applicable values of cache block main memory
# size of l1 cache is half of l2 cache 
from helpercode import *        

def initialize_cache_memory(cache_memory,no_of_lines,no_of_blocks,size_of_block):
    if(cache_memory=={}):
        for i in range(0,int(no_of_lines)):
            l={}#line simulation`
            tag="0"*int(math.log2(no_of_blocks)-math.log2(no_of_lines))
            l[tag]={}
            for j in range(0,int(size_of_block)):
                w="0"*64#word simulation
                l[tag][integer_to_binary(j,math.log2(size_of_block))]=w#adding words to block
            cache_memory[integer_to_binary(i,math.log2(no_of_lines))]=l#adding block to line

def input_main_memory(main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks, no_of_lines,size_of_block,address="",word=""):
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
                break
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
        word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks, no_of_lines/2,size_of_block,1,address,word)
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,1,address,word)
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=floating_to_binary(word)

def input_cache_memory(main_memory,cache_memory,no_of_blocks, no_of_lines,size_of_block,flag=1,address="",word=""):
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                break
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    if(word==""):
        word=float(input("Enter the number:"))#should be an integer or floating point
    tag=address[:int(math.log2(no_of_blocks/no_of_lines))]
    line_no=address[int(math.log2(no_of_blocks/no_of_lines)):int(math.log2(no_of_blocks/no_of_lines))+int(math.log2(no_of_lines))]
    block_offset=address[int(math.log2(no_of_blocks/no_of_lines))+int(math.log2(no_of_lines)):]
    m=floating_to_binary(word)
    if(tag in cache_memory[line_no].keys()):
        cache_memory[line_no][tag][block_offset]=m
    elif(flag==0):
        import_block_from_main_memory(no_of_blocks,no_of_lines,cache_memory,main_memory,address[:int(math.log2(no_of_blocks))])
        cache_memory[line_no][tag][block_offset]=m
    main_memory[address[:int(math.log2(no_of_blocks))]][address[int(math.log2(no_of_blocks)):]]=m



def print_cache_memory(cache_memory):
    print("cache memory")
    for i in cache_memory:
        for j in cache_memory[i]:
            for k in cache_memory[i][j]:
                print(j+" "+i+" "+k,end=" ")
                print(cache_memory[i][j][k])
            print()


def import_block_from_main_memory(no_of_blocks,no_of_lines,cache_memory,main_memory,x=""):
    if(x==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                break
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    else:
        address=x
    block_address=address[:int(math.log2(no_of_blocks))]
    tag=address[:int(math.log2(no_of_blocks/no_of_lines))]
    line_no=address[int(math.log2(no_of_blocks/no_of_lines)):int(math.log2(no_of_blocks))]
    cache_memory[line_no]={}
    cache_memory[line_no][tag]=main_memory[block_address]

def import_block_from_l2_cache_memory(no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,main_memory):#lines of l2 cache
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            break
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    tag=address[:int(math.log2(no_of_blocks/no_of_lines))]
    line_no=address[int(math.log2(no_of_blocks/no_of_lines)):int(math.log2(no_of_blocks/no_of_lines))+int(math.log2(no_of_lines))]
    import_block_from_main_memory(no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,address)
    if(tag not in cache_memory_l2[line_no].keys()):
        import_block_from_main_memory(no_of_blocks,no_of_lines,cache_memory_l2,main_memory,address)


def search_in_cache_memory(no_of_blocks,no_of_lines,cache_memory,main_memory,cache_memory2={},cache_type="l2",address=""):
    if(address==""):
        s=0
        for i in main_memory:
            s=len(main_memory[i])
            break
        while(True):
            address=input("Enter the address: ")
            if(len(address)==math.log2(s*no_of_blocks)):
                break
            else:
                print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    tag=address[:int(math.log2(no_of_blocks/no_of_lines))]
    line_no=address[int(math.log2(no_of_blocks/no_of_lines)):int(math.log2(no_of_blocks/no_of_lines))+int(math.log2(no_of_lines))]
    block_offset=address[int(math.log2(no_of_blocks/no_of_lines))+int(math.log2(no_of_lines)):]
    try:
        x=cache_memory[line_no][tag][block_offset]
        print(x)
        print(binary_to_float(x))
    except:
        print("cache miss")
        if(cache_type=="l1"):
            search_in_cache_memory(no_of_blocks,no_of_lines*2,cache_memory2,main_memory,cache_memory2,"l2",address)
        block_address=address[:int(math.log2(no_of_blocks))]
        tag=address[:int(math.log2(no_of_blocks/no_of_lines))]
        line_no=address[int(math.log2(no_of_blocks/no_of_lines)):int(math.log2(no_of_blocks))]
        cache_memory[line_no]={}
        cache_memory[line_no][tag]=main_memory[block_address]
        x=cache_memory[line_no][tag][block_offset]
        if(cache_type=="l2"):
            print(x)
            print(binary_to_float(x))

def input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block):
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            break
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,0,address,word)
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,0,address,word)

def input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block):
    s=0
    for i in main_memory:
        s=len(main_memory[i])
        break
    while(True):
        address=input("Enter the address: ")
        if(len(address)==math.log2(s*no_of_blocks)):
            break
        else:
            print("address requires "+str(int(math.log2(s*no_of_blocks)))+" bits")
    word=float(input("Enter the number:"))#should be an integer or floating point
    input_cache_memory(main_memory,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block,0,address,word)
    input_cache_memory(main_memory,cache_memory_l1,no_of_blocks,no_of_lines/2,size_of_block,1,address,word)



def direct_map_cache():
    size_of_cache=int(input("enter size of cache:"))
    size_of_block=int(input("enter size of block:"))
    size_of_main_memory=int(input("enter size of main memory:"))
    word_size=64#no of bits in 1 word also type of cache and memory
    # size_of_cache=2
    # size_of_main_memory=32
    # size_of_block=2
    no_of_lines=size_of_cache/size_of_block
    no_of_blocks=size_of_main_memory/size_of_block
    block_offset_bytes=math.log(size_of_block,2)
    main_memory={}
    cache_memory_l1={}
    cache_memory_l2={}
    initialize_main_memory(main_memory,no_of_blocks,size_of_block)
    initialize_cache_memory(cache_memory_l2,no_of_lines,no_of_blocks,size_of_block)
    initialize_cache_memory(cache_memory_l1,no_of_lines/2,no_of_blocks,size_of_block)
    while(True):
        print()
        print("1. Write to main memory")
        print("2. Write to cache L1 memory")
        print("3. Write to cache L2 memory")
        print("4. Read from main memory")
        print("5. Read from L1 cache memory")
        print("6. Read from L2 cache memory")
        print("7. Import block from main memory to L2 cache")
        print("8. Import block from L2 to L1 cache")
        print("9. Print L1 cache memory")
        print("10. Print L2 cache memory")
        print("11. Print main memory")
        print("12. exit")
        a=input("Enter the option: ")
        try:
            a=int(a)
        except:
            pass
        if(a==1):
            input_main_memory(main_memory,cache_memory_l1,cache_memory_l2,no_of_blocks,no_of_lines,size_of_block)
        elif(a==2):
            input_l1_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block)
        elif(a==3):
            input_l2_cache_memory(main_memory,no_of_lines,cache_memory_l1,cache_memory_l2,no_of_blocks,size_of_block)
        elif(a==4):
            search_in_main_memory(main_memory,no_of_blocks)
        elif(a==5):
            search_in_cache_memory(no_of_blocks,no_of_lines/2,cache_memory_l1,main_memory,cache_memory_l2,"l1")
        elif(a==6):
            search_in_cache_memory(no_of_blocks,no_of_lines,cache_memory_l2,main_memory)
        elif(a==7):
            import_block_from_main_memory(no_of_blocks,no_of_lines,cache_memory_l2,main_memory)
        elif(a==8):
            import_block_from_l2_cache_memory(no_of_blocks,no_of_lines,cache_memory_l1,cache_memory_l2,main_memory)
        elif(a==9):
            print_cache_memory(cache_memory_l1)
        elif(a==10):
            print_cache_memory(cache_memory_l2)
        elif(a==11):
            print_main_memory(main_memory)
        elif(a==12):
            break




































