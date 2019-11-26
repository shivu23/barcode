# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:17:14 2019

@author: Shivu
"""

import barcode
hr=barcode.get_barcode_class('ean13')
Hr=hr('1234567891012')
qr=Hr.save('123')
from barcode.writer import ImageWriter
hr=barcode.get_barcode_class('code39')
Hr=hr('1234567891012',writer=ImageWriter())
qr=Hr.save('1234')
Hr=hr('abcdef',writer=ImageWriter())
qr=Hr.save('12345')
