#!/usr/bin/env python3

import sys

l0_count = l1_count = l2_count = l3_count = 0
indent_string = ""
output_string = ""
div_str = ""
start_code = "\\documentclass[11pt]{article}\n\\usepackage{outlines}\n\\begin{document}\n\\begin{outline}"
end_code = "\\end{outline}\n\\end{document}"

print(start_code)

for line in sys.stdin:
    t = line.count("\t")
    last_level = t
    notab_line = div_str + line.replace("\t", "")
    if t == 0:
        if line.startswith(": "):
            indent_string = ""
            notab_line = line.replace(": ", "")
        else:
            if last_level == t:
                l0_count += 1
            indent_string = "\\1[" + str(l0_count) + ".0]"
            l1_count = l2_count = l3_count = 0
    elif t == 1:
        if line.startswith("\t: "):
            indent_string = ""
            notab_line = line.replace("\t: ", "")
        else:
            if last_level == t:
                l1_count += 1
            indent_string = "\\2[" + str(l0_count) + "." + str(l1_count) + "]"
            l2_count = l3_count = 0
    elif t == 2:
        if line.startswith("\t\t: "):
            indent_string = ""
            notab_line = line.replace("\t\t: ", "")
        else:
            if last_level == t:
                l2_count += 1
            indent_string = "\\3[" + str(l0_count) + "." + str(l1_count) + "." + str(l2_count) + "]"
            l3_count = 0
    elif t == 3:
        if line.startswith("\t\t\t: "):
            indent_string = ""
            notab_line = line.replace("\t\t\t: ", "")
        else:
            if last_level == t:
                l3_count += 1
            indent_string = "\\4[" + str(l0_count) + "." + str(l1_count) + "." + str(l2_count) + "." + str(l3_count) + "]"
    
    output_string = indent_string + notab_line
    print(output_string , end="")

print(end_code)
