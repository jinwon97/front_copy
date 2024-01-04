from account.models import LogInfo
from rest_framework.response import Response
from datetime import datetime, timedelta

def LoginTrue(username):
    try:
        user_logInfo = LogInfo.objects.get(user_id__username = username)
        user_logInfo.isLogedIn = True
        user_logInfo.save()
        return True
    except:
        return False
    
def LoginFalse(username):
    try:
        user_logInfo = LogInfo.objects.get(user_id__username = username)
        user_logInfo.isLogedIn = False
        user_logInfo.save()
        return True
    except:
        return False
    
def LoginCheck(username):
    try:
        user_logInfo = LogInfo.objects.get(user_id__username = username)
        if user_logInfo.isLogedIn:
            if datetime.now() - user_logInfo.logtime > timedelta(hours = 1):
                user_logInfo.isLogedIn = False
                user_logInfo.save()
                return False
            else:
                user_logInfo.isLogedIn = True
                user_logInfo.save()
                return True
        else:
            return False
    except:
        return False