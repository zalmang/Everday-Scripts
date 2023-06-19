def zinput(inputstm, str="", opt="y/n"):
    if str == "":
        str = input(f"{inputstm} {opt}")
    if str.lower() == "y":
        return 1
    elif str.lower() == "n":
        return 0
    else:
        return zinput("Invalid entry. Please try again (y/n): ")