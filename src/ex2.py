## Input
# "To be or not to be," quoth the Bard, "that is the question".
# The programming contestant replied: "I must disagree. To `C' or not to `C', that is The Question!"
## Output
#
# ``To be or not to be,'' quoth the Bard, ``that is the question''.
# The programming contestant replied: ``I must disagree. To `C' or not to `C', that is The Question!''

def transform(phrase):
    flag = False
    final_phrase = ''
    for char in phrase:
        if char == '"':
            if flag == False:
                flag = True
                final_phrase += '``'
            else:
                flag = False
                final_phrase += "''"
        else:
            final_phrase += char
    return final_phrase

phrase = str(input("Phrase: "))
final_phrase = transform(phrase)
print(final_phrase)