user_permission = 14 # 0b1111

READ_PERMISSION = 1 # 0b0001
WRITE_PERMISSION = 2 # 0b0010
EXE_PERMISSION = 4 # 0b0100
DEL_PERMISSION = 8 # 0b1000


def canDo(user_permission, actionPermission):
    def handleAction(func):
        def doAction():
            if (user_permission & actionPermission) != 0:
                func()
            else:
                print('No permission...')
            return None
        return doAction
    return handleAction


@canDo(user_permission, READ_PERMISSION)
def read():
    print('Reading...')


@canDo(user_permission, WRITE_PERMISSION)
def write():
    print('Write...')


@canDo(user_permission, EXE_PERMISSION)
def exe():
    print('Exeing...')


@canDo(user_permission, DEL_PERMISSION)
def delete():
    print('Delling...')


if __name__ == "__main__":
    read()
    write()
    exe()
    delete()
