#Suppose you are told that the one time pad encryption of the message "attack at dawn" is 09e1c5f70a65ac519458e7e53f36
#(the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex)
# What would be the one time pad encryption of the message "attack at dusk" under the same OTP key?

# Run the script with pyenv: pyenv exec python question7.py 

def main():    
    message = "attack at dawn"
    target = "attack at dusk"
    encryptedMessageHex = "09e1c5f70a65ac519458e7e53f36"

    messageHex = message.encode('utf-8').hex()
    key = strxor(messageHex, encryptedMessageHex)
    test = strxor(messageHex, key)
    if encryptedMessageHex != test:
        print("failed to verify encryption")
        exit(1)

    targetHex = target.encode('utf-8').hex()
    encryptedTarget = strxor(targetHex, key)
    print("Question 7 response")
    print(encryptedTarget)    

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):        
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

if __name__ == "__main__":
    main()