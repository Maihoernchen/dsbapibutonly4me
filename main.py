# using https://github.com/nerrixDE/DSBApi
# install with "pip install git+https://github.com/nerrixDE/DSBApi.git#egg=dsbapipy"

import dsbapi as dsb
import time
import datetime
import buyvape


def main():
    days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag", "Samstag","Sonntag"]
    klasse = "11c"
    ownFields = ['Stunde','Lehrer','Fach','Raum','Anmerkung','Typ']
    dsbclient = dsb.DSBApi("243322", "HammerHai21", tablemapper=ownFields)
    entries = dsb.DSBApi.fetch_entries(dsbclient)
    if len(entries) > 1:
        entries = entries[0]
    print(len(entries))
    dayvar = entries[0]
    day = dayvar['day']
    finall = []
    print(entries)
    for s in range(len(entries)):
        step = entries[s]
        teacha = step['Lehrer']
        teach = teacha[:4]
        less = step['Stunde']
        entry = entries[s]
        tap = step['Typ']
        fach = step['Fach']
        if tap == "Vertretung":
            etea = teacha[5:]
            lass = fach[:3]
            eles = fach[4:]
        else:
            etea = ""
            eles = ""
            lass = ""
        if buyvape.main(tap,day,teach,less,fach,etea,eles,lass) and buyvape.main(tap,day,teach,less,fach,etea,eles,lass) not in finall:
            finall.append(buyvape.main(tap,day,teach,less,fach,etea,eles,lass))
            finall.append("\n")
    print(finall)
    return finall
