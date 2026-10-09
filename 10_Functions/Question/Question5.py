def greets(user="Anuj"):
    return "Hello , " + user + " ! welcome to our company"


print(greets())
print(greets("ram"))


# def greets(user="Anuj"):
#     return "Hello , ", user, " ! welcome to our company"

# it treat return as tuple because it has comma separated

# print(greets())
# ('Hello , ', 'Anuj', ' ! welcome to our company')
# print(greets("ram"))
# ('Hello , ', 'ram', ' ! welcome to our company')
