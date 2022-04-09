from cgi import print_arguments


sen = input('Enter the sentence. : ').split()
print(sen[0])
word = list(sen[0])
print(word[0] in 'aeiouAEIOU')
if word[0] in 'aeiouAEIOU' :
    print("Good Sentence")