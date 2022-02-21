import json


def sabber(day,less,ma,teach,fach,etea,eles,lass):
    if ma == "Vertretung":
        if len(fach) < 4:
            stra = "Am " , day , " habt ihr in der ", less, ". Stunde " , fach , " ", " bei " , etea, " anstatt ", teach
        else:
            stra = "Am " , day , " habt ihr in der ", less, ". Stunde anstatt " , fach , " ", eles, " bei " , etea, " anstatt ", teach
    else:
        stra = "Am " , day , " habt ihr in der ", less, ". Stunde " , fach , " ", ma , " bei " , teach
    stra = ''.join(stra)
    return stra



def main(ta,day,teach,less,fach,etea,eles,lass):
    daylist = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
    dayindex = daylist.index(day)
    with open("ml.json", "r") as f:
        data = json.load(f)
        data = data["Data"][dayindex]
    try:
        if data[less] == teach or teach in data[less]:
            ne = sabber(day,less,ta,teach,fach,etea,eles,lass)
            print(ne)
    except Exception as e:
        print(e)

    try:
        return ne
    except:
        return False
