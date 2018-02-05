# coding=utf-8
import  pytest

def getips():
    ns=2
    with open("ips.txt") as f:
        ips=[]
        for i in f:
            ips.append((i.strip(),ns))
    return  ips
IPS=getips()
print IPS
@pytest.mark.parametrize("ip,ns",IPS)
def test_chckip(ip,ns):

    ips = ip.split(".")
    L = len(ips)
    print  ip,ns
    loop = 0
    if L == 4:
        for i in ips:
            if i.isdigit() and 0 <= int(i) <= 255:
                loop += 1
            else:
                break
    if loop == 4:
        ret = 1
    else:
        ret = 0
    assert ret == 1
