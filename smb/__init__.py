from fman import ApplicationCommand, show_quicksearch, show_prompt, QuicksearchItem
from .osascripthelper import OsascriptHelper

osascript = OsascriptHelper()
getMountsScript = '''
    tell application "Finder"
	    set volumeFolders to do shell script "ls /Volumes/"
	    set mountedVolumes to paragraphs of the volumeFolders
	    set diskList to the disks
	    set intersection to {}
	    repeat with a in diskList
		    set a to name of a
		    if a is not name of startup disk then
			    if {a} is in mountedVolumes then set end of intersection to a
		    end if
	    end repeat
	    return intersection
    end tell'''
mountScript = '''
    set server to "{0}"
    if server does not start with "smb://" then
	    set server to "smb://" & server
    end if
    tell application "Finder"
	    mount volume server
    end tell'''
unmountScript = '''
tell application "Finder"
   eject disk "{0}"
end tell'''

class MountSmbVolume(ApplicationCommand):
    def __call__(self):
        address, ok = show_prompt('Please enter the address of the server')
        if not address or not ok:
            return
        osascript.executeScript(mountScript.format(address))

class UnmountVolume(ApplicationCommand):
    def __call__(self):
        result = show_quicksearch(self._get_items)
        if result:
            query, value = result
            osascript.executeScript(unmountScript.format(value))
    def _get_items(self, query):
        result = osascript.executeScript(getMountsScript)
        for item in result:
            try:
                index = item.lower().index(query)
            except ValueError as not_found:
                continue
            else:
                highlight = range(index, index + len(query))
                yield QuicksearchItem(item, highlight=highlight)
