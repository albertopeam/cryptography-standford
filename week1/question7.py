#Suppose you are told that the one time pad encryption of the message "attack at dawn" is 09e1c5f70a65ac519458e7e53f36
#(the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex)
# What would be the one time pad encryption of the message "attack at dusk" under the same OTP key?

# Run the script with pyenv: pyenv exec python question7.py 
import codecs

def main():    
    message = "attack at dawn"
    target =  "attack at dusk"
    encryptedMessageHex = "6c73d5240a948c86981bc294814d"

    messageBytes = bytes(message, 'ascii')
    encryptedMessageBytes = bytes.fromhex(encryptedMessageHex)
    keyBytes = xor(messageBytes, encryptedMessageBytes) 

    verifyBytes = xor(messageBytes, keyBytes)
    if verifyBytes != encryptedMessageBytes:
        print("failed to verify encryption")
        exit(1)

    targetBytes = bytes(target, 'ascii')
    encryptedTargetBytes = xor(targetBytes, keyBytes)
    print(encryptedTargetBytes.hex())

def xor(a,b): 
    return bytes(x^y for x,y in zip(a,b))

if __name__ == "__main__":
    main()