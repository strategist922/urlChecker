#=================================bunch of necessary Libraries=============================================
import os, sys, urllib3, base64, json, subprocess, requests
from time import gmtime, strftime
# =========================================================================================================

# ==========Slack Tokens and stuff=========================================================================
SLACK_INCOMING_WEB_HOOK = "https://hooks.slack.com/services/xxxxxxx/xxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxx"
SLACK_INCOMING_USER = "somename"  # Slack Bot display name
SLACK_INCOMING_CHANNEL = "#channelor@user"  # Slack Channel
http = urllib3.PoolManager()
# =========================================================================================================

# ====== log file configuration ===========================================================================
logname = 'health'
logfile_name = logname + ".log"
# =========================================================================================================

# ==========Just calling uptimes with auths and messages for slack payload if down=========================
def checkUptimes():
    checkLogic("https://someurl1.check","lol:wut","some url 1")
    checkLogic("https://someurl2.check","bruh:wut","some url 2")
    checkLogic("https://someurl3.check","likeReally:wut","some url 3")

# =========================================================================================================

# ==========Basically constructing a call and deciding if to send a slack message==========================
def checkLogic(url,auth,message):
    try:
        headers = urllib3.util.make_headers(basic_auth=auth)
        r = http.request('GET', url, headers=headers)
        if(r.status != 200):
            payload = {"text": message +" is down", "username": SLACK_INCOMING_USER, "channel": SLACK_INCOMING_CHANNEL, "icon_emoji": ":bangbang:"}
            r= requests.post(SLACK_INCOMING_WEB_HOOK, json.dumps(payload), headers={'content-type': 'application/json'})
    except IOError as e:
        log("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        log("Could not convert data to an integer.")
    except:
        log("Unexpected error:" + str(sys.exc_info()[0]))
        raise    
# =========================================================================================================

# ====================Generic Log Stuff====================================================================
def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + str(message))
# =========================================================================================================

# =====================The Actual Driver===================================================================
if __name__ == "__main__":
    checkUptimes()
    log("I was ran")
# =========================================================================================================