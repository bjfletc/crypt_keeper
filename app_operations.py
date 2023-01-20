# contains the functions used to encrypt/decrypt files.

# base command template, {operation} & {file_name} will be replaced by functions
base_command = 'openssl enc -aes-256-cbc {operation} -in "{file_name}" -out "{file_name}"'


def encrypt_file(file_name):
    global base_command
    command = base_command

    # set the operation to encrypt
    command = command.replace('{operation}', '-e')
    command = command.replace('{file_name}', file_name, 1)
    command = command.replace('{file_name}', file_name + '.enc', -1)
    return command


def decrypt_file(file_name):
    global base_command
    command = base_command

    # set the operation to decrypt
    command = command.replace('{operation}', '-d')
    command = command.replace('{file_name}', file_name, 1)
    command = command.replace('{file_name}', file_name[:-4], -1)
    return command


# for testing purposes only
if __name__ == '__main__':
    print(encrypt_file('test_file.txt'))
    print(decrypt_file('test_file.txt.enc'))
