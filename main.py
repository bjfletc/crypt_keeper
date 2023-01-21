# author: Brandon Fletcher
# e-mail: brandonjfletcher@gmail.com
# GitHub: https://github.com/bjfletc
# crypt_keeper 🗝️:  an application to be used on macOS/Linux for the purpose of
#                   encrypting/decrypting files using AES-256-CBC encryption that is built into
#                   the operating system of these platforms.

from app_operations import encrypt_file, decrypt_file


def main():
    example_file = 'test.txt'
    # going to make the output files of this application end in .enc
    example_encrypted_file = 'test.txt.enc'
    print(encrypt_file(example_file, 'password'))
    print(decrypt_file(example_encrypted_file, 'password'))


if __name__ == '__main__':
    main()
