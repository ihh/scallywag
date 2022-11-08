#!/usr/bin/env python
from os import listdir
dir = 'lorc'
files = listdir(dir)
def makeIcon(name):
    f = open(dir + '/' + name,"r")
    data = f.read()
    return '"' + name.replace('.svg','') + '": "' + data.replace('"','\\"') + '"'
out = open("iconlist.js","w")
out.write ("var iconData = {" + ",\n".join(map(makeIcon,files)) + "}\n")

