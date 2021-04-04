def decrypt(library, message):
    """
    return String for parameters
    library a list of Strings
    and message a string
    """

    # Make lists of keys and values
    keys = []
    values = []
    for entry in library:
        entry = entry.split()
        keys.append(entry[1])
        values.append(entry[0])

    # Decode the message
    decoded = ''
    message = message.split()
    for m in range(len(message)):
        for k in range(len(keys)):
            if message[m] == keys[k]:
                decoded += values[k]
        if message[m] not in keys:
            decoded += '?'
    return decoded