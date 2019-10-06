def formated_name(fname, lname, middle=None):
    if middle:
        fullname = f"{fname} {middle} {lname}"
    else:
        fullname = f"{fname} {lname}"

    return fullname.title()



