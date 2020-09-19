try:
    import readline
except:
    readline = None
from pydoc import Helper
import code
import sys
import os
sys.path=[os.path.dirname(sys.executable)]+sys.path


class _helper(Helper):
    def __repr__(self):
        return "Type help() for interactive help, or help(object) for help about object."

    def __str__(self):
        return "Type help() for interactive help, or help(object) for help about object."

    def intro(self):
        print('''
Welcome to LitePython 's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/{0}/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
''')


help = _helper()


class License():
    lc = """MIT License

Copyright (c) 2020 Kavindu Santhusa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""".replace("\n", " ")
    def __init__(self): pass
    def __call__(self): return self.lc
    def __repr__(self): return "Type license() to see the full license text"


license = License()
copyright = "Copyright (c) 2020 Kavindu Santhusa"
credits = None
history = []
if readline:
    try:
        readline.read_history_file("litepython.history")
    except:
        pass


class LitePython(code.InteractiveConsole):
    def interact(self, banner=None):
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = ">>> "
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = "... "
        cprt = 'Type "help()", "copyright", "credits" or "license" for more information.'
        if banner is None:
            self.write("Python %s on %s\n%s\n(%s)\n" %
                       (sys.version, sys.platform, cprt,
                        self.__class__.__name__))
        elif banner:
            self.write("%s\n" % str(banner))
        more = 0
        while 1:
            try:
                if more:
                    prompt = sys.ps2
                else:
                    prompt = sys.ps1
                try:
                    line = self.raw_input(prompt)
                except EOFError:
                    self.write("\n")
                    break
                else:
                    more = self.push(line)
            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0
        if readline:
            try:
                readline.write_history_file("litepython.history")
            except:
                pass


console = LitePython({"__name__": "<stdin>", "help": help, "license": license,
                      "copyright": copyright, "credits": credits}, filename="<stdin>")
if len(sys.argv) > 1:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("""LightPython 1.0.0
usage: {} [option] ... [-c cmd | -m mod | file | -] [arg] ...""".format(sys.argv[0]))
        sys.exit(0)
    elif sys.argv[1] == "-c" or sys.argv[1] == "--compile":
        if len(sys.argv) > 2:
            console.runcode(sys.argv[2])
        else:
            print("""Argument expected for the -c option
usage: {0} [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `{0} -h' for more information.""".format(sys.argv[0]))
        sys.exit(0)
    else:
        if sys.argv[1] == "-m":
            if len(sys.argv) > 2:
                _file = os.path.join(os.path.dirname(
                    sys.executable), sys.argv[2])
            else:
                print("""Argument expected for the -m option
usage: {0} [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `{0} -h' for more information.""".format(sys.argv[0]))
                sys.exit(0)
        else:
            _file = sys.argv[2]
        import runpy

        def runner(code="", l={}):
            console.locals.update(l)
            console.runcode(code)
        runpy.exec = runner
        runpy.run_path(_file, {"__name__": "__main__", "help": help, "license": license,
                               "copyright": copyright, "credits": credits}, "__main__")
        sys.exit(0)
bannar = """LitePython 1.0.0
Type "help", "copyright", "credits" or "license" for more information."""
console.interact(bannar)
