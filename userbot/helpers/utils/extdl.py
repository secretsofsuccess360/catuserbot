import datetime
from subprocess import PIPE, Popen

from telethon.tl.tlobject import TLObject
from telethon.tl.types import MessageEntityMentionName, MessageEntityPre
from telethon.utils import add_surrogate

from ...Config import Config
from ...utils import edit_delete

def install_pip(pipfile):
    process = Popen(["pip", "install", f"{pipfile}"], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
