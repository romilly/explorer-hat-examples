import explorerhat as eh
from time import sleep


def prepare_row(row):
    for each_row in range(4):
        if each_row == row:
            eh.output[each_row].off() # so it's at 5v
        else:
            eh.output[each_row].on()  # so it's at 0v


def wait_for_press():
    while True:
        for row in range(4):
            prepare_row(row)
            for col in range(3):
                pressed = eh.input[col].read()
                # print('row  %d col %d pressed %s ' % (row, col, pressed))
                if eh.input[col].read():
                    return row, col
        sleep(1)


def anything_pressed():
    for row in range(4):
        prepare_row(row)
        for col in range(3):
            if eh.input[col].read():
                return True
    return False


def wait_until_clear():
    pressed = True
    while pressed:
        pressed = anything_pressed()


def wait_for_key():
    row, col = wait_for_press()
    print(row, col)
    sleep(0.1)
    wait_until_clear()
    return row, col


while True:
    row, col = wait_for_key()
    print('row %d col %d pressed' % (row,col))
    sleep(0.1)
