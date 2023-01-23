# contains the functions used to encrypt/decrypt files.


def build_command(operation, file_name, key):
    # base command template, {operation} & {file_name} will be replaced by function
    base_command = 'openssl enc -aes-256-cbc {operation} -in "{file_name}" -out "{file_name}"'

    # set the operation to encrypt
    base_command = base_command.replace('{operation}', operation)
    base_command = base_command.replace('{file_name}', file_name, 1)
    # check whether the file is an encrypted file
    if file_name[-4:] == '.enc':
        base_command = base_command.replace('{file_name}', file_name[:-4], -1)
        base_command = base_command + " -d -pass pass:" + '"' + key + '"'
    else:
        base_command = base_command.replace('{file_name}', file_name + '.enc', -1)
        base_command = base_command + " -pass pass:" + '"' + key + '"'
    return base_command


def encrypt_file(file_name, encryption_key):
    return build_command('-e', file_name, encryption_key)


def decrypt_file(file_name, decryption_key):
    return build_command('-d', file_name, decryption_key)

