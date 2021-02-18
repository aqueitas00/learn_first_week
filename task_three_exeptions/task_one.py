
def hello_user():
    while True:
        try:
            user_say = input('How are you?\n:')
            if user_say == 'Good':
                print('That`s fine')
                break
            else:
                print('How?', end='')
        except KeyboardInterrupt:
            print('Byebye')
            break

if __name__ == '__main__':
        hello_user()