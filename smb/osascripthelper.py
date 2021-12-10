from typing import List
from fman import show_alert, OK
from subprocess import Popen, PIPE
import shutil

osascript = "/usr/bin/osascript"

class OsascriptHelper:
    def executeScript(self, script):
        if self._check_osascript():
            p = Popen(['osascript'], stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='utf8')
            stdout, stderr = p.communicate(script)
            result = self._parse_result(stdout)
            return result

    def _parse_result(self, scriptOutput) -> List:
        result = scriptOutput.split(', ')
        for i in range(len(result)):
            result[i] = result[i].rstrip("\n")
        return result

    def _check_osascript(self):
        check = shutil.which(osascript) is not None
        if (check):
            return True
        self._handle_osascript_not_found()
        return False

    def _handle_osascript_not_found(self):
      print('Osascript not found')
      show_alert(
            'Osascript was not found',
            OK, OK
        )
