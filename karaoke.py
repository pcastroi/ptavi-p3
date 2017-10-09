#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

if __name__ == '__main__':
    """
    Programa principal
    """
    i = 0
    ssHandler = smallsmilhandler.SmallSMILHandler()
    taglist = ssHandler.get_tags()
    parser = make_parser()
    parser.setContentHandler(ssHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
        
    for diccionario in taglist:
        print(taglist[diccionario])
    #print(taglist)
