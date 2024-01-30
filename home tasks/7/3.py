def get_pins(s):
    U = {
        '1':'24',
        '2':'135',
        '3':'26',
        '4':'157',
        '5':'2468',
        '6':'359',
        '7':'48',
        '8':'579',
        '9':'68'
    }
    n = len(s)
    A = []
    for i in range(n):
        A.append(U[s[i]])
    for i in range(n):
        ...

if __name__ == '__main__':
    get_pins('123')