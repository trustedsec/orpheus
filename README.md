# Orpheus
![Orpheus](orpheus.png?raw=true)

Orpheus is a wrapper for a modified version of Impacket's GetUserSPNs.py and kerberosv5.py which alters the KDC Options (Ticket Options) and the Encryption Type for Kerberoasting. 

Side Note: Orpheus is named after the Greek god that was able to get past Cerberus (the three headed dog) to get into Hades.

# Installation / Running

You will need to install the latest version of [Impacket](https://github.com/SecureAuthCorp/impacket). This was tested on the [0.10.0 release](https://github.com/SecureAuthCorp/impacket/releases/tag/impacket_0_10_0). Then

```
git clone https://github.com/trustedsec/orpheus.git
cd orpheus
python3 orpheus.py
```

# Commands
Type help for a listing of commands. To change the KDC options, enter the number of the option and press enter.
```
Commands:
    0 to 31                       Toggles the specific KDC Option flag.
    hex <value>                   Sets KDC Options from a hexadecimal value.
    cred <value>                  Sets the GetUserSPNs.py credential parameter.
    dcip <value>                  Sets the GetUserSPNs.py domain IP parameter.
    file <value>                  Sets the GetUserSPNs.py filename parameter.
    enc                           Toggles the encryption type from 23 (RC4) to 18 (AES-256).
    command                       Show the GetUserSPNs.py command with specified options.
    run                           Runs GetUserSPNs.py with the selected options.
    clear                         Clears the screen and displays the options.
    exit                          Exits the script.
```

# Video
Check out the video on [YouTube](https://www.youtube.com/watch?v=SwbSq1dTz7Y)

# Blog Post
Check out the blog post on [TrustedSec](https://www.trustedsec.com/blog/the-art-of-bypassing-kerberoast-detections-with-orpheus/)
