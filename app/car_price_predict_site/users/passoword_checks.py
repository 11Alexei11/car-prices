def is_password_valiable(password: str):
    len_param = False if not len(password) < 8 else True
    diff_param = False if password.isnumeric() else False

    if len_param and diff_param:
        return True

    return False