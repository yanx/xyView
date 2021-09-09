import os
import sys
import wx

_platformNames = ["wxMSW", "wxGTK", "wxMac"]


_importList = ["wx.aui", "wx.calendar", "wx.html", "wx.media", "wx.wizard",
               "wx.combo", "wx.animate", "wx.gizmos", "wx.glcanvas", "wx.grid",
               "wx.richtext", "wx.stc"]

_dirWX = dir(wx)
for mod in _importList:
    try:
        module = __import__(mod)
    except ImportError:
        continue


#---------------------------------------------------------------------------

def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.join(*tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st


def GetDataDir():
    """
    Return the standard location on this platform for application data
    """
    sp = wx.StandardPaths.Get()
    return sp.GetUserDataDir()


def GetModifiedDirectory():
    """
    Returns the directory where modified versions of the demo files
    are stored
    """
    return os.path.join(GetDataDir(), "modified")


def GetModifiedFilename(name):
    """
    Returns the filename of the modified version of the specified demo
    """
    if not name.endswith(".py"):
        name = name + ".py"
    return os.path.join(GetModifiedDirectory(), name)


def GetOriginalFilename(name):
    """
    Returns the filename of the original version of the specified demo
    """
    if not name.endswith(".py"):
        name = name + ".py"

    if os.path.isfile(name):
        return name

    originalDir = os.getcwd()
    listDir = os.listdir(originalDir)
    # Loop over the content of the demo directory
    for item in listDir:
        if not os.path.isdir(item):
            # Not a directory, continue
            continue
        dirFile = os.listdir(item)
        # See if a file called "name" is there
        if name in dirFile:
            return os.path.join(item, name)

    # We must return a string...
    return ""


def DoesModifiedExist(name):
    """Returns whether the specified demo has a modified copy"""
    if os.path.exists(GetModifiedFilename(name)):
        return True
    else:
        return False


def GetConfig():
    if not os.path.exists(GetDataDir()):
        os.makedirs(GetDataDir())

    config = wx.FileConfig(
        localFilename=os.path.join(GetDataDir(), "options"))
    return config


def MakeDocDirs():

    docDir = os.path.join(GetDataDir(), "docs")
    if not os.path.exists(docDir):
        os.makedirs(docDir)

    for plat in _platformNames:
        imageDir = os.path.join(docDir, "images", plat)
        if not os.path.exists(imageDir):
            os.makedirs(imageDir)


def GetDocFile():

    docFile = os.path.join(GetDataDir(), "docs", "TrunkDocs.pkl")

    return docFile


def GetDocImagesDir():

    MakeDocDirs()
    return os.path.join(GetDataDir(), "docs", "images")


def SearchDemo(name, keyword):
    """ Returns whether a demo contains the search keyword or not. """
    fid = open(GetOriginalFilename(name), "rt")
    fullText = fid.read()
    fid.close()

    fullText = fullText.decode("iso-8859-1")

    if fullText.find(keyword) >= 0:
        return True

    return False

