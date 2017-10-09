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
#        atrib = ""
        for atribs in dic:
            print(dic['tag'] + '\t', end='')
            if atribs == 'tag':
                pass
            else:
                print(atribs + '=' + dic[atribs] + '\t',)
                #if atribs == 'src':
                    #taglist[i][atribs][:taglist[i][atribs].rfind('/')] = urllib.request.urlretrieve(taglist[i][atribs])
                    


    json.dump(taglist, open('karaoke.json', 'w'))
    
