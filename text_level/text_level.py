from tkinter.filedialog import askopenfile

text_file = askopenfile(mode='r', title='Select sample text file.')
text = ''
for line in text_file:
    text = text + line.rstrip('\n')
text_file.close()
text = text.lstrip()

n_letters = 0
for letter in text:
    if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
        n_letters = n_letters + 1

n_words = 1
for letter in text:
    if letter == ' ':
        n_words = n_words + 1

n_sentences = 0
for letter in text:
    if letter == '.' or letter == '?' or letter == '!':
        n_sentences = n_sentences + 1

L = n_letters / n_words * 100
S = n_sentences / n_words * 100
index = 0.0588 * L - 0.296 * S - 15.8

if index < 1:
    print("Before grade 1.")
else:
    print("Input text grade: ", round(index))



