# CSC490 - Public Key Encryption Implmenetation Assignment

def inverse(a, n):
    t = 0
    newT = 1
    r = n
    newR = a
    while newR != 0:
        quotient = r // newR
        t, newT = newT, t - quotient * newT
        r, newR = newR, r - quotient * newR
    if r > 1: 
        #print("a is not invertable")
        return -1
    if t < 0:
        t = t + n
    return t

class PrivateSide:
    def __init__(self):
        self.a = [1,2,5,11,32,87,141] # private key
        self.q = 1234
        self.r = 901
        self.r1 = inverse(self.r, self.q)

    def GeneratePublicKey(self):
        b = []
        for i in range(len(self.a)):
            b.append(self.r * self.a[i] % self.q)
        return b

    def Decrypt(self, value): # convert 2074 back to a
        # get the converted sum
        newSum = value * self.r1 % self.q
        string = "" # this is used to hold the binary form of the decrypted value
        for i in range(len(self.a) -1, -1, -1):
            if (newSum >= self.a[i]):
                newSum = newSum - self.a[i]
                string = "1" + string
            else:
                string = "0" + string
        # convert binary back to integer
        dec_value = int(string, 2)
        char = chr(dec_value)
        return char

class PublicSide:
    def __init__(self):
        self.b = [] #public key

    def TakeInPublicKey(self,a): # set public key based on private key
        self.b = a

    def Encrypt(self,char): # convert a into 2074
        ascii_code = ord(char) # when char is a, ascii_code is 65
        bin_code = bin(ascii_code)[2:] # when ascii_code is 65, bin_code should be 1000001
        while (len(bin_code) < 7): # we need to append 0's to the head of the string
            bin_code = "0" + bin_code
        result = 0
        for i in range(len(self.b)):
            if bin_code[i] == "1":
                result = result + self.b[i]
        return result

class TestEncryption:
    def __init__(self) -> None:
        self.encryption = PublicSide()
        self.decryption = PrivateSide()
        self.encryption.TakeInPublicKey(self.decryption.GeneratePublicKey())
    
    def SetInput(self, text):
        self.inputText = text

    def cipher(self):
        result_array = []
        for char in self.inputText:
            encrypted_number = self.encryption.Encrypt(char)
            result_array.append(encrypted_number)
        return result_array

    def decipher(self, cipher_list):
        result_str = ""
        for number in cipher_list:
            result_str = result_str + self.decryption.Decrypt(number)
        return result_str
    
test = TestEncryption()
test.SetInput("apple")
ciphered = test.cipher()
print(ciphered)
plainText = test.decipher(ciphered)
print(plainText)

""" testChar = "A"
decryption = PrivateSide()
encryption = PublicSide()
encryption.TakeInPublicKey(decryption.GeneratePublicKey())
cipherText = encryption.Encrypt(testChar)
print(cipherText)
decipherText = decryption.Decrypt(cipherText)
print(decipherText) """