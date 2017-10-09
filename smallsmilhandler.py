#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.dicroot = {'width': "", 'height': "", 'background-color': ""}
        self.dicreg = {'id': "", 'top': "", 'bottom': "", 'left': "", 'right': ""}
        self.dicimg = {'src': "", 'region': "", 'begin': "", 'dur': ""}
        self.dicaud = {'src': "", 'begin': "", 'dur': ""}
        self.dictxt = {'src': "", 'region': ""}
        self.list_tags = []
                    
    def startElement(self, name, attrs):
            """
            Método para cuando se abre una etiqueta SMIL
            """
            if name == 'root-layout':
                self.dicroot['width'] = attrs.get('width', "")
                self.dicroot['height'] = attrs.get('height', "")
                self.dicroot['background-color'] = attrs.get('background-color', "")
                self.list_tags.append(self.dicroot)
            elif name == 'region':
                self.dicreg['id'] = attrs.get('id', "")
                self.dicreg['top'] = attrs.get('top', "")
                self.dicreg['bottom'] = attrs.get('bottom', "")
                self.dicreg['left'] = attrs.get('left', "")
                self.dicreg['right'] = attrs.get('right', "")
                self.list_tags.append(self.dicreg)
            elif name == 'img':
                self.dicimg['src'] = attrs.get('src', "")
                self.dicimg['region'] = attrs.get('region', "")
                self.dicimg['begin'] = attrs.get('begin', "")
                self.dicimg['dur'] = attrs.get('dur', "")
                self.list_tags.append(self.dicimg)
            elif name == 'audio':
                self.dicaud['src'] = attrs.get('src', "")
                self.dicaud['begin'] = attrs.get('begin', "")
                self.dicaud['dur'] = attrs.get('dur', "")
                self.list_tags.append(self.dicaud)
            elif name == 'textstream':
                self.dictxt['src'] = attrs.get('src', "")
                self.dictxt['region'] = attrs.get('region', "")
                self.list_tags.append(self.dictxt)

if __name__ == '__main__':
    """
    Programa principal
    """
    parser = make_parser()
    ssHandler = SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(open('karaoke.smil'))
    print(ssHandler.list_tags)
