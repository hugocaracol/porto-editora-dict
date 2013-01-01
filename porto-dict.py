#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib2
from bs4 import BeautifulSoup

"""
Checks a portuguese word synonym in Porto Editora
online dictionary (http://www.infopedia.pt/pesquisa-global/)
You can also check for a foreign word (english, french, etc).
"""

arguments = sys.argv
if len(arguments) < 2:
    print 'Usage: ' + __file__ + ' <word>'
    sys.exit()

word = arguments[1]
infop_req = urllib2.urlopen('http://www.infopedia.pt/pesquisa.jsp?qsFiltro=0&qsExpr='
                            + word)
encoding = infop_req.headers['content-type'].split('charset=')[-1]
html = infop_req.read()

soup = BeautifulSoup(html)
definition_html = soup.find("div", {"id": "divartigo"})
if definition_html is None:
    print 'Não foi encontrado.'
    sys.exit()


word = str(soup.find("span", {"class": "dolVerbeteEntrinfo"})
           .get_text().encode(encoding))
category = soup.find("div", {"id": "divartigo"}) \
    .find("div", {"class": "dolDivisaoCatgram"}) \
    .find("span", {"class": "dolCatgramTbcat"}) \
    .get_text().encode(encoding)
definitions = soup.find("div", {"id": "divartigo"}) \
    .find("div", {"class": "dolDivisaoCatgram"}) \
    .find_all("table", {"class": "dolCatgramAceps"})


print word + ' (' + str(category) + ')'
for d in definitions:
    print d.get_text().encode(encoding)
