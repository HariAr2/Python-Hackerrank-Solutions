def swap_case(s):
    return ''.join([x.upper() if x.islower() else x.lower() for x in s])
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
