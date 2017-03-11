trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num

    Numbers in Mandarin follow 3 simple rules.
    # There are words for each of the digits from 0 to 10.
    # For numbers 11-19, the number is pronounced as "ten digit", so for example, 16 would be pronounced (using Mandarin) as "ten six".
    # For numbers between 20 and 99, the number is pronounced as “digit ten digit”, so for example, 37 would be pronounced (using Mandarin) as "three ten seven". If the digit is a zero, it is not included.
    '''
    mand_num = ''
    length = len(us_num)
    for i in range(length):
        if i == 0:
            #mand_num = trans[us_num[length - i - 1]] + mand_num
            if us_num[length - 1 - i] == '0' and length != 1:
                mand_num = mand_num
            else:
                mand_num = trans[us_num[length - i - 1]] + mand_num
        elif i == 1:
            if mand_num != '':
                mand_num = ' ' + mand_num
            if us_num[length-i-1] == '1':
                mand_num = trans['10'] + mand_num
            else:
                mand_num = trans[us_num[length - i - 1]] + ' ' + trans['10'] + mand_num
    return  mand_num

print("'" + convert_to_mandarin('0') + "'")
print("'" + convert_to_mandarin('1') + "'")
print("'" + convert_to_mandarin('10') + "'")
print("'" + convert_to_mandarin('36') + "'")
print("'" + convert_to_mandarin('20') + "'")
print("'" + convert_to_mandarin('16') + "'")
print("'" + convert_to_mandarin('17') + "'")
