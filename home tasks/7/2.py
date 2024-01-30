def rim_converter(N:str):
    
    A = 0
    A += N.count('CM') * 900
    N.replace('CM','')
    A += N.count('CD') * 400
    N.replace('CD','')
    A+= N.count('XC')*90
    N.replace('XC', '')
    A+= N.count('XL')*40
    N.replace('XL','')
    A+= N.count('IX')*9
    N.replace('IX','')
    A+= N.count('IV')*4
    N.replace('IV', '')
    A+= N.count('M')*1000
    N.replace('M','')
    A+= N.count('D')*500
    N.replace('D','')
    A+= N.count('C')*100
    N.replace('C', '')
    A+= N.count('L')*50
    N.replace('L', '')
    A+= N.count('X')*10
    N.replace('X', '')
    A+= N.count('V')*5
    N.replace('V', '')
    A+= N.count('I')
    N.replace('I', '')
    return A

if __name__ == '__main__':
    
    print(rim_converter('MCM'))