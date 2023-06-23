#!/usr/bin/env python3

import sys

l0_count = l1_count = l2_count = l3_count = l4_count = 0
indent_string = ""
output_string = ""
div_str = ") "

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
            indent_string = str(l0_count) + ".0"
            l1_count = l2_count = l3_count = l4_count = 0
    elif t == 1:
        if line.startswith("\t: "):
            indent_string = "\t"
            notab_line = line.replace("\t: ", "")
        else:
            if last_level == t:
                l1_count += 1
            indent_string = "\t" + str(l0_count) + "." + str(l1_count)
            l2_count = l3_count = l4_count = 0
    elif t == 2:
        if line.startswith("\t\t: "):
            indent_string = "\t\t"
            notab_line = line.replace("\t\t: ", "")
        else:
            if last_level == t:
                l2_count += 1
            indent_string = "\t\t" + str(l0_count) + "." + str(l1_count) + "." + str(l2_count)
            l3_count = l4_count = 0
    elif t == 3:
        if line.startswith("\t\t\t: "):
            indent_string = "\t\t\t"
            notab_line = line.replace("\t\t\t: ", "")
        else:
            if last_level == t:
                l3_count += 1
            indent_string = "\t\t\t" + str(l0_count) + "." + str(l1_count) + "." + str(l2_count) + "." + str(l3_count)
            l4_count = 0
    elif t == 4:
        if line.startswith("\t\t\t\t: "):
            indent_string = "\t\t\t\t"
            notab_line = line.replace("\t\t\t\t: ", "")
        else:
            if last_level == t:
                l4_count += 1
            indent_string = "\t\t\t\t" + str(l0_count) + "." + str(l1_count) + "." + str(l2_count) + "." + str(l3_count) + "." + str(l4_count)

    output_string = indent_string + notab_line
    print(output_string , end="")
