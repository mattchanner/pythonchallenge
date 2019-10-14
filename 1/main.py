import string

table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

source = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle" \
        " qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

decoded = string.translate(source, table)

# print(decoded)

# i hope you didnt translate it by hand. thats what computers are for. 
# doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. 
# now apply on the url.

print(string.translate("map", table))

# ocr