email = input("Enter your email: \n> ")

# uName = None
# dName = None


uName = email[:email.index('@')]
dName = email[(email.index('@') + 1):]

if email != '':
    # print('Your username is: ' + email[:email.index('@')] + ', and your domain name is: ' + email[(email.index('@') + 1):])

    print('Your username is: "' + uName + '", and your domain name is: "' + dName + '"')

