#/usr/bin/env python
# -*- coding:utf-8 -*-

def check_login():
    u = raw_input("pls enter username:")
    p = raw_input("pls enter passwd:")
    ac = {}
    with open("D:/Python/mywork/%s.txt" % u, "r") as checktimes:
        login_times = int(checktimes.read())
        print "login_times:", login_times
        while int(login_times) == 2:
            print "you account is lock"
            exit(1)
        with open("D:/Python/mywork/account.txt", 'r') as account:
            for i in account:
                username = i.split(":")[0].strip()
                passwd = i.split(":")[1].strip()
                ac[username] = passwd

            if ac[u] == p:
                print "welcome"
            else:
                print "error username or passwd"
                login_times += 1
                with open("D:/Python/mywork/%s.txt" % u, "w") as lt:
                    lt.write(str(login_times))


if __name__ == "__main__":
    check_login()
