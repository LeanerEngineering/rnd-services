# -*- coding: UTF-8 -*-

"""
Sample-code for managing elemt-trees
"""

#XML-generation
import xml.etree.ElementTree as ET


def simple_tree():
    
    a = ET.Element('a')
    b = ET.SubElement(a, 'b')
    b.text = "B is cool"
    c = ET.SubElement(a, 'c')
    c.text = "C is cool"
    d = ET.SubElement(a, 'd')
    d.text = "D is cool"
     
    
    result = ET.tostring(a, encoding="UTF-8", method="xml") 
    
    return result

    #return Response(result, mimetype='text/xml')
    

def main():
    print 'Start...'
    
    print simple_tree()
    
    print 'mail-end' 

if __name__ == '__main__':
    main()