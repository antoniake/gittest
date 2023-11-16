def hello_world(name):
    # print('Inside Function') # testing not needed
    return f'Hello {name}.'


def main():
    name = 'Antonia'
    print('This runs first.')
    hello = hello_world(name)
    # print('Hello Clara') # We only greet one person
    print(hello)
    

if __name__ == '__main()__':
    main()
    print("goodbye toni and clara!")
