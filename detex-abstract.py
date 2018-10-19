#!/usr/bin/env python3
from __future__ import print_function

import re

class Replacements:
    def __init__(self):
        self.subs = []

    def add(self, pattern, replacement):
        self.subs.append( (pattern, replacement) )

    def substitute(self, text):
        for (pattern, repl) in self.subs:
            text = re.sub(pattern, repl, text)
        return text

    def debug(self):
        for (pattern, repl) in self.subs:
            print(pattern, "->", repl)


math_repl = Replacements()
math_repl.add(r"""\times""", "x")

def detex(lines, repl):
    new_lines = []
    ## strip comments
    for (i, line) in enumerate(lines):
        if line.find("%") >= 0:
            idx = line.index("%")
            line = line[:idx] # note: removes newline, as intended
        new_lines.append(line)

    # note: now lines does not include newlines at end of each line
    lines = "".join(new_lines).split("\n")

    ## replace lines
    new_lines = []
    for line in lines:
        new_lines.append(repl.substitute(line))

    return "\n".join(new_lines)


def macro_re(macro_name, args=True):
    if args:
        return r"""\\""" + re.escape(macro_name) + r"""{(.*?)}"""
    else:
        return r"""\\""" + re.escape(macro_name)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("fname", help="Abstract LaTeX file")
    parser.add_argument("--rm-macro", nargs="*",
                        help="LaTeX \macros to remove entirely")
    parser.add_argument("--strip-macro", nargs="*",
                        help="LaTeX \macros to strip (replacing with their contents)")
    parser.add_argument("--sys", help="replace \sys macro with this text")

    args = parser.parse_args()

    repl = Replacements()

    if args.sys:
        repl.add(macro_re("sys", args=False), args.sys)

    if args.rm_macro:
        for macro in args.rm_macro:
            repl.add(macro_re(macro), "")
    if args.strip_macro:
        for macro in args.strip_macro:
            repl.add(macro_re(macro), r"""\1""")

    repl.add(macro_re("emph"), r"""_\1_""")
    repl.add(r"""$(.*?)$""", lambda m: math_repl.substitute(m.group(1)))

    with open(args.fname) as f:
        t = detex(f, repl)
        print(t, end="")
