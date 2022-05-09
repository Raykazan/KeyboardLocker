## KeyboardLocker

A linux tool to disable and re-enable the default keyboard.

This tool will lock the keyboard as you need.

The need to clean my keyboard led me to this solution. Hope this can help someone in any way.

### For Now...

For now it has been tested on my Kubuntu machine.

```markdown

    The .desktop file has the Exec line commented, so you need to put the path and uncomment the line yourself.
    # The .desktop file
    [Desktop Entry]
    Comment=
    #Exec=/path/to/program/KeyboardLocker/klock.py
    GenericName=Bloqueador de teclado
    Icon=yast-keyboard
    Categories=Utilities; Tools;
    Name=KeyboardLocker
    NoDisplay=false
    Path[$e]=
    StartupNotify=true
    Terminal=0
    TerminalOptions=
    Type=Application
    
´´´
    

Any help and improvements are welcome!
