import time

def search(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    count=0
    start = time.time()
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        j = 0
          
        # For current index i, check  
        # for pattern match */ 
        while(j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
  
        if (j == M):  
            print("Pattern found at index ", i)
            count+=1
    end = time.time()
    print("End of search")
    print("Time taken = "  + str(end-start))
    print(count)


my_file_name = "GCF_000006945.2_ASM694v2_genomic.fna"
my_file = open(my_file_name)
my_file_contents = my_file.read().rstrip("\n")
my_file_contents = my_file_contents.replace('\n', '')
pat = input("Type something to test this out: ")
txt = str(my_file_contents)
#txt = "AAAAAABBBBCCABCAABCCD"
print(txt)
#pat = "ABABCABAB"
search(pat, txt)


# This code is contributed by Bhavya Jain
