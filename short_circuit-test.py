"""
Created on Monday August 23 2021

@author: İzzet Emre KARSAVURAN
"""

from pyfirmata import Arduino, util
import time
import pyfirmata
import cv2

board = Arduino('COM9')
it = util.Iterator(board)
it.start()

#DIGITAL INPUT
DI1 = board.get_pin('d:3:i')
DI2 = board.get_pin('d:4:i')
DI3 = board.get_pin('d:5:i')
DI4 = board.get_pin('d:6:i')
DI5 = board.get_pin('d:7:i')

#DIGITAL OUTPUT
DO1 = board.get_pin('d:8:o')
DO2 = board.get_pin('d:9:o')
DO3 = board.get_pin('d:10:o')
DO4 = board.get_pin('d:11:o')
DO5 = board.get_pin('d:12:o')
DO6 = board.get_pin('d:13:o')


def read_discrate_inpu_function(coil):

    if coil == 1:
        coil_status = DI1.read()
    if coil ==2:
        coil_status = DI2.read()
    if coil ==3:
        coil_status = DI3.read()
    if coil ==4:
        coil_status = DI4.read()
    if coil ==5:
        coil_status = DI5.read()
    return coil_status


def n_test():
    coil = read_discrate_inpu_function(1)
    if coil:
        status = coil
    else:
        status = coil
    return status


def l_test():
    coil = read_discrate_inpu_function(2)
    if coil:
        status = coil
    else:
        status = coil
    return status


def pe_test():
    coil = read_discrate_inpu_function(3)
    if coil:
        status = coil
    else:
        status = coil
    return status


if __name__ == '__main__':

    while 1:

        img = cv2.imread("img.jpg")
        img = cv2.resize(img, (400, 300))

        pe_status = "NOT OK"
        l_status = "NOT OK"
        n_status = "NOT OK"

        a = l_test()
        b = n_test()
        c = pe_test()


        if a:
            if a==1 :
                        cv2.putText(img, 'L Test: {}'.format("OK"), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    1,
                                    cv2.LINE_AA)
            else :
                        cv2.putText(img, 'L Test: {}'.format("NOT OK"), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    1,
                                    cv2.LINE_AA)
        if not a:
            cv2.putText(img, 'L Test: {}'.format("Baglatı Kurulamadı"), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)

        if b:
            if b == 1:
                    cv2.putText(img, 'N Test: {}'.format("OK"), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255),
                                1,
                                cv2.LINE_AA)
            else:
                    cv2.putText(img, 'N Test: {}'.format("NOT OK"), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255),
                                1,
                                cv2.LINE_AA)
        if not b:
                cv2.putText(img, 'N Test: {}'.format("Baglatı Kurulamadı"), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255),
                            1,
                            cv2.LINE_AA)


        if c:
            if c==1 :
                        cv2.putText(img, 'PE Test: {}'.format("OK"), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    1,
                                    cv2.LINE_AA)
            else :
                        cv2.putText(img, 'PE Test: {}'.format("NOT OK"), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255),
                                    1,
                                    cv2.LINE_AA)
        if not c:
            cv2.putText(img, 'PE Test: {}'.format("Baglatı Kurulamadı"), (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA)


        cv2.imshow('img', img)
        if cv2.waitKey(5) & 0xFF == 27:
            cv2.destroyAllWindows()
            print("Exitting...")
            break