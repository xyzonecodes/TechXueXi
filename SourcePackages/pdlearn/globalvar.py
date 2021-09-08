##是否是无界面模式，一般用在命令行，docker上
#from pdlearn.utils.pluspush import PlusPushHandler
#from pdlearn.utils.fangtang import FangtangHandler
#from pdlearn.utils.dingding import DingDingHandler
from pdlearn.utils.sendNotify import sendNotify

pushmode ="1"
nohead = False
accesstoken = ""
secret=""
islooplogin=False
db=None
##推送或者显示
def pushprint(text):
#     print(accesstoken,secret)
#     if nohead==True:
     notify=sendNotify()
     print(text)
     # if pushmode=="1":
     #      s=1
     #      # push=DingDingHandler(accesstoken,secret)
     #      # push.ddtextsend(text)
     # elif pushmode=="3":
     #      push=FangtangHandler(accesstoken)
     #      push.fttext(text)
     # elif pushmode=="4":
     #      push=PlusPushHandler(accesstoken)
     #      push.fttext(text)