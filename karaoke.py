#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class KaraokeLocal

    def __init__ (self, fsmil):
        ssHandler = smallsmilhandler.SmallSMILHandler()
        self.taglist = ssHandler.get_tags()
        parser = make_parser()
        parser.setContentHandler(ssHandler)
        parser.parse(fmsil)
        
    def __str__ (self)
        for dic in self.taglist:
            print(dic['tag'] + '\t', end='')
        for atribs in dic:
            if atribs == 'tag':
                pass
            else:
                print(atribs + '=' + dic[atribs] + '\t', end='')
            print('\n')
            
    def to_json (self, fsmil, fjson)
        if fjson == '':
            fjson == fsmil.split('.')[0] + '.json'
        json.dump(self.taglist, open(fjson, 'w'))
              
    def do_local (self)
        for dic in self.taglist:
            for atribs in dic:
                if atribs == 'src' and 'http' in dic[atribs]:
                    urllib.request.urlretrieve(dic[atribs], dic[atribs][dic[atribs].rfind('/') + 1:])
                    dic[atribs] = dic[atribs][dic[atribs].rfind('/') + 1:]

if __name__ == '__main__':
    
    try:
        __init__(sys.argv[1])
    except IndexError:
            sys.exit("Usage: python3 karaoke.py file.smil")





            

                    



    
