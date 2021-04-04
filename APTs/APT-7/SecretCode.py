def decrypt(message, numbers):
    '''
    message (string) - regular message with 1 or more words
    numbers (list of ints) - list of positive and negative integers

    Return the secret message hidden in message using the list numbers.
    '''

    message = message.split()
    secret = ''
    for i in range(len(message)):
        if not (numbers[i] >= len(message[i]) or numbers[i] < -len(message[i])):
            secret += message[i][numbers[i]]

    return secret

