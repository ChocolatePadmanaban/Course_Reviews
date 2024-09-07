# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) < 2:
        return list(sequence)
    sequence_list = list(sequence)
    temp = sequence_list[0]
    remaing_list = [ sequence_list[j] for j in range(1,len(sequence_list))]
    remaing_seq = "".join(remaing_list)
    remaing_seq_permutation = get_permutations(remaing_seq)
    total_permutation = []
    for sub_permutation in remaing_seq_permutation:
        sub_permutation_list = list(sub_permutation)
        for j in range(len(sub_permutation_list)+1):
            sub_permutation_list.insert(j, temp)
            total_permutation.append( "".join(sub_permutation_list.copy()))
            del sub_permutation_list[j]
    total_permutation = list(set(total_permutation))
    return total_permutation
    # pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here
