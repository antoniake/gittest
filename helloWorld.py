def hello_world():
    print('Inside Function')
    return 'Hello World.'

def main():
    print ('This runs first.')
    hello = hello_world()
    print ('Outside Function')
    print(hello)
    
main() 

# if __name__ == '__main()__':
#     main()
    