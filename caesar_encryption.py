def caesarEncrypt(text,shift):
    output_str = ""

    for char in text:
        if(char.isupper()):
            shifted_final = ord(char) + (shift%26)
            if(shifted_final > 90):
                shifted_final -= 26
            output_str+=chr(shifted_final)
        elif(char.islower()):
            shifted_final = ord(char) + (shift%26)
            if(shifted_final > 122):
                shifted_final -= 26
            output_str += chr(shifted_final)


    return output_str
