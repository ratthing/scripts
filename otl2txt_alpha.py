#!/usr/bin/env python3

import sys

L0 = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVII", "XVIII", "XIX", "XX")
L1 = ("\tA", "\tB", "\tC", "\tD", "\tE", "\tF", "\tG", "\tH", "\tI", "\tJ", "\tK", "\tL", "\tM", "\tN", "\tO", "\tP", "\tQ", "\tR", "\tS", "\tT")
L2 = ("\t\t 1", "\t\t 2", "\t\t 3", "\t\t 4", "\t\t 5", "\t\t 6", "\t\t 7", "\t\t 8", "\t\t 9", "\t\t10", "\t\t11", "\t\t12", "\t\t13", "\t\t14", "\t\t15", "\t\t16", "\t\t17", "\t\t18", "\t\t19", "\t\t20")
L3 = ("\t\t\ta", "\t\t\tb", "\t\t\tc", "\t\t\td", "\t\t\te", "\t\t\tf", "\t\t\tg", "\t\t\th", "\t\t\ti", "\t\t\tj", "\t\t\tk", "\t\t\tl", "\t\t\tm", "\t\t\tn", "\t\t\to", "\t\t\tp", "\t\t\tq", "\t\t\tr", "\t\t\ts", "\t\t\tt")
L4 = ("\t\t\t\t    i", "\t\t\t\t   ii", "\t\t\t\t  iii", "\t\t\t\t   iv", "\t\t\t\t    v", "\t\t\t\t   vi", "\t\t\t\t  vii", "\t\t\t\t viii", "\t\t\t\t   ix", "\t\t\t\t    x", "\t\t\t\t   xi", "\t\t\t\t  xii", "\t\t\t\t xiii", "\t\t\t\t  xiv", "\t\t\t\t   xv", "\t\t\t\t xvii", "\t\t\t\txviii", "\t\t\t\t  xix", "\t\t\t\t   xx")

l0_count = l1_count = l2_count = l3_count = l4_count = 0
indent_string = ""
notab_line = ""
div_str=". "

for line in sys.stdin:
    t = line.count("\t")
    notab_line = div_str + line.replace("\t", "")
    if t == 0:
        if line.startswith(": "):
            indent_string = ""
            notab_line = line.replace(": ", "")
        else:
            indent_string = L0[l0_count]
            l0_count += 1
            l1_count = l2_count = l3_count = l4_count = 0
    elif t == 1:
        if line.startswith("\t: "):
            indent_string = "\t"
            notab_line = line.replace("\t: ", "")
        else:
            indent_string = L1[l1_count]
            l1_count += 1
            l2_count = l3_count = l4_count = 0
    elif t == 2:
        if line.startswith("\t\t: "):
            indent_string = "\t\t"
            notab_line = line.replace("\t\t: ", "")
        else:
            indent_string = L2[l2_count]
            l2_count += 1
            l3_count = l4_count = 0
    elif t == 3:
        if line.startswith("\t\t\t: "):
            indent_string = "\t\t\t"
            notab_line = line.replace("\t\t\t: ", "")
        else:
            indent_string = L3[l3_count]
            l3_count += 1
            l4_count = 0
    elif t == 4:
        if line.startswith("\t\t\t\t: "):
            indent_string = "\t\t\t\t"
            notab_line = line.replace("\t\t\t\t: ", "")
        else:
            indent_string = L4[l4_count]
            l4_count += 1

    output_string = indent_string + notab_line
    print(output_string , end="")
