# contains the functions used to encrypt/decrypt files.

def build_command(operation, file_name):
    # base command template, {operation} & {file_name} will be replaced by function
    base_command = 'openssl enc -aes-256-cbc {operation} -in "{file_name}" -out "{file_name}"'

    # command = base_command

    # set the operation to encrypt
    base_command = base_command.replace('{operation}', operation)
    base_command = base_command.replace('{file_name}', file_name, 1)
    # check whether the file is an encrypted file
    if file_name[-4:] == '.enc':
        base_command = base_command.replace('{file_name}', file_name[:-4], -1)
    else:
        base_command = base_command.replace('{file_name}', file_name + '.enc', -1)
    return base_command


def encrypt_file(file_name):
    return build_command('-e', file_name)


def decrypt_file(file_name):
    return build_command('-d', file_name)
