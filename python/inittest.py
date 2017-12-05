import xml.dom.minidom as dom

#print "Content-type: text/plain\n\n"

baum = dom.parse("config.xml")

for eintrag in baum.firstChild.childNodes:
    if eintrag.nodeName == "config_temp_gauge":
        for knoten in eintrag.childNodes:
                print (knoten.firstChild.data.strip())
