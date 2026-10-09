def details(**Kwargs):
    print(Kwargs)
    # it will give a dictionary

    for key, value in Kwargs.items():
        print(f"{key} : {value}")


details(name="Anuj", age=18, DOB=2004)
