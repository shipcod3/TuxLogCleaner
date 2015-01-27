###########################
# tux_logcleaner.py       #
# @shipcod3               #
#                         #
# greets to ROOTCON goons #
###########################

import os, sys, time

print """
 _____                _                     _____  _                                 
|_   _|              | |                   /  __ \| |                                
  | |   _   _ __  __ | |      ___    __ _  | /  \/| |  ___   __ _  _ __    ___  _ __ 
  | |  | | | |\ \/ / | |     / _ \  / _` | | |    | | / _ \ / _` || '_ \  / _ \| '__|
  | |  | |_| | >  <  | |____| (_) || (_| | | \__/\| ||  __/| (_| || | | ||  __/| |   
  \_/   \__,_|/_/\_\ \_____/ \___/  \__, |  \____/|_| \___| \__,_||_| |_| \___||_|   
                                     __/ |                                           
by @shipcod3                        |___/  -- a simple log cleaner for linux                                          
"""

def tux():
    logs = ["/var/log/lastlog", 
            "/var/log/messages", 
            "/var/log/warn", 
            "/var/log/wtmp", 
            "/var/log/poplog", 
            "/var/log/qmail", 
            "/var/log/smtpd", 
            "/var/log/telnetd", 
            "/var/log/secure", 
            "/var/log/auth", 
            "/var/log/auth.log", 
            "/var/log/cups/access_log", 
            "/var/log/cups/error_log", 
            "/var/log/thttpd_log", 
            "/var/log/spooler", 
            "/var/spool/tmp", 
            "/var/spool/errors", 
            "/var/spool/locks", 
            "/var/log/nctfpd.errs", 
            "/var/log/acct", 
            "/var/apache/log", 
            "/var/apache/logs", 
            "/usr/local/apache/log", 
            "/usr/local/apache/logs", 
            "/usr/local/www/logs/thttpd_log", 
            "/var/log/news", 
            "/var/log/news/news", 
            "/var/log/news.all", 
            "/var/log/news/news.all", 
            "/var/log/news/news.crit", 
            "/var/log/news/news.err", 
            "/var/log/news/news.notice", 
            "/var/log/news/suck.err", 
            "/var/log/news/suck.notice", 
            "/var/log/xferlog", 
            "/var/log/proftpd/xferlog.legacy", 
            "/var/log/proftpd.xferlog", 
            "/var/log/proftpd.access_log", 
            "/var/log/httpd/error_log", 
            "/var/log/httpsd/ssl_log", 
            "/var/log/httpsd/ssl.access_log", 
            "/var/adm", 
            "/var/run/utmp", 
            "/etc/wtmp", 
            "/etc/utmp", 
            "/etc/mail/access", 
            "/var/log/mail/info.log", 
            "/var/log/mail/errors.log", 
            "/var/log/httpd/*_log", 
            "/var/log/ncftpd/misclog.txt", 
            "/var/account/pacct", 
            "/var/log/snort", 
            "/var/log/bandwidth", 
            "/var/log/explanations", 
            "/var/log/syslog", 
            "/var/log/user.log", 
            "/var/log/daemons/info.log", 
            "/var/log/daemons/warnings.log", 
            "/var/log/daemons/errors.log", 
            "/etc/httpd/logs/error_log", 
            "/etc/httpd/logs/*_log", 
            "/var/log/mysqld/mysqld.log"
            "/root/.ksh_history", 
            "/root/.bash_history", 
            "/root/.sh_history", 
            "/root/.history", 
            "/root/*_history", 
            "/root/.login", 
            "/root/.logout", 
            "/root/.bash_logut", 
            "/root/.Xauthority"]

    print "Are you sure you want to clear your logs and shell histories?"
    answer = raw_input("y/n: ")
    
    if answer.lower() == 'y':
        
        for log in logs:
            if os.path.isfile(log):
                print "[***] Cleaning " +log
                os.remove(log)
                print "[+] Done cleaning.."
    
        time.sleep(1)
        print "\n[***] Done sweeping \m/"

    else:
        print "MMmkay!"
        sys.exit()
    
if __name__ == "__main__":
    if not os.geteuid() == 0:
        sys.exit("Please run this script as root")

    else:
        tux()
