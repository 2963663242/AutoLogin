import pickle
def dictToNetscape(cookies,filename):
    fp = open(filename, "w")
    fp.write("# Netscape HTTP Cookie File\n")
    for cookie in cookies:
        fp.write(cookie.get("domain", "") + "\t")
        fp.write("TRUE\t")
        fp.write(cookie.get("path", "") + "\t")
        fp.write(str(cookie.get("secure", "")).upper() + "\t")
        fp.write(str(cookie.get("expiry", "0")) + "\t")
        fp.write(cookie.get("name", "") + "\t")
        fp.write(cookie.get("value", "") + "\n")

if __name__ == '__main__':
    filename = "C:/Users/Administrator/Desktop/cookies.txt"
    cookies = pickle.load(open('taobao_cookies.txt', 'rb'))
    dictToNetscape(cookies,filename)