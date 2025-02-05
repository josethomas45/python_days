def text_analyse(sentence):

    words = sentence.split()
    digit_count = sum(c.isdigit() for c in sentence)
    upper_case_count = sum(c.isupper() for c in sentence)
    lower_case_count = sum(c.islower() for c in sentence)

    print("Number of words:", len(words))
    print("Number of digits:", digit_count)
    print("Number of uppercase letters:", upper_case_count)
    print("Number of lowercase letters:", lower_case_count)

sentence = input("Enter a sentence:")
text_analyse(sentence)
