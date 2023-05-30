n = int(input())

users = {}
logged_users = {}

for x in range(n):
    operation = input().split()
    if operation[0] == 'register':
        username = operation[1]
        password = operation[2]
        if username in users:
            print('fail: user already exists')
        else:
            users[username] = password
            print('success: new user added')
    elif operation[0] == 'login':
        username = operation[1]
        password = operation[2]
        if username not in users:
            print('fail: no such user')
        else:
            if password != users[username]:
                print('fail: incorrect password')
            else:
                if username in logged_users:
                    print('fail: already logged in')
                else:
                    logged_users[username] = password
                    print('success: user logged in')
    elif operation[0] == 'logout':
        username = operation[1]
        if username not in users:
            print('fail: no such user')
        else:
            if username not in logged_users:
                print('fail: already logged out')
            else:
                del logged_users[username]
                print('success: user logged out')