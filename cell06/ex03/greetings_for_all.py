def greetings(name="noblestranger"):
    if not isinstance(name, str):
        print("Error:string.")
        return
    print(f"Welcome, {name}!")

greetings()
greetings("Alice")
greetings(123)
greetings(["not", "a", "string"])
