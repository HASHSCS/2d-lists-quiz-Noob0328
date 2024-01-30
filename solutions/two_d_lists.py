# TODO: Implement a function that takes a two-dimensional list and returns the sum of each row
def sum_each_row(two_d_list):
    sum=[]
    for row in two_d_list:
        b=0
        for a in row:
            b+=a
        sum.append(b)
    return sum




# TODO: Implement a function that counts the number of non-zero elements in a two-dimensional list
def count_non_zero(two_d_list):
    count=0
    for row in two_d_list:
        for a in row:
            if a > 0:
                count+=1
    return count



    

# TODO: Implement a function that extracts and returns the last element of each row in a two-dimensional list
def last_elements(two_d_list):
    t=[]
    for row in two_d_list:  
        for a in row:
            if a==row[-1]:
                t.append(a)
    return t
                


# TODO: Implement a function that counts the number of times a given value appears in a two-dimensional list
def count_occurrences(two_d_list, value):
    count=0
    for i in range(len(two_d_list)):
        for n in range(len(two_d_list[i])):
            if two_d_list[i][n]==value:
                count+=1
    return count