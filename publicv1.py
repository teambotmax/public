'''
Simple Public Bots Fixed by Ressync™♪

Sᴘᴇcɪᴀʟ Tʜᴀɴᴋs Tᴏ :
- Ibal™♪
- Uwewww™♪
- Yhzkl Bagas

Tʜᴀɴᴋs Tᴏ :
- Darma™♪
- Pebb™♪
- IGoy™♪
- Agungnur.y™♪

Sᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ :
 • MiBots™♪
 • NoiBots™♪
 • Release™♪
 • SentinelCorps™♪
 • LeadershipCorps™♪
 • HigherBrotherTeam™♪
 • ExecllentsTeamBots™♪
 • and All of My Friends :)
 
©2020 By MPC♪

'''
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from MPCBots.thrift.protocol import TCompactProtocol
from MPCBots.thrift.transport import THttpClient
from MPCBots.ttypes import LoginRequest
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from zalgo import zalgoname
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, pytz, sys, pafy, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, platform, ctypes, sys, ast, re, os, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
etb = LINE('email','password')
#=======================================================
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp1.json","r","utf-8")
tokenOpen = codecs.open("toket.json","r","utf-8")
premiumOpen = codecs.open("user.json","r","utf-8")
#=====================================================================
#=====================================================================
etbProfile = etb.getProfile()
etbSettings = etb.getSettings()
etbPoll = OEPoll(etb)
etbMID = etb.getProfile().mid
#=====================================================================
#=====================================================================
loop = asyncio.get_event_loop()
admin =["u6664f570c2145d3dcab19d0bf0dfc15e"]
myAdmin = ["u6664f570c2145d3dcab19d0bf0dfc15e"]
botStart = time.time()
msg_dict = {}
temp_flood = {}
groupName = {}
groupImage = {}
kuciyose = {}
protectname = []
wbanlist = []
steals = []
protectinvite = []
protectkick = []
protectjoin = []
protectqr = []
protectantijs = []
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
token = json.load(tokenOpen)
premium = json.load(premiumOpen)
responsename = etb.getProfile().displayName
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

kimak= {
    "Addaudio": False,
    "Audio": {},
    "Audios": {
     },
}

hoho = {
    "savefile": False,
    "namefile": "",
}

bro = {
    "reader": True,
}

check = {
    "checkcontact": False,
}

itil = {
    "blacklist": {},
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}
#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = etbProfile.displayName
settings["myProfile"]["statusMessage"] = etbProfile.statusMessage
settings["myProfile"]["pictureStatus"] = etbProfile.pictureStatus
cont = etb.getContact(etbMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = etb.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open('setting.json', 'r') as fp:
    setup2 = json.load(fp)
with open("temp1.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

def sendTemplate(to, data):
    allow_liff()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = etb.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def allow_liff():
	url = 'https://access.line.me/dialog/api/permissions'
	data = {
	    'on': [
	        'P',
	        'CM'
	    ],
	    'off': []
	}
	headers = {
	    'X-Line-Access': etb.authToken,
	    'X-Line-Application': etb.server.APP_NAME,
	    'X-Line-ChannelId': '1602687308',
	    'Content-Type': 'application/json'
	}
	requests.post(url, json=data, headers=headers)
def inSteals(from_):
    global steals
    if from_ in steals:
        return True
    return False
def appendSteals(from_):
    try:
        global steals
        if from_ in steals:
            return
        return steals.append(from_)
    except:
        return False
def clearSteals():
    global steals
    steals = []
    return
def bcTemplate(gr, data):
    allow_liff()
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = etb.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendTemplate(group, data):
    allow_liff()
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = etb.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d d %02d h %02d m %02d s' % (days, hours, mins, secs)

def debug():
    get_profile_time_start = time.time()
    get_profile = etb.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = etb.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = etb.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    etb.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    etb.sendMessage(to, '', annda, 13)

def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            etb.sendMessage(to, text, {'MSG_SENDER_NAME': etb.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + etb.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            etb.sendMessage(to, text, {'MSG_SENDER_NAME': etb.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + etb.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Mpcorpss  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    etb.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(etb.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + etb.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = etb.genOBSParams({'oid': etbMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = etb.server.postContent('{}/talk/vp/upload.nhn'.format(str(etb.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        etb.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("KhieWasHere.mp4")
    
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = etb.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        etb.sendMessage(to, textx, {'MSG_SENDER_NAME': etb.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + etb.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
def logError(text):
    etb.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('temp1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = etb.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def videoyt(to,text):
    link = pafy.new(text)
    v=link.streams
    for a in v:
          mp4=a.url
    data={
       'type': 'video',
       'originalContentUrl': mp4,
       'previewImageUrl': "https://i.ibb.co/P4J49rr/yyhhh1.jpg"
}
    sendTemplate(to, data)
#=====================================================================
async def etbBot(op):
    try:
        if settings["restartPoint"] != None:
            etb.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            etb.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if etb.getProfile().mid in op.param3:
                G = etb.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    etb.acceptGroupInvitation(op.param1)
                    etb.sendMention(op.param1,"Hi @!, thanks for inviting me in this group ^_^\n\nType `Help` to see all commands !!\n\nIf there are bug in commands, please type `Chatmaker` or contact creator on link bellow :\nContact : https://lin.ee/K5ZxCaS\n\nType `@leave` for leave bots >_<","",[op.param2])

        if op.type == 19 or op.type == 133:
            if op.param3 == "uac9e750cc79a6dee9c23157b9d8a9890":
                myGroup = 'c5d69ae9fbda3d02ad3068be16c6b9284'
                nameGroup = etb.getGroup(op.param1).name
                jam = pytz.timezone("Asia/Jakarta")
                jamSek = datetime.now(tz=jam)
                jamm = datetime.strftime(jamSek, '%d-%m-%Y')
                jammm = datetime.strftime(jamSek,'%H:%M:%S')
                contact = etb.getContact(mid)
                kiker = etb.getContact(op.param2)
                res = "┏━━━━━"
                res += "\n┣ NOTIFICATION KICK"
                res += "\n┣ In Group: {}".format(nameGroup)
                res += "\n┣ Date: {}".format(jamm)
                res += "\n┣ Time: {}".format(jammm)
                res += "\n┣ Victim : {}".format(contact.displayName)
                res += "\n┣ Kicker: {}".format(kiker.displayName)
                res += "\n┗━━━━━━━"
                etb.sendMessage(myGroup, res)
                etb.sendContact(myGroup, op.param2)

        if op.type == 55:
            if cctv['cyduk'][op.param1] == True:
                if op.param1 in cctv['point']:
                    Name = etb.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n " + Name
                        mpcorps={'previewUrl': "http://dl.profile.line-cdn.net/"+etb.getContact(op.param2).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': 'You can join chat?', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': etb.getContact(op.param2).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+op.param2,'MSG_SENDER_NAME':  etb.getContact(op.param2).displayName,}
                        etb.sendMessage(op.param1, etb.getContact(op.param2).displayName, mpcorps, 19)
            if cctv['cyduk'][op.param1] == True:
                if op.param1 in cctv['point']:
                    Name = etb.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = etb.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        etb.sendImageWithURL(op.param1, image)

        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message               
            text = msg.text
            msg_id = msg.id
            receiver = msg.to             
            sender = msg._from
            s = etb.getProfile().mid
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
               setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:                    	
                    if sender != etb.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if sender != s:
                	        peler["receivercount"] += 1
                        if sender == s:
                	        peler["sendcount"] += 1

#=====================================================================
        if op.type == 26:
            if msg.contentType == 13:
                if check["checkcontact"] == True:
                    msg.contentType = 0
                    etb.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = etb.getContact(msg.contentMetadata["mid"])
                        path = etb.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        etb.sendMessage(msg.to," 「 Contact Info 」\nMid User : " + msg.contentMetadata["mid"] + "\nName : " + msg.contentMetadata["displayName"] + "\nStatus : " + contact.statusMessage + "\nPict URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        etb.sendImageWithURL(msg.to, image)
                        check["checkcontact"] = False
#==========================================
        if op.type == 26:
            if msg.contentType == 16:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                if settings["getpost"] == True:
                    try:
                        b = msg.contentMetadata["mediaType"]
                        c = msg.contentMetadata["mediaOid"].split("|")[1]
                        d = msg.contentMetadata["mediaOid"].split("|")[2]
                        if b == "V":
                            etb.sendMessage(to,"Downloading♪")
                            etb.sendVideoWithURL(to,"https://obs-us.line-apps.com/myhome/{}/download.nhn?{}".format(c.replace("sid=",""),d))
                            settings["getpost"] = False
                            etb.sendMessage(to,"Done! ")
                        else:
                             etb.sendMessage(to,"Video Gblk Bukan Gambar")
                    except Exception as e:
                        etb.sendMessage(to,str(e))
#==========================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != etbMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = etb.getContact(sender)
                        if msg.toType == 2:
                            anu = etb.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        etb.sendMessage(to, str(e))
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != etbMID: to = sender
                else: to = receiver
                if msg.contentType == 14:
                    if hoho["savefile"] == True:
                        try:
                             namafile = hoho["namafile"]
                             etb.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             etb.sendMessage(to, "Successful, the file has been uploaded")
                        except Exception as e:
                         	etb.sendMessage(to, str(e))
                if msg.contentType == 1: 
                    if settings["changeCoverProfile"] == True:
                        path = etb.downloadObjectMsg(msg_id)
                        settings["changeCoverProfile"] = False
                        etb.updateProfileCover(path)
                        etb.sendMessage(to,"Cover Image Updated.")                                           
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            etb.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            etb.sendChatChecked(to, msg_id)
                    if "/youtu.be" in msg.text.lower():
                        regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                        links = re.findall(regex, text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)     
                            for mmk in n_links:
                                videoyt(to,mmk)
#==========================================
#==========================================
#==========================================
                    elif cmd.startswith("exec\n"):
                        if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            try:
                                sep = text.split("\n")
                                search = text.replace(sep[0] + "\n","")
                                exec(search)
                            except Exception as error:
                                etb.sendMessage(msg.to,"  「 !! ERROR !! 」\n{}".format(error))
                    elif text.lower() == 'ginfo':
                        group = etb.getGroup(to)
                        try:
                            gCreator = group.creator.displayName
                        except:
                            gCreator = "Not Found"
                        if group.invitee is None:
                            gPending = "0"
                        else:
                            gPending = str(len(group.invitee))
                        if group.preventedJoinByTicket == True:
                            gQr = "Closed"
                            gTicket = "Not Found"
                        else:
                            gQr = "Open"
                            gTicket = "https://etb.me/R/ti/g/{}".format(str(etb.reissueGroupTicket(group.id)))
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ret_ = "[ Group Info ]"
                        ret_ += "\nName Group : {}".format(str(group.name))
                        ret_ += "\nID Group : {}".format(group.id)
                        ret_ += "\nCreator : {}".format(str(gCreator))
                        ret_ += "\nTotal Member : {}".format(str(len(group.members)))
                        ret_ += "\nTotal Pending : {}".format(gPending)
                        ret_ += "\nGroup QR : {}".format(gQr)
                        ret_ += "\nGroup Ticket : {}".format(gTicket)
                        etb.sendReplyMessage(msg.id, to, str(ret_))
                        etb.sendImageWithURL(to, path)
                    elif cmd.startswith("github "):
                        users = removeCmd("github", text)
                        path = requests.get('https://api.github.com/users/{}'.format(users))
                        data = path.text
                        data = json.loads(data)
                        data = {
                            "type": "template",
                            "altText": "information",
                            "template": {
                                "type": "buttons",
                                "thumbnailImageUrl": "{}".format(str(data["avatar_url"])),
                                "imageSize": "contain",
                                "imageAspectRatio": "square",
                                "title": '{}'.format(str(data["name"])),
                                "text": 'Followers: {}\nFollowing: {}\nRepositories: {}'.format(str(data["followers"]), (data["following"]), (data["public_repos"])),
                                "actions": [{
                                    "type": "uri",
                                    "label": "Repositories",
                                    "uri": "https://github.com/{}?tab=repositories".format(str(users))
                                },
                                {
                                    "type": "uri",
                                    "label": "Go Page",
                                    "uri": "https://github.com/{}".format(str(users))
                                }]
                            }
                        }
                        sendTemplate(to, data)
#==========================================
#==========================================
                    elif cmd == "timeleft":
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        etb.sendReplyMessage(msg.id, to, "「 Runtime 」\n"+str(runtime))                        
                    elif cmd == "clearchat" and sender == admin:
                        etb.removeAllMessages(op.param1)
                        etb.generateReplyMessage(msg.id)
                        etb.sendReplyMessage(msg.id, to, "Success♪")                        
#==========================================    
                    elif cmd == "help":
                        ret = "         Type : Public\n        Version : 1.0.0\n     Developer : MPC™\n      Copyright©2020\n       「 Help Menu 」\n\n"   
                        ret += "  • Checkmid <mid>\n"
                        ret += "  • Github <user>\n"
                        ret += "  • Checkcontact\n"
                        ret += "  • Reader on/off\n"
                        ret += "  • Mid <@>\n"
                        ret += "  • Timeleft\n"
                        ret += "  • Getpost\n"
                        ret += "  • Debug\n"
                        ret += "  • Tagall\n"
                        ret += "  • About\n"
                        ret += "  • Ginfo\n"
                        ret += "  • Ping\n"
                        ret += "  • Me\n"
                        ret += "  • Mid\n"
                        ret += "  • @leave"                        
                        hello = "{}".format(str(ret))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret)),
                            "sentBy": {
                                "label": "𝕸𝖊𝖗𝖕𝖆𝖙𝖎𝕻𝖚𝖙𝖎𝖍𝕮𝖔𝖗𝖕𝖘™",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(etb.getContact(etbMID).pictureStatus),
                                "linkUrl": "https://lin.ee/K5ZxCaS"
                                }
                            }
                        sendTemplate(to, data)
#==========================================
                    elif cmd == "reader on":
                        if bro["reader"] == True:
                            try:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                etb.sendMessage(msg.to, "Get reader activated\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                del cctv['point'][msg.to]
                                del cctv['sidermem'][msg.to]
                                del cctv['cyduk'][msg.to]
                            except:
                                pass
                            cctv['point'][msg.to] = msg.id
                            cctv['sidermem'][msg.to] = ""
                            cctv['cyduk'][msg.to]=True

                    elif cmd == "reader off":
                        if bro["reader"] == True:
                            if msg.to in cctv['point']:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cctv['cyduk'][msg.to]=False
                                etb.sendMessage(msg.to, "Get reader deactivated\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                            else:
                                etb.sendMessage(msg.to, "Has been deactivated >_<")
#=========================================
#==========================================
#==========================================
                    elif cmd.startswith("#leave "):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            number = removeCmd("#leave", text)
                            groups = etb.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = etb.getGroup(group)
                                try:
                                    etb.leaveGroup(G.id)
                                except:
                                    etb.leaveGroup(G.id)
                                etb.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                etb.sendMessage(to, str(error))
#==========================================
                    if cmd == "chatmaker":
                        etb.sendMention(msg.to, 'Hello @! if u want chat my creator\nType : Chatmaker [text]\nExample : Chatmaker Hi etby',' ', [msg._from])
                    elif cmd.startswith("chatmaker "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contact = etb.getContact(sender)
                        owner = "u6664f570c2145d3dcab19d0bf0dfc15e"
                        mat_ = "Sender: @!"
                        mat_ += "\nMessage: {}".format(txt)
                        mat = {
                            'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus,
                            'MSG_SENDER_NAME':  contact.displayName,
                            'mid': sender,
                        }
                        mid = etb.getContact(sender).displayName
                        mentions(owner, mat_, [sender])
                        etb.sendMessage(owner, mid, contentMetadata=mat, contentType=13)
                        etb.sendMention(to, "Hi @!\nYour message has been send ^_^","",[msg._from])
#==========================================
#==========================================
#==========================================
                    elif cmd.startswith("name "):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            string = removeCmd("name", text)
                            if len(string) <= 10000000000:
                                pname = etb.getContact(sender).displayName
                                profile = etb.getProfile()
                                profile.displayName = string
                                etb.updateProfile(profile)
                                etb.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("status "):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            string = removeCmd("status", text)
                            if len(string) <= 10000000000:
                                pname = etb.getContact(sender).statusMessage
                                profile = etb.getProfile()
                                profile.statusMessage = string
                                etb.updateProfile(profile)
                                etb.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
#==========================================
                    elif cmd == "mid":
                        etb.generateReplyMessage(msg.id)
                        etb.sendReplyMessage(msg.id, to, "「 Mid 」\n "+str(sender))
#==========================================
                    elif cmd == "ping":
                        etb.sendMention(to, "PONG ! @!","",[msg._from])
#==========================================
#==========================================
#==========================================
#==========================================
                    elif cmd == "screenlist":
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            proses = os.popen("screen -list")
                            a = proses.read()
                            etb.sendReplyMessage(msg.id, to, "{}\n 𝐌𝐄𝐑𝐏𝐀𝐓𝐈 𝐏𝐔𝐓𝐈𝐇 𝐂𝐎𝐑𝐏𝐒♪ ".format(str(a)))
                            proses.close()
                    elif cmd == "autojoin on":
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            etb.sendMessage(to, msgs)
                    elif cmd == "autojoin off":
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            etb.sendMessage(to, msgs)
#==========================================
                    elif cmd == "getpost":
                        if settings["getpost"] == True:
                            msgs=" 「 Get Post 」\nGetpost already Enable♪"
                        else:
                            msgs=" 「 Get Post 」\nShare timeline videos♪"
                            settings["getpost"] = True
                        etb.sendReplyMessage(msg.id, to, msgs)
                    elif cmd == "checkcontact":
                        if check["checkcontact"] == True:
                            msgs=" 「 Contact Info 」\nGet contact already Enable♪"
                        else:
                            msgs=" 「 Contact Info 」\nPlease share contact♪"
                            check["checkcontact"] = True
                        etb.sendReplyMessage(msg.id, to, msgs)
#==========================================
                    elif text.lower() == "reboot":
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            etb.sendMention(to, "@! Success rebooting",' ', [msg._from])
                            restartBot()
                        else:pass
#==========================================
                    elif cmd == "tagall":
                        group = etb.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(etb.getProfile().mid)
                        etb.datamention(to,'Mention',nama)
                    elif cmd== '@leave':
                        etb.leaveGroup(to)
#==========================================
                    elif cmd == "me":
                        hoax = etb.getContact(msg._from).mid
                        etb.sendContact(msg.to,hoax)
#==========================================
                    elif cmd.startswith("#replychat "):
                        if sender == "u6664f570c2145d3dcab19d0bf0dfc15e":
                            try:
                                sep = text.replace("#replychat ","")
                                bctxt = text.split(" ")
                                dan = bctxt[1]
                                anu = bctxt[2]
                                ret_ = "「 Incoming Message 」"
                                ret_ += "\n From : Admin"
                                ret_ += "\n To : @!"
                                ret_ += "\n Message : {}".format(anu)
                                ret_ += "\n\nPlease type chatmaker <message>\nto reply ^_^"
                                etb.sendMention("{}" .format(dan), str(ret_),"", [dan])
                                etb.sendReplyMessage(msg.id,to, "success")
                            except Exception as e:
                                etb.sendMessage(to, str(e))
                    elif cmd.startswith("#chat "):
                    	if sender == "u6664f570c2145d3dcab19d0bf0dfc15e":
                            sep = text.replace("#chat ","")
                            bctxt = text.split(" ")
                            dan = bctxt[1]
                            anu = bctxt[2]
                            gr = etb.getGroupIdsJoined()
                            try:
                                pesan = gr[int(dan)-1]
                                group = etb.getGroup(pesan)
                                etb.sendMessage(pesan, "{}".format(str(anu)))
                                etb.sendMessage(to, "Success sent message to group : {}".format(group.name))
                            except Exception as anu:
                                etb.sendMessage(to, str(anu))
                    elif cmd.startswith("mid "):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            ret_ = "「 Mid User 」"
                            for ls in lists:
                                ret_ += "\n{}".format(str(ls))
                            etb.generateReplyMessage(msg.id)
                            etb.sendReplyMessage(msg.id, to, str(ret_))                                
                    elif cmd.startswith("skill "):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = etb.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = etb.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return etb.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               etb.kickoutFromGroup(msg.to,[target])
                    elif cmd.startswith("slain "):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = etb.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = etb.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return etb.sendMessage(to,"not found name "+midn)
                           for target in targets:
                               etb.kickoutFromGroup(msg.to,[target])
                               etb.findAndAddContactsByMid(target)
                               etb.inviteIntoGroup(msg.to, [target])
                               etb.cancelGroupInvitation(msg.to, [target])
                               time.sleep(5)
                               etb.inviteIntoGroup(msg.to, [target])
#==========================================
                    elif cmd== 'check':
                        if sender in ["u6664f570c2145d3dcab19d0bf0dfc15e"] and msg.toType == 2:
                            try:
                                etb.sendMention(to, "Hadir komandan @!","",[sender])
                            except:pass
                        else:
                            etb.sendMention(to, "Sokap lu ajg @!","",[kontol])
#==========================================
                    elif cmd.startswith("cvp"):
                        if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            link = removeCmd("helper:cvp", text)
                            contact = etb.getContact(sender)
                            etb.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = etb.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            etb.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Success")
                            os.remove("TeamAnuBot.mp4")                            
#==========================================
#==========================================
#==========================================
                    elif cmd == "about":
                        try:
                            arr = []
                            today = datetime.today()
                            thn = 2018 
                            bln = 8    #isi bulannya yg sewa
                            hr = 9   #isi tanggalnya yg sewa
                            future = datetime(thn, bln, hr)
                            days = (str(future - today))
                            comma = days.find(",")
                            days = days[:comma]
                            h = etb.getContact(etbMID)
                            groups = etb.getGroupIdsJoined()
                            contactlist = etb.getAllContactIds()
                            oampc = "u7659c7f3e951565c262c93eea9582d3c"
                            kontak = etb.getContacts(contactlist)
                            favorite = etb.getFavoriteMids()
                            fil = etb.getSettings().privacyReceiveMessagesFromNotFriend
                            seal = etb.getSettings().e2eeEnable
                            blockedlist = etb.getBlockedContactIds()
                            src = etb.getSettings().privacySearchByUserid
                            python_imp = platform.python_implementation()
                            python_ver = platform.python_version()
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            fakesp = '567'
                            sp = "".join([random.choice(fakesp) for x in range(5)])
                            hsl = "0.00" + sp
                            kontak2 = etb.getContacts(blockedlist)
                            status = {"kick": "", "invite": ""}
                            try:etb.kickoutFromGroup(to, [etbMID]);status["kick"] = "Normal"
                            except:status["kick"] = "Limit"
                            try:etb.inviteIntoGroup(to, [etbMID]);status["invite"] = "Normal"
                            except:status["invite"] = "Limit"
                            if src == True:alid = "Allow add by LineID : [✔] Allowed"
                            else:alid = "Allow add by LineID : [❌] Not Allowed"                            
                            if seal == True:letsel = "Letter Sealing : [✔] Allowed"
                            if seal == False:letsel = "Letter Sealing : [❌] Not Allowed"
                            if fil == True:fpes = "Filter Message : [❌] Not Allowed"
                            if fil == False:fpes = "Filter Message : [✔] Allowed"
                            ret_ = "> About :"
                            ret_ += "\nBot name : {}".format(h.displayName)
                            ret_ += "\nRuntime : {}".format(runtime)
                            ret_ += "\nResponse : {}".format(hsl)
                            ret_ += "\nGroup : {}".format(str(len(groups)))
                            ret_ += "\nFriend : {}".format(str(len(kontak)))
                            ret_ += "\nFavorite: {}".format(str(len(favorite)))
                            ret_ += "\nBlocked : {}".format(str(len(kontak2)))
                            ret_ += "\nChat send : {}".format(str(peler["sendcount"]))
                            ret_ += "\nChat received : {}".format(str(peler["receivercount"]))
                            ret_ += "\n{}".format(alid)
                            ret_ += "\n{}".format(letsel)
                            ret_ += "\n{}".format(fpes)
                            ret_ += "\nKick : %s" % status["kick"]
                            ret_ += "\nInvite : %s" % status["invite"]
                            ret_ += "\n\n> System : \nLanguage : {}".format(python_imp)
                            ret_ += "\nVersion : {}".format(python_ver)
                            ret_ += "\n\n> Other Info :\nBot Type : Public"
                            ret_ += "\nBot Version : v1.0"
                            ret_ += "\nDeveloped by : \n"
                            ret_ += " • @!                  "
                            mentions(to, str(ret_),[oampc])
                        except Exception as e:
                            etb.sendMessage(to, str(e))
#==========================================
                    if msg.text.lower() == "clear:admin":
                      if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                        if msg.toType == 2:
                            if setup2["admin"] == {}:etb.sendReplyMessage(msg.id, msg.to,"Admin list not found.")
                            else:
                                setup2["admin"] = {}
                                with open('setting.json', 'w') as fp:
                                    json.dump(setup2, fp, sort_keys=True, indent=4)                               
                                etb.sendReplyMessage(msg.id,msg.to,"Admin list cleared.")
                                
                    if msg.text.lower().startswith("add:admin "):
                      if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                         if 'MENTION' in msg.contentMetadata.keys() != None:
                             names = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                 if mention['M'] in wait["blacklist"]:
                                     etb.sendMessage(msg.to," User in blacklist.")
                                 elif mention['M'] in setup2["admin"]:
                                     etb.sendMessage(msg.to," User already in admin list.")
                                 else:
                                     if mention['M'] not in wait["blacklist"] and mention['M'] not in setup2["admin"]:
                                         setup2["admin"][mention['M']] = True
                                         with open('setting.json', 'w') as fp:
                                           json.dump(setup2, fp, sort_keys=True, indent=4)
                                         etb.sendMessage(msg.to,etb.getContact(mention['M']).displayName +" added in admin list.")
                                    
                    if msg.text.lower().startswith("del:admin "):
                      if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in setup2["admin"]:etb.sendReplyMessage(msg.id,msg.to, "User not in admin list.")
                            else:
                                try:
                                    del setup2["admin"][target]
                                    with open('setting.json', 'w') as fp:
                                        json.dump(setup2, fp, sort_keys=True, indent=4)
                                    etb.sendReplyMessage(msg.id,msg.to,etb.getContact(target).displayName +" removed from admin list.")
                                except:pass                                    

                    if msg.text.lower() == "list:admin":
                      if msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                       if msg.toType == 2:
                          ang = setup2["admin"]
                          if ang == {}:etb.sendMessage(msg.to," 「 Admin Access 」\nUser is empty!!")
                          else:
                             num = 1
                             enak = "Type : Admin Access\n\n"
                             for a in ang:
                                entot = etb.getContact(a).displayName
                                enak += "{}. {}\n".format(num,entot)
                                num = (num+1)
                             enak += "---------------------------------------\nTotal user : {} ".format(len(setup2["admin"]))                          
                             etb.generateReplyMessage(msg.id)                     
                             etb.sendReplyMessage(msg.id,msg.to,enak)
#==========================================
                    elif cmd == "debug":
                        etb.sendReplyMessage(msg.id, to, debug())
#==========================================
                    elif cmd.startswith('#inviteme '):
                       if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                             cond = cmd.split(" ")
                             num = int(cond[1])
                             gid = etb.getGroupIdsJoined()
                             group = etb.getCompactGroup(gid[num-1])
                             etb.findAndAddContactsByMid(sender)
                             etb.inviteIntoGroup(gid[num-1],[sender])                
                             etb.sendMessage(msg.to,"Success inviting you admin ^_^")
                    elif cmd.startswith("checkmid "):
                        sep = text.split(" ")
                        thempc = text.replace(sep[0] + " ","")
                        merpatiputih = etb.getContact(thempc).mid
                        etb.sendContact(msg.to,merpatiputih)
#==========================================
                    elif cmd == "#glist":
                       if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = etb.getGroupIdsJoined()
                            sd = etb.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal groups : {} \n────────────────────\n1. #chat / <num> / <text>\n2. #inviteme <num>\n3. #openqr <num>\n4. #leave <num>\n".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} ({})".format(no, G.name[0:50], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                etb.generateReplyMessage(msg.id)
                                etb.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith("bcast"):
                        if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            sep = text.split(" ")
                            psn = text.replace(sep[0] + " ","")
                            targets = etb.getGroupIdsJoined()
                            g = etb.getGroup(to)
                            for target in targets:
                                try:
                                    etb.sendMention(target,f"{psn}\n────────────────────\nBroadcast by : @!","",[sender])
                                except TalkException:
                                    targets.remove(target)
                                    time.sleep(0.8)
                            etb.sendMessage(to,f"Success Broadcast to : {len(etb.getGroupIdsJoined())} Groups")
                    elif cmd.startswith("#openqr "):
                        if msg._from in setup2["admin"] or msg._from in "u6664f570c2145d3dcab19d0bf0dfc15e":
                            number = removeCmd("#openqr", text)
                            groups = etb.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = etb.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    etb.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(etb.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    etb.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(etb.reissueGroupTicket(G.id)))
                                etb.sendMessage(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                etb.sendMessage(to, str(error))
#==========================================
#=======================================
        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = etbPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(etbBot(op))
                   #etbBot(op)
                   etbPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()