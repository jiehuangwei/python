import sublime, sublime_plugin
import time

class TestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # 1430539200
        # 1430539200
        for sel in self.view.sel():
            t = float(self.view.substr(sel))
            try:
                self.view.replace(edit, sel, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))
            except:
                pass
