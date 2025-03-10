def log(filename=""):
    """логирует функцию в файл, указанном в параметре filename,
    если этот параметр пуст, то фукнция логируется в консоль"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
                message = f"{function.__name__} ok"
            except Exception as e:
                message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename == "":
                print(message)
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            return message
        return wrapper
    return decorator
