#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

if __name__ == '__main__':
    """
    Programa principal
    """
    ssHandler = smallsmilhandler.SmallSMILHandler()
    taglist = ssHandler.get_tags()
    parser = make_parser()
    parser.setContentHandler(ssHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
          
    for dic in taglist:
        print(dic['tag'] + '\t', end='')
        for atribs in dic:
            if atribs == 'tag':
                pass
            else:
                print(atribs + '=' + dic[atribs] + '\t', end='')
                if atribs == 'src':
                    #dic[atribs][dic[atribs].rfind('/') + 1:] =
                    urllib.request.urlretrieve(dic[atribs])
        print('\n')

                    


    json.dump(taglist, open('karaoke.json', 'w'))
    
