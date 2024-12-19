
def Datoskukax(x):
    if (x < 1453.6 or abs(1453.6 - x) < 8) and (x > 1437.3):
        valorx = 1453.6
        return valorx

    if (x < 1421.0 or abs(1421.0 - x) < 8) and (x > 1404.7):
        valorx = 1421.0
        return valorx

    if (x < 1388.4 or abs(1388.4 - x) < 8) and (x > 1372.1):
        valorx = 1388.4
        return valorx

    if (x < 1355.8 or abs(1355.8 - x) < 8) and (x > 1339.5):
        valorx = 1355.8
        return valorx

    if (x < 1323.2 or abs(1323.2 - x) < 8) and (x > 1306.9):
        valorx = 1323.2
        return valorx

    if (x < 1290.6 or abs(1290.6 - x) < 8) and (x > 1274.3):
        valorx = 1290.6
        return valorx

    if (x < 1258.0 or abs(1258.0 - x) < 8) and (x > 1241.7):
        valorx = 1258.0
        return valorx

    if (x < 1225.4 or abs(1225.4 - x) < 8) and (x > 1209.1):
        valorx = 1225.4
        return valorx

    if (x < 1192.8 or abs(1192.8 - x) < 8) and (x > 1176.5):
        valorx = 1192.8
        return valorx

    if (x < 1160.2 or abs(1160.2 - x) < 8) and (x > 1143.9):
        valorx = 1160.2
        return valorx

    if (x < 1127.6 or abs(1127.6 - x) < 8) and (x > 1111.3):
        valorx = 1127.6
        return valorx

    if (x < 1095.0 or abs(1095.0 - x) < 8) and (x > 1078.7):
        valorx = 1095.0
        return valorx

    if (x < 1062.4 or abs(1062.4 - x) < 8) and (x > 1046.1):
        valorx = 1062.4
        return valorx

    if (x < 1029.8 or abs(1029.8 - x) < 8) and (x > 1013.5):
        valorx = 1029.8
        return valorx

    if (x < 997.2 or abs(997.2 - x) < 8) and (x > 980.9):
        valorx = 997.2
        return valorx

    if (x < 964.6 or abs(964.6 - x) < 8) and (x > 948.3):
        valorx = 964.6
        return valorx


def Datoskukay(y):
    if (y >= -459.8 or abs(-459.8 - y) <=14) and (y < -432.9):
        valory = -459.8
        return valory

    if (y >= -406.0 or abs(-406.0 - y) <= 14) and (y < -379.1):
        valory = -406.0
        return valory

    if (y >= -352.2 or abs(-352.2 - y) <= 14) and (y < -325.3):
        valory = -352.2
        return valory

    if (y >= -298.4 or abs(-298.4 - y) <= 14) and (y < -271.5):
        valory = -298.4
        return valory

    if (y >= -244.6 or abs(-244.6 - y) <= 14) and (y < -217.7):
        valory = -244.6
        return valory

    if (y >= -190.8 or abs(-190.8 - y) <= 14) and (y < -163.9):
        valory = -190.8
        return valory

    if (y >= -137.0 or abs(-137.0 - y) <= 14) and (y < -110.1):
        valory = -137.0
        return valory

    if (y >= -83.2 or abs(-83.2 - y) <= 14) and (y < -56.3):
        valory = -83.2
        return valory

    if (y >= -29.4 or abs(-29.4 - y) <= 14) and (y < -2.5):
        valory = -29.4
        return valory

    if (y >= 24.4 or abs(24.4 - y) <= 14) and (y < 51.3):
        valory = 24.4
        return valory

    if (y >= 78.2 or abs(78.2 - y) <= 14) and (y < 105.1):
        valory = 78.2
        return valory

    if (y >= 132.0 or abs(132.0 - y) <= 14) and (y < 158.9):
        valory = 132.0
        return valory

    if (y >= 185.8 or abs(185.8 - y) <=14) and (y < 212.7):
        valory = 185.8
        return valory

    if (y >= 239.6 or abs(239.6 - y) <= 14) and (y < 266.5):
        valory = 239.6
        return valory

    if (y >= 293.4 or abs(293.4 - y) <= 14) and (y < 320.3):
        valory = 293.4
        return valory

    if (y >= 347.2 or abs(347.2 - y) <= 14) and (y < 374.1):
        valory = 347.2
        return valory


def Kukadot(dotx,doty):
    if dotx == 1453.6 and doty == -406.0:
        Datok = "001"
        return Datok
    if dotx == 1453.6 and doty == -352.2:
        Datok = "002"
        return Datok
    if dotx == 1453.6 and doty == -298.4:
        Datok = "003"
        return Datok
    if dotx == 1453.6 and doty == -244.6:
        Datok = "004"
        return Datok
    if dotx == 1453.6 and doty == -190.8:
        Datok = "005"
        return Datok
    if dotx == 1453.6 and doty == -137.0:
        Datok = "006"
        return Datok
    if dotx == 1453.6 and doty == -83.2:
        Datok = "007"
        return Datok
    if dotx == 1453.6 and doty == -29.4:
        Datok = "008"
        return Datok
    if dotx == 1453.6 and doty == 24.4:
        Datok = "009"
        return Datok
    if dotx == 1453.6 and doty == 78.2:
        Datok = "010"
        return Datok
    if dotx == 1453.6 and doty == 132.0:
        Datok = "011"
        return Datok
    if dotx == 1453.6 and doty == 185.8:
        Datok = "012"
        return Datok
    if dotx == 1453.6 and doty == 239.6:
        Datok = "013"
        return Datok
    if dotx == 1453.6 and doty == 293.4:
        Datok = "014"
        return Datok
    if dotx == 1453.6 and doty == 347.2:
        Datok = "015"
        return Datok
    if dotx == 1421.0 and doty == -459.8:
        Datok = "016"
        return Datok
    if dotx == 1421.0 and doty == -406.0:
        Datok = "017"
        return Datok
    if dotx == 1421.0 and doty == -352.2:
        Datok = "018"
        return Datok
    if dotx == 1421.0 and doty == -298.4:
        Datok = "019"
        return Datok
    if dotx == 1421.0 and doty == -244.6:
        Datok = "020"
        return Datok
    if dotx == 1421.0 and doty == -190.8:
        Datok = "021"
        return Datok
    if dotx == 1421.0 and doty == -137.0:
        Datok = "022"
        return Datok
    if dotx == 1421.0 and doty == -83.2:
        Datok = "023"
        return Datok
    if dotx == 1421.0 and doty == -29.4:
        Datok = "024"
        return Datok
    if dotx == 1421.0 and doty == 24.4:
        Datok = "025"
        return Datok
    if dotx == 1421.0 and doty == 78.2:
        Datok = "026"
        return Datok
    if dotx == 1421.0 and doty == 132.0:
        Datok = "027"
        return Datok
    if dotx == 1421.0 and doty == 185.8:
        Datok = "028"
        return Datok
    if dotx == 1421.0 and doty == 239.6:
        Datok = "029"
        return Datok
    if dotx == 1421.0 and doty == 293.4:
        Datok = "030"
        return Datok
    if dotx == 1421.0 and doty == 347.2:
        Datok = "031"
        return Datok
    if dotx == 1388.4 and doty == -459.8:
        Datok = "032"
        return Datok
    if dotx == 1388.4 and doty == -406.0:
        Datok = "033"
        return Datok
    if dotx == 1388.4 and doty == -352.2:
        Datok = "034"
        return Datok
    if dotx == 1388.4 and doty == -298.4:
        Datok = "035"
        return Datok
    if dotx == 1388.4 and doty == -244.6:
        Datok = "036"
        return Datok
    if dotx == 1388.4 and doty == -190.8:
        Datok = "037"
        return Datok
    if dotx == 1388.4 and doty == -137.0:
        Datok = "038"
        return Datok
    if dotx == 1388.4 and doty == -83.2:
        Datok = "039"
        return Datok
    if dotx == 1388.4 and doty == -29.4:
        Datok = "040"
        return Datok
    if dotx == 1388.4 and doty == 24.4:
        Datok = "041"
        return Datok
    if dotx == 1388.4 and doty == 78.2:
        Datok = "042"
        return Datok
    if dotx == 1388.4 and doty == 132.0:
        Datok = "043"
        return Datok
    if dotx == 1388.4 and doty == 185.8:
        Datok = "044"
        return Datok
    if dotx == 1388.4 and doty == 239.6:
        Datok = "045"
        return Datok
    if dotx == 1388.4 and doty == 293.4:
        Datok = "046"
        return Datok
    if dotx == 1388.4 and doty == 347.2:
        Datok = "047"
        return Datok
    if dotx == 1355.8 and doty == -459.8:
        Datok = "048"
        return Datok
    if dotx == 1355.8 and doty == -406.0:
        Datok = "049"
        return Datok
    if dotx == 1355.8 and doty == -352.2:
        Datok = "050"
        return Datok
    if dotx == 1355.8 and doty == -298.4:
        Datok = "051"
        return Datok
    if dotx == 1355.8 and doty == -244.6:
        Datok = "052"
        return Datok
    if dotx == 1355.8 and doty == -190.8:
        Datok = "053"
        return Datok
    if dotx == 1355.8 and doty == -137.0:
        Datok = "054"
        return Datok
    if dotx == 1355.8 and doty == -83.2:
        Datok = "055"
        return Datok
    if dotx == 1355.8 and doty == -29.4:
        Datok = "056"
        return Datok
    if dotx == 1355.8 and doty == 24.4:
        Datok = "057"
        return Datok
    if dotx == 1355.8 and doty == 78.2:
        Datok = "058"
        return Datok
    if dotx == 1355.8 and doty == 132.0:
        Datok = "059"
        return Datok
    if dotx == 1355.8 and doty == 185.8:
        Datok = "060"
        return Datok
    if dotx == 1355.8 and doty == 239.6:
        Datok = "061"
        return Datok
    if dotx == 1355.8 and doty == 293.4:
        Datok = "062"
        return Datok
    if dotx == 1355.8 and doty == 347.2:
        Datok = "063"
        return Datok
    if dotx == 1323.2 and doty == -459.8:
        Datok = "064"
        return Datok
    if dotx == 1323.2 and doty == -406.0:
        Datok = "065"
        return Datok
    if dotx == 1323.2 and doty == -352.2:
        Datok = "066"
        return Datok
    if dotx == 1323.2 and doty == -298.4:
        Datok = "067"
        return Datok
    if dotx == 1323.2 and doty == -244.6:
        Datok = "068"
        return Datok
    if dotx == 1323.2 and doty == -190.8:
        Datok = "069"
        return Datok
    if dotx == 1323.2 and doty == -137.0:
        Datok = "070"
        return Datok
    if dotx == 1323.2 and doty == -83.2:
        Datok = "071"
        return Datok
    if dotx == 1323.2 and doty == -29.4:
        Datok = "072"
        return Datok
    if dotx == 1323.2 and doty == 24.4:
        Datok = "073"
        return Datok
    if dotx == 1323.2 and doty == 78.2:
        Datok = "074"
        return Datok
    if dotx == 1323.2 and doty == 132.0:
        Datok = "075"
        return Datok
    if dotx == 1323.2 and doty == 185.8:
        Datok = "076"
        return Datok
    if dotx == 1323.2 and doty == 239.6:
        Datok = "077"
        return Datok
    if dotx == 1323.2 and doty == 293.4:
        Datok = "078"
        return Datok
    if dotx == 1323.2 and doty == 347.2:
        Datok = "079"
        return Datok
    if dotx == 1290.6 and doty == -459.8:
        Datok = "080"
        return Datok
    if dotx == 1290.6 and doty == -406.0:
        Datok = "081"
        return Datok
    if dotx == 1290.6 and doty == -352.2:
        Datok = "082"
        return Datok
    if dotx == 1290.6 and doty == -298.4:
        Datok = "083"
        return Datok
    if dotx == 1290.6 and doty == -244.6:
        Datok = "084"
        return Datok
    if dotx == 1290.6 and doty == -190.8:
        Datok = "085"
        return Datok
    if dotx == 1290.6 and doty == -137.0:
        Datok = "086"
        return Datok
    if dotx == 1290.6 and doty == -83.2:
        Datok = "087"
        return Datok
    if dotx == 1290.6 and doty == -29.4:
        Datok = "088"
        return Datok
    if dotx == 1290.6 and doty == 24.4:
        Datok = "089"
        return Datok
    if dotx == 1290.6 and doty == 78.2:
        Datok = "090"
        return Datok
    if dotx == 1290.6 and doty == 132.0:
        Datok = "091"
        return Datok
    if dotx == 1290.6 and doty == 185.8:
        Datok = "092"
        return Datok
    if dotx == 1290.6 and doty == 239.6:
        Datok = "093"
        return Datok
    if dotx == 1290.6 and doty == 293.4:
        Datok = "094"
        return Datok
    if dotx == 1290.6 and doty == 347.2:
        Datok = "095"
        return Datok
    if dotx == 1258.0 and doty == -459.8:
        Datok = "096"
        return Datok
    if dotx == 1258.0 and doty == -406.0:
        Datok = "097"
        return Datok
    if dotx == 1258.0 and doty == -352.2:
        Datok = "098"
        return Datok
    if dotx == 1258.0 and doty == -298.4:
        Datok = "099"
        return Datok
    if dotx == 1258.0 and doty == -244.6:
        Datok = "100"
        return Datok
    if dotx == 1258.0 and doty == -190.8:
        Datok = "101"
        return Datok
    if dotx == 1258.0 and doty == -137.0:
        Datok = "102"
        return Datok
    if dotx == 1258.0 and doty == -83.2:
        Datok = "103"
        return Datok
    if dotx == 1258.0 and doty == -29.4:
        Datok = "104"
        return Datok
    if dotx == 1258.0 and doty == 24.4:
        Datok = "105"
        return Datok
    if dotx == 1258.0 and doty == 78.2:
        Datok = "106"
        return Datok
    if dotx == 1258.0 and doty == 132.0:
        Datok = "107"
        return Datok
    if dotx == 1258.0 and doty == 185.8:
        Datok = "108"
        return Datok
    if dotx == 1258.0 and doty == 239.6:
        Datok = "109"
        return Datok
    if dotx == 1258.0 and doty == 293.4:
        Datok = "110"
        return Datok
    if dotx == 1258.0 and doty == 347.2:
        Datok = "111"
        return Datok
    if dotx == 1225.4 and doty == -459.8:
        Datok = "112"
        return Datok
    if dotx == 1225.4 and doty == -406.0:
        Datok = "113"
        return Datok
    if dotx == 1225.4 and doty == -352.2:
        Datok = "114"
        return Datok
    if dotx == 1225.4 and doty == -298.4:
        Datok = "115"
        return Datok
    if dotx == 1225.4 and doty == -244.6:
        Datok = "116"
        return Datok
    if dotx == 1225.4 and doty == -190.8:
        Datok = "117"
        return Datok
    if dotx == 1225.4 and doty == -137.0:
        Datok = "118"
        return Datok
    if dotx == 1225.4 and doty == -83.2:
        Datok = "119"
        return Datok
    if dotx == 1225.4 and doty == -29.4:
        Datok = "120"
        return Datok
    if dotx == 1225.4 and doty == 24.4:
        Datok = "121"
        return Datok
    if dotx == 1225.4 and doty == 78.2:
        Datok = "122"
        return Datok
    if dotx == 1225.4 and doty == 132.0:
        Datok = "123"
        return Datok
    if dotx == 1225.4 and doty == 185.8:
        Datok = "124"
        return Datok
    if dotx == 1225.4 and doty == 239.6:
        Datok = "125"
        return Datok
    if dotx == 1225.4 and doty == 293.4:
        Datok = "126"
        return Datok
    if dotx == 1225.4 and doty == 347.2:
        Datok = "127"
        return Datok
    if dotx == 1192.8 and doty == -459.8:
        Datok = "128"
        return Datok
    if dotx == 1192.8 and doty == -406.0:
        Datok = "129"
        return Datok
    if dotx == 1192.8 and doty == -352.2:
        Datok = "130"
        return Datok
    if dotx == 1192.8 and doty == -298.4:
        Datok = "131"
        return Datok
    if dotx == 1192.8 and doty == -244.6:
        Datok = "132"
        return Datok
    if dotx == 1192.8 and doty == -190.8:
        Datok = "133"
        return Datok
    if dotx == 1192.8 and doty == -137.0:
        Datok = "134"
        return Datok
    if dotx == 1192.8 and doty == -83.2:
        Datok = "135"
        return Datok
    if dotx == 1192.8 and doty == -29.4:
        Datok = "136"
        return Datok
    if dotx == 1192.8 and doty == 24.4:
        Datok = "137"
        return Datok
    if dotx == 1192.8 and doty == 78.2:
        Datok = "138"
        return Datok
    if dotx == 1192.8 and doty == 132.0:
        Datok = "139"
        return Datok
    if dotx == 1192.8 and doty == 185.8:
        Datok = "140"
        return Datok
    if dotx == 1192.8 and doty == 239.6:
        Datok = "141"
        return Datok
    if dotx == 1192.8 and doty == 293.4:
        Datok = "142"
        return Datok
    if dotx == 1192.8 and doty == 347.2:
        Datok = "143"
        return Datok
    if dotx == 1160.2 and doty == -459.8:
        Datok = "144"
        return Datok
    if dotx == 1160.2 and doty == -406.0:
        Datok = "145"
        return Datok
    if dotx == 1160.2 and doty == -352.2:
        Datok = "146"
        return Datok
    if dotx == 1160.2 and doty == -298.4:
        Datok = "147"
        return Datok
    if dotx == 1160.2 and doty == -244.6:
        Datok = "148"
        return Datok
    if dotx == 1160.2 and doty == -190.8:
        Datok = "149"
        return Datok
    if dotx == 1160.2 and doty == -137.0:
        Datok = "150"
        return Datok
    if dotx == 1160.2 and doty == -83.2:
        Datok = "151"
        return Datok
    if dotx == 1160.2 and doty == -29.4:
        Datok = "152"
        return Datok
    if dotx == 1160.2 and doty == 24.4:
        Datok = "153"
        return Datok
    if dotx == 1160.2 and doty == 78.2:
        Datok = "154"
        return Datok
    if dotx == 1160.2 and doty == 132.0:
        Datok = "155"
        return Datok
    if dotx == 1160.2 and doty == 185.8:
        Datok = "156"
        return Datok
    if dotx == 1160.2 and doty == 239.6:
        Datok = "157"
        return Datok
    if dotx == 1160.2 and doty == 293.4:
        Datok = "158"
        return Datok
    if dotx == 1160.2 and doty == 347.2:
        Datok = "159"
        return Datok
    if dotx == 1127.6 and doty == -459.8:
        Datok = "160"
        return Datok
    if dotx == 1127.6 and doty == -406.0:
        Datok = "161"
        return Datok
    if dotx == 1127.6 and doty == -352.2:
        Datok = "162"
        return Datok
    if dotx == 1127.6 and doty == -298.4:
        Datok = "163"
        return Datok
    if dotx == 1127.6 and doty == -244.6:
        Datok = "164"
        return Datok
    if dotx == 1127.6 and doty == -190.8:
        Datok = "165"
        return Datok
    if dotx == 1127.6 and doty == -137.0:
        Datok = "166"
        return Datok
    if dotx == 1127.6 and doty == -83.2:
        Datok = "167"
        return Datok
    if dotx == 1127.6 and doty == -29.4:
        Datok = "168"
        return Datok
    if dotx == 1127.6 and doty == 24.4:
        Datok = "169"
        return Datok
    if dotx == 1127.6 and doty == 78.2:
        Datok = "170"
        return Datok
    if dotx == 1127.6 and doty == 132.0:
        Datok = "171"
        return Datok
    if dotx == 1127.6 and doty == 185.8:
        Datok = "172"
        return Datok
    if dotx == 1127.6 and doty == 239.6:
        Datok = "173"
        return Datok
    if dotx == 1127.6 and doty == 293.4:
        Datok = "174"
        return Datok
    if dotx == 1127.6 and doty == 347.2:
        Datok = "175"
        return Datok
    if dotx == 1095.0 and doty == -459.8:
        Datok = "176"
        return Datok
    if dotx == 1095.0 and doty == -406.0:
        Datok = "177"
        return Datok
    if dotx == 1095.0 and doty == -352.2:
        Datok = "178"
        return Datok
    if dotx == 1095.0 and doty == -298.4:
        Datok = "179"
        return Datok
    if dotx == 1095.0 and doty == -244.6:
        Datok = "180"
        return Datok
    if dotx == 1095.0 and doty == -190.8:
        Datok = "181"
        return Datok
    if dotx == 1095.0 and doty == -137.0:
        Datok = "182"
        return Datok
    if dotx == 1095.0 and doty == -83.2:
        Datok = "183"
        return Datok
    if dotx == 1095.0 and doty == -29.4:
        Datok = "184"
        return Datok
    if dotx == 1095.0 and doty == 24.4:
        Datok = "185"
        return Datok
    if dotx == 1095.0 and doty == 78.2:
        Datok = "186"
        return Datok
    if dotx == 1095.0 and doty == 132.0:
        Datok = "187"
        return Datok
    if dotx == 1095.0 and doty == 185.8:
        Datok = "188"
        return Datok
    if dotx == 1095.0 and doty == 239.6:
        Datok = "189"
        return Datok
    if dotx == 1095.0 and doty == 293.4:
        Datok = "190"
        return Datok
    if dotx == 1095.0 and doty == 347.2:
        Datok = "191"
        return Datok
    if dotx == 1062.4 and doty == -459.8:
        Datok = "192"
        return Datok
    if dotx == 1062.4 and doty == -406.0:
        Datok = "193"
        return Datok
    if dotx == 1062.4 and doty == -352.2:
        Datok = "194"
        return Datok
    if dotx == 1062.4 and doty == -298.4:
        Datok = "195"
        return Datok
    if dotx == 1062.4 and doty == -244.6:
        Datok = "196"
        return Datok
    if dotx == 1062.4 and doty == -190.8:
        Datok = "197"
        return Datok
    if dotx == 1062.4 and doty == -137.0:
        Datok = "198"
        return Datok
    if dotx == 1062.4 and doty == -83.2:
        Datok = "199"
        return Datok
    if dotx == 1062.4 and doty == -29.4:
        Datok = "200"
        return Datok
    if dotx == 1062.4 and doty == 24.4:
        Datok = "201"
        return Datok
    if dotx == 1062.4 and doty == 78.2:
        Datok = "202"
        return Datok
    if dotx == 1062.4 and doty == 132.0:
        Datok = "203"
        return Datok
    if dotx == 1062.4 and doty == 185.8:
        Datok = "204"
        return Datok
    if dotx == 1062.4 and doty == 239.6:
        Datok = "205"
        return Datok
    if dotx == 1062.4 and doty == 293.4:
        Datok = "206"
        return Datok
    if dotx == 1062.4 and doty == 347.2:
        Datok = "207"
        return Datok
    if dotx == 1029.8 and doty == -459.8:
        Datok = "208"
        return Datok
    if dotx == 1029.8 and doty == -406.0:
        Datok = "209"
        return Datok
    if dotx == 1029.8 and doty == -352.2:
        Datok = "210"
        return Datok
    if dotx == 1029.8 and doty == -298.4:
        Datok = "211"
        return Datok
    if dotx == 1029.8 and doty == -244.6:
        Datok = "212"
        return Datok
    if dotx == 1029.8 and doty == -190.8:
        Datok = "213"
        return Datok
    if dotx == 1029.8 and doty == -137.0:
        Datok = "214"
        return Datok
    if dotx == 1029.8 and doty == -83.2:
        Datok = "215"
        return Datok
    if dotx == 1029.8 and doty == -29.4:
        Datok = "216"
        return Datok
    if dotx == 1029.8 and doty == 24.4:
        Datok = "217"
        return Datok
    if dotx == 1029.8 and doty == 78.2:
        Datok = "218"
        return Datok
    if dotx == 1029.8 and doty == 132.0:
        Datok = "219"
        return Datok
    if dotx == 1029.8 and doty == 185.8:
        Datok = "220"
        return Datok
    if dotx == 1029.8 and doty == 239.6:
        Datok = "221"
        return Datok
    if dotx == 1029.8 and doty == 293.4:
        Datok = "222"
        return Datok
    if dotx == 1029.8 and doty == 347.2:
        Datok = "223"
        return Datok
    if dotx == 997.2 and doty == -459.8:
        Datok = "224"
        return Datok
    if dotx == 997.2 and doty == -406.0:
        Datok = "225"
        return Datok
    if dotx == 997.2 and doty == -352.2:
        Datok = "226"
        return Datok
    if dotx == 997.2 and doty == -298.4:
        Datok = "227"
        return Datok
    if dotx == 997.2 and doty == -244.6:
        Datok = "228"
        return Datok
    if dotx == 997.2 and doty == -190.8:
        Datok = "229"
        return Datok
    if dotx == 997.2 and doty == -137.0:
        Datok = "230"
        return Datok
    if dotx == 997.2 and doty == -83.2:
        Datok = "231"
        return Datok
    if dotx == 997.2 and doty == -29.4:
        Datok = "232"
        return Datok
    if dotx == 997.2 and doty == 24.4:
        Datok = "233"
        return Datok
    if dotx == 997.2 and doty == 78.2:
        Datok = "234"
        return Datok
    if dotx == 997.2 and doty == 132.0:
        Datok = "235"
        return Datok
    if dotx == 997.2 and doty == 185.8:
        Datok = "236"
        return Datok
    if dotx == 997.2 and doty == 239.6:
        Datok = "237"
        return Datok
    if dotx == 997.2 and doty == 293.4:
        Datok = "238"
        return Datok
    if dotx == 997.2 and doty == 347.2:
        Datok = "239"
        return Datok
    if dotx == 964.6 and doty == -459.8:
        Datok = "240"
        return Datok
    if dotx == 964.6 and doty == -406.0:
        Datok = "241"
        return Datok
    if dotx == 964.6 and doty == -352.2:
        Datok = "242"
        return Datok
    if dotx == 964.6 and doty == -298.4:
        Datok = "243"
        return Datok
    if dotx == 964.6 and doty == -244.6:
        Datok = "244"
        return Datok
    if dotx == 964.6 and doty == -190.8:
        Datok = "245"
        return Datok
    if dotx == 964.6 and doty == -137.0:
        Datok = "246"
        return Datok
    if dotx == 964.6 and doty == -83.2:
        Datok = "247"
        return Datok
    if dotx == 964.6 and doty == -29.4:
        Datok = "248"
        return Datok
    if dotx == 964.6 and doty == 24.4:
        Datok = "249"
        return Datok
    if dotx == 964.6 and doty == 78.2:
        Datok = "250"
        return Datok
    if dotx == 964.6 and doty == 132.0:
        Datok = "251"
        return Datok
    if dotx == 964.6 and doty == 185.8:
        Datok = "252"
        return Datok
    if dotx == 964.6 and doty == 239.6:
        Datok = "253"
        return Datok
    if dotx == 964.6 and doty == 293.4:
        Datok = "254"
        return Datok
    if dotx == 964.6 and doty == 347.2:
        Datok = "255"
        return Datok


def clasificacion(tamaño):
    if tamaño > 50 and tamaño <100:
        letter="G"
        return letter
        print("G")
    if tamaño >30 and tamaño < 49:
        letter = "M"
        return letter
    if tamaño >10 and tamaño < 29:
        letter = "P"
        return letter