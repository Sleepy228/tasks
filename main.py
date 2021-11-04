import json

if __name__ == '__main__':
    cars = {"BMW": "X6", "AUDI": "A4", "OPEL": "N3"}

    data = {
        "presidents":
        [
        {
            "name": "Joe Biden",
            "species": {"homo" : 1}

        },
        {
            "name": "Donald Trump",
            "species": "homo",
            "key" : [2, "dsadas"]
        },
        {
            "name": "Putin",
            "species": "homo"
        }
        ]
    }
    print("dasdas")

    with open("file.json", "w") as file:
        file.write(json.dumps(cars))

    with open("new.json", "w") as newfile:
        json.dump(data, newfile)

    with open("file.json") as file:
        fileCars = json.load(file)

    for president in data["presidents"]:
        if president["name"] == "Putin":
            print(president)

    with open("rus.txt", "r", encoding="utf-8") as file:
        print(file.readlines())
    array1 = [1, "dsa", 3]
    array2 = [2, 1, 3, "sdas", True, 2.1, [1,2,3], (1.3,), {2, 1}, {2: "s"}]
    print(())
    slovar = {"key": "value", "data": "value2"}

    for item in slovar.keys():
        print(item)
    b = [1,2,3]
    a = set("HELLO WORLD")
    print(a)


    print("login")

