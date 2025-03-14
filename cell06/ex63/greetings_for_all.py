def greeting(name="noble stranger"):
    if not isinstance(name, str):
        print("Error: Name must be a string.")

    else :
        print(f"Hello, {name}.")



greeting()
greeting("Alexander")
greeting(888)