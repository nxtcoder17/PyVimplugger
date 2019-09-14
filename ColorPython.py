################################################################# 
# #               Module Instructions                         # #
# ################################################################
# Class Variables:                                              #
#       bold        : Text followed is printed in BOLD          #
#       dim         : Text followed is printed in dim colors    #
#       bg          : background color for the text followed    #
#       invert      : inverts background color with text color  #
#       underline   : Text Followed in underlined               #
#       dashed      : Text Followed is dashed (strikedthrough)  #
#                                                               #
# How to Use :                                                  #
# ************                                                  #
#       Just import this module/class file                      #
#       Issue it like.                                          #
#           Color.bold['green'] + <text follows> + Color.reset  #
#       this statement, makes text look GREEN and BOLDER        #
#################################################################

class Color:
    bold = {
            'black'  : '\033[01;30m',
            'red'    : '\033[01;31m',
            'green'  : '\033[01;32m',
            'yellow' : '\033[01;33m',
            'blue'   : '\033[01;34m',
            'purple' : '\033[01;35m',
            'cyan'   : '\033[01;36m',
            'white'  : '\033[01;37m'
            };

    normal = {
            'black'  : '\033[00;30m',
            'red'    : '\033[00;31m',
            'green'  : '\033[00;32m',
            'yellow' : '\033[00;33m',
            'blue'   : '\033[00;34m',
            'purple' : '\033[00;35m',
            'cyan'   : '\033[00;36m',
            'white'  : '\033[00;37m'
            };

    dim = {
            'black'  : '\033[02;30m',
            'red'    : '\033[02;31m',
            'green'  : '\033[02;32m',
            'yellow' : '\033[02;33m',
            'blue'   : '\033[02;34m',
            'purple' : '\033[02;35m',
            'cyan'   : '\033[02;36m',
            'white'  : '\033[02;37m'
            };

    bg = {
            'black'  : '\033[02;40m',
            'red'    : '\033[02;41m',
            'green'  : '\033[02;42m',
            'yellow' : '\033[02;43m',
            'blue'   : '\033[02;44m',
            'purple' : '\033[02;45m',
            'cyan'   : '\033[02;46m',
            'white'  : '\033[02;47m'
            };


    italic = {
            'black'  : '\033[03;31m',
            'red'    : '\033[03;31m',
            'green'  : '\033[03;32m',
            'yellow' : '\033[03;33m',
            'blue'   : '\033[03;34m',
            'purple' : '\033[03;35m',
            'cyan'   : '\033[03;36m',
            'white'  : '\033[03;37m'
            };
    # Inverts background Color with the Text Color
    invert = {
            'black'  : '\033[04;40m',
            'red'    : '\033[04;41m',
            'green'  : '\033[04;42m',
            'yellow' : '\033[04;43m',
            'blue'   : '\033[04;44m',
            'purple' : '\033[04;45m',
            'cyan'   : '\033[04;46m',
            'white'  : '\033[04;47m'
            };

    underline = {
            'black'  : '\033[04;30m',
            'red'    : '\033[04;31m',
            'green'  : '\033[04;32m',
            'yellow' : '\033[04;33m',
            'blue'   : '\033[04;34m',
            'purple' : '\033[04;35m',
            'cyan'   : '\033[04;36m',
            'white'  : '\033[04;37m'
            };

    dashed = {
            'black'  : '\033[09;40m',
            'red'    : '\033[09;41m',
            'green'  : '\033[09;42m',
            'yellow' : '\033[09;43m',
            'blue'   : '\033[09;44m',
            'purple' : '\033[09;45m',
            'cyan'   : '\033[09;46m',
            'white'  : '\033[09;47m'
            };

    neutral = "\033[00m"
    reset = neutral

    def __init__(self):
        pass

# Added on Sat 29 Jun 2019 07:20:49 PM IST
attr_call_map = {
    'bold': lambda color, text: Color.bold [color] + text + Color.neutral,
    'normal': lambda color, text: Color.normal [color] + text + Color.neutral,
    'italic': lambda color, text: Color.italic [color] + text + Color.neutral,
    'dim': lambda color, text: Color.dim [color] + text + Color.neutral,
    'bg': lambda color, text: Color.bg [color] + text + Color.neutral,
    'invert': lambda color, text: Color.invert [color] + text + Color.neutral,
    'underline': lambda color, text: Color.underline [color] + text + Color.neutral,
    'dashed': lambda color, text: Color.dashed [color] + text + Color.neutral,
}

def pprint (color, attr, text):
    if attr in attr_call_map:
        return attr_call_map [attr] (color, text)
    else:
        return text
