import yaml

def main():
    print('hello')
    with open('test.yaml') as fp:
        obj = yaml.safe_load(fp)
        print(obj)
        #print(obj['listX'][1])
        #print('obj[0]')
        #print(obj[0])
        #print('obj[1]')
        #print(obj[1])

main()
