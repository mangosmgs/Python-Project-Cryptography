import math

def print_menu(a_menu):
    """
    The function accepts a dictionary of keys-options like the one shown above
    and prints the menu options stored in that dictionary in an easy-to-read
    format as shown below
    """
    print('==========================')
    for key, value in a_menu.items():
        print(f'{key} = {value}')
    print('==========================')

def create_matrix(row_length, column_length):
    """
    The function expects two integers `row_length` and `column_length`
    as input and returns a matrix of dimension `row_length` x `column_length` 
    which contains space characters(`' '`)
    The outer nested list contains a list of length row_length and each element of this list is itself a
    list of 
    length column_length.
    The inner lists contain strings (a total of column_length strings), all of which are single space 
    characters(' ').
    """
    my_list = []
    for i in range(0, row_length):
        sub_list = []
        for j in range(0, column_length):
            sub_list.append(' ')
        my_list.append(sub_list)
    return my_list

def encode_to_matrix(message_string, column_length):
    """
    The function takes a string `message_string` and an integer
    `column_length` as integer and "writes" the message string
    on to a matrix that has `column_length` many columns.
    1. Calculate the number of rows using the length of the message string and the column length input
    parameters.
    2. Call the `create_matrix()` function with # of rows calculated in the previous step and
    `column_length` to 
    get the matrix with space characters.
    3. Initiate a variable `k` with 0
    4. for-loop over the range(# of rows)
        for-loop over the range(# of columns)
            set the corresponding row and column of the matrix to the k-th character in `message_string`
            increment `k` by 1
            if `k` is greater than or equal to the length of `message_string`, break to go to the next row
        if `k` is greater than or equal to the length of `message_string`, break since you are done with
        the message
    5. return the resulting matrix
    """

    if len(message_string) % column_length == 0:
        rows = len(message_string) // column_length
    else:
        rows = len(message_string) // column_length + 1
    
    matrix = create_matrix(rows, column_length)
    k = 0
    """
    Note that we do not provide the number of rows that the output nested list should contain. You need to 
    find this using the length of message_string and the column_length(Hint: You can divide themessage_string 
    into chunks of length column_length each: how many such chunks will you form? Should you use normal division(/)
    or floor division(//) or something else?).
    """

    for i in range(0, rows):
        for j in range(0, column_length):
            matrix[i][j] = message_string[k]
            k += 1
            if k >= len(message_string):
                break
        if k >= len(message_string):
            break
    return matrix

def encrypt_transposition(message, nColumns):
    """
    Create a 2D matrix with nColumns columns. (You can calculate the number of rows based on the length of
    the message - use the function that you previously wrote to get an empty 2D matrix -
    create_matrix(row_length, column_length)).
    Fill any remaining slots in the end with spaces (in case the last row is not full).
    Construct the encrypted by reading the matrix column by column instead, starting from column #1 and
    going down -
    """
    nRows = math.ceil(len(message) / nColumns)
    empty_matrix = create_matrix(nRows, nColumns)
    comp_matrix = encode_to_matrix(message, nColumns)
    encrypted = ''
    for j in range(nColumns): #over col
        for i in range(len(comp_matrix)): #over row
            encrypted += comp_matrix[i][j]
            i += 1
        j += 1
    return encrypted

def decrypt_transposition(message, nColumns):
    """
    Let's create our 2D-matrix (same way as before). The message is 30 characters, so with 3 columns, you will
    need 10 rows to fit the message:
    Let's start placing the letters column by column (starting from the top left and going down), the way
    the encrypted message was read from the table:
    Read the letters from the newly created matrix row-by-row (left to right starting from the top row) to
    get the plaintext message MESSENGER HAS ARRIVED SAFELY. You'll need to remove the trailing spaces at
    the end!
    """
    nRows = math.ceil(len(message) / nColumns)
    empty_matrix = create_matrix(nRows, nColumns)
    m = 0
    for j in range(nColumns):
        for i in range(0, nRows):
            empty_matrix[i][j] = message[m]
            m += 1
            if m >= len(message):
                break
        if m >= len(message):
            break
    comp_matrix = empty_matrix
    decrypted = ''
    for i in range(len(comp_matrix)):
        for j in range(nColumns):
            decrypted += comp_matrix[i][j]
            j += 1
        i += 1
    return decrypted.strip()

def extend_string(key_string, new_length):
    """
    The function takes a string parameter `key_string` and
    an integer parameter `new_length` and creates a new string
    that is formed by repeating key_string multiple times to
    match the length `new_length`.
    param: key_string is a string that needs to be repeated.
    param: new_length is an integer that denotes the number of times key_string should be repeated.
    """
    if new_length >= 0:
        piece = key_string[0 : -1]
        string_length = len(key_string)
        int_times = new_length // string_length
        dec_times = new_length % string_length
        if new_length >= string_length:
            if dec_times == 0:
                return int_times * key_string
            else:
                return int_times * key_string + piece[0:dec_times]
        else:
            return piece[0:new_length]
    else:
        return None

def extend_vigenere(message, secret):
    """
    Write a function extend_vigenere(message, secret) that accepts the string parameters message
    representing the plaintext message and secret representing the secret phrase/word. The function
    returns a new secret that matches the plaintext message in length, extending or shrinking the passed
    secret if necessary.
    """
    length = len(message)
    new_secret = extend_string(secret, length)
    return new_secret

def get_alphabet_vigenere():
    """
    Write a function get_alphabet_vigenere() that does not have any parameters and returns the string
    containing the entire alphabet. For this lab, the alphabet will be: uppercase English letters followed
    by 0123456789, followed by lowercase English letters.
    """
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'

def encrypt_vigenere(message, secret):
    """
    Write a function encrypt_vigenere(message, secret) that accepts strings for plaintext (readable text)
    and the secret word(not extended). The function should return the encrypted message.
    """
    encrypted_v = ''
    alphabet = get_alphabet_vigenere()
    key = extend_vigenere(message, secret)
    if message == '':
        return ''
    if ' ' in message:
        return -1
    for idx, value in enumerate(message):
        idx_alphabet = alphabet.index(value)
        letter_key = key[idx]
        idx_key = alphabet.index(str(letter_key)) 
        if (idx_alphabet + idx_key) < len(alphabet):
            final_index = idx_alphabet + idx_key
            encrypted_v += alphabet[final_index]
        else:
            final_index = (idx_alphabet + idx_key) % len(alphabet)
            encrypted_v += alphabet[final_index]
    return encrypted_v

def decrypt_vigenere(message, secret):
    """
    This function accepts string arguments as the encrypted message and secret word that was used for
    encryption (not extended)
    """
    alphabet = get_alphabet_vigenere()
    key = extend_vigenere(message, secret)
    decrypted_v = ''
    if message == '':
        return ''
    for idx, value in enumerate(message):
        final_idx = alphabet.index(value)
        letter_key = key[idx]
        idx_key = alphabet.index(letter_key) 
        if final_idx > idx_key:
            decrypted_v += alphabet[(final_idx - idx_key)]
        elif final_idx < idx_key:
            decrypted_v += alphabet[final_idx + len(alphabet) - idx_key]
    return decrypted_v
