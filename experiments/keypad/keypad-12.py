import explorerhat as eh
from time import sleep


def prepare_column(column):
    for each_col in range(3):
        if each_col == column:
            eh.output[each_col].off() # so it's at 5v
        else:
            eh.output[each_col].on()  # so it's at 0v


def check_for_key():
    while True:
        for col in range(3):
            prepare_column(col)
            for row in range(4):
                if eh.input[col].read():
                    return row, col
        return False


def key_pressed():
    p = False
    while not p:
        p = check_for_key()
    return p


def wait_for_release():
    while key_pressed():
        sleep(0.1)


while True:
    row, col = key_pressed()
    wait_for_release()
    print('row %d col %d pressed' % (row,col))
    sleep(0.1)
