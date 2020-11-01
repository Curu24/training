class Node:
    def __init__(self, char = None):
        self.char = char
        self.children = []
        self.end = False

root = Node('*')
curr = root

# recursive insert into the trie
def insert(s, curr):
    if curr.children and curr.children[0].char == s[0]:
        curr = curr.children[0]
    elif len(curr.children) > 1 and curr.children[1].char == s[0]:
        curr = curr.children[1]                
    else:
        new_node = Node(s[0])
        curr.children.append(new_node)
        curr = new_node

    if len(s) > 1:
        s = s[1:]
        insert(s, curr)
    else:
        curr.end = True
    
# search for a string in the trie
def search(sequence):
    tmp_node = root
    found = False
    for letter in sequence:
        common = False
        for child in tmp_node.children:
            if child.char == letter:
                tmp_node = child
                common = True
                break
        if not common:
            return found
    if tmp_node.end:
        found = True
    return found

# user input
print('''Type any number of sequences containing only 2 types
of characters 'a' and 'b' to fill the database (ended by blank entry).''')

sequences = []

while True:
    seq = input("Sequence: ")
    if seq == '':
        break
    sequences.append(seq)

node_no = 0
letter = 'none'

# loads strings into the trie
for seq in sequences:
    insert(seq, root)

print("Select 2 sequences from the database.")

# takes 2 strings from user to compare
seq1 = input("Sequence 1: ")
seq2 = input("Sequence 2: ")

if search(seq1) and search(seq2):
    for i in range(min(len(seq1), len(seq2))):
        if seq1[i] == seq2[i]:
            node_no += 1
            letter = seq1[i]
        else:
            break
    print("Last common node is -", letter, "- with node no.", node_no)
    
else:
    print("One or both the sequences not found in the database.")
