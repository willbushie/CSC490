# CSC490 - Hamming Code - Error Correciton Algorithm

# hamming algorithm to produce an 11,16 hamming code, with 5 parity bits
# video that this process was built from: https://www.youtube.com/watch?v=X8jsijhllIA&t=1046s
class HammingCode:
    def __init__(self,input) -> None:
        self.input = input
        self.uncodedSections = []
        self.encodedSections = []
        self.completeEncodedString = ""
        self.completeDecodedString = ""

    # execute all encoding operations - return the encoded string
    def encodeOperation(self):
        self.splitBinInputUncoded(self.input)
        # encode each section
        for section in range(len(self.uncodedSections)):
            self.encode(self.uncodedSections[section])
        # print out the results
        #print(self.encodedSections)
        for section in range(len(self.encodedSections)):
            self.completeEncodedString += self.encodedSections[section]
        # return the entire encoded string to be used for other purposes
        return self.completeEncodedString
    
    # execute all decoding operations - return the decoded string
    def decodeOperation(self):
        self.encodedSections = []
        correctedSections = self.errorCheck(self.input)
        self.completeDecodedString = self.decode(correctedSections)
        # return the entire decoded string to be used for other purposes
        return self.completeDecodedString

    # split a string input into sections of 11 bit strings, and update class attributes
    def splitBinInputUncoded(self,binary):
        section = ""
        currBinary = binary
        while len(currBinary) != 0:
            if len(currBinary) >= 11:
                section = currBinary[:11]
                self.uncodedSections.append(section)
                currBinary = currBinary[11:len(currBinary)]
            elif len(currBinary) < 11:
                currBinary = currBinary + "0" * (11 - len(currBinary))
    
    # split a string input of encoded sections into 16 bit sections - return a list of 16 bit strings
    def splitBinInputEncoded(self,binary):
        sections = []
        currBinary = binary
        while len(currBinary) != 0:
            if len(currBinary) >= 16:
                holder = currBinary[:16]
                sections.append(holder)
                currBinary = currBinary[16:len(currBinary)]
        return sections

    # encode an 11 bit string, return a 16 bit list of ints
    def encode(self,binary):
        section = [None] * 16
        binaryList = [None] * 11
        for index in range(len(binary)):
            binaryList[index] = int(binary[index])
        # place the non-parity bits into the section list
        count = 0
        for index in range(len(section)):
            if index != 0 and index != 1 and index != 2 and index != 4 and index != 8:
                section[index] = binaryList[count]
                count += 1
        # place bit 1
        bit1 = section[3] + section[5] + section[7] + section[9] + section[11] + section[13] + section[15]
        if bit1 % 2 == 0:
            section[1] = 0
        else:
            section[1] = 1
        # place bit 2
        bit2 = section[3] + section[6] + section[7] + section[10] + section[11] + section[14] + section[15]
        if bit2 % 2 == 0:
            section[2] = 0
        else:
            section[2] = 1
        # place bit 4
        bit4 = section[5] + section[6] + section[7] + section[12] + section[13] + section[14] + section[15]
        if bit4 % 2 == 0:
            section[4] = 0
        else:
            section[4] = 1
        # place bit 8
        bit8 = section[9] + section[10] + section[11] + section[12] + section[13] + section[14] + section[15]
        if bit8 % 2 == 0:
            section[8] = 0
        else:
            section[8] = 1
        # place bit 0 - instead of checking the entire block, check only the parity bits
        bit0 = section[1] + section[2] + section[4] + section[8]
        if bit0 % 2 == 0:
            section[0] = 0
        else:
            section[0] = 1
        # add this to the class attributes
        returnString = ""
        for index in range(len(section)):
            returnString = returnString + (str(section[index])) 
        self.encodedSections.append(returnString)

    # helper function to place a 1 at the specified indexes   [{"certain":False,"wrong":False}]
    def errorCheckListHelper(self,listOfDict,indexes,label):
        for index in range(len(indexes)):
            if listOfDict[indexes[index]]["certain"] != True:
                if label == 1:
                    listOfDict[indexes[index]]["wrong"] = True
                elif label == 0:
                    listOfDict[indexes[index]]["wrong"] = False
                    listOfDict[indexes[index]]["certain"] = True
        return listOfDict

    # check for errors in a passed binary string (that has been encoded) - return an error corrected string (can fix all but the 0 position)
    def errorCheck(self,binary):
        sections = self.splitBinInputEncoded(binary)
        #print(sections)
        for section in range(len(sections)):
            list = []
            indexesList = []
            for count in range(16):
                indexesList.append({"certain":False,"wrong":False})
            error = {"error":False,"indexes":indexesList}
            for item in range(len(sections[section])):
                list.append(int(sections[section][item]))
            # check for errors using the parity bits
            # check bit 0
            if list[0] != (list[1] + list[2] + list[4] + list[8]) % 2:
                error["error"] = True
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[1,2,4,8],1)
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[3,5,6,7,9,10,11,12,13,14,15],0)
            else:
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[0,1,2,4,8],0)
            # check bit 1
            if list[1] != (list[3] + list[5] + list[7] + list[9] + list[11] + list[13] + list[15]) % 2:
                error["error"] = True
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[3,5,7,9,11,13,15],1)
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[6,10,12,14],0)
                # if bit0 wrong and bit 1 wrong, its bit1
                if error["indexes"][0]["wrong"] == False:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[2,4,8],0)
                else:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[1],0)
            else:
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[1,3,5,7,9,11,13,15],0)
            # check bit 2
            if list[2] != (list[3] + list[6] + list[7] + list[10] + list[11] + list[14] + list[15]) % 2:
                error["error"] = True
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[3,6,7,10,11,14,15],1)
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[5,9,13,12],0)
                # if bit0 and bit2 wrong, its bit2
                if error["indexes"][0]["wrong"] == False:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[1,4,8],0)
                else:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[2],0)
            else:
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[2,3,6,7,10,11,14,15],0)
            # check bit 4
            if list[4] != (list[5] + list[6] + list[7] + list[12] + list[13] + list[14] + list[15]) % 2:
                error["error"] = True
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[5,6,7,12,13,14,15],1)
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[3,9,10,11],0)
                # if bit0 and bit4 wrong, its bit4
                if error["indexes"][0]["wrong"] == False:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[1,2,8],0)
                else:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[4],0)
            else:
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[4,5,6,7,12,13,14,15],0)
            # check bit 8
            if list[8] != (list[9] + list[10] + list[11] + list[12] + list[13] + list[14] + list[15]) % 2:
                error["error"] = True
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[9,10,11,12,13,14,15],1)
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[5,6,7,3],0)
                # if bit0 and bit8 wrong, its bit8
                if error["indexes"][0]["wrong"] == False:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[1,2,4],0)
                else:
                    error["indexes"] = self.errorCheckListHelper(error["indexes"],[0,8],0)
            else:
                error["indexes"] = self.errorCheckListHelper(error["indexes"],[8,9,10,11,12,13,14,15],0)
            # evaluate the error and see if it can be corrected or not (less than 2 errors, it can be corrected, more than 2, cannot be corrected)
            if error["error"] == True:
                errors = 0
                errorIndex = []
                for index in range(len(error["indexes"])):
                    if error["indexes"][index]["wrong"] == True:
                        errors += 1
                        errorIndex.append(index)
                if errors < 2:
                    for index in range(len(errorIndex)):
                        if list[errorIndex[index]] == 0:
                            list[errorIndex[index]] = 1
                        elif list[errorIndex[index]] == 1:
                            list[errorIndex[index]] = 0
            # update the sections list
            checkedString = ""
            for item in range(len(list)):
                checkedString = checkedString + str(list[item])
            sections[section] = checkedString
        #print(sections)
        returnString = ""
        for section in range(len(sections)):
            for index in range(len(sections[section])):
                returnString = returnString + str(sections[section][index])
        return returnString

    # 11 bits to 8 bits once decoding has taken place
    def decode(self,binary):
        encodedSections = self.splitBinInputEncoded(binary)
        decodedSections = []
        for section in range(len(encodedSections)):
            decodedSection = []
            for index in range(16):
                if index != 0 and index != 1 and index != 2 and index != 4 and index != 8:
                    decodedSection.append(encodedSections[section][index])
            decodedSections.append(decodedSection)
        removeBits = (len(decodedSections) * 11 % 8)
        # remove the last bits from the last decoded section
        if removeBits != 0:
            #print(decodedSections[-1])
            decodedSections[-1] = decodedSections[-1][:-removeBits]
            #print(decodedSections[-1])
        stringValue = ""
        for section in range(len(decodedSections)):
            for index in range(len(decodedSections[section])):
                stringValue = stringValue + str(decodedSections[section][index])
        return stringValue



def test():
    # testing the algorithm
    #code = HammingCode("00110001001000000101000001110010")
    #print(code.encodeOperation())
    #code = HammingCode("101000110000100100101000000101000100000111100100")
    #print(code.input)
    #print(code.decode(code.errorCheck(code.input)))
    return 0

test()