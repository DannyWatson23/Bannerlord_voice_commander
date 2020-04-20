# Bannerlord_voice_commander
Simple Python project to control troops via voice
I've compiled it with PyInstaller to ensure the dependencies are included in the executable to remove the need for you to download any crap, faff, etc. If you have Python3 with the dependencies, feel free just to download the source code and run via that.

Executable location (~40MB too big for Github however has all dependencies included for ease - hosted on my OneDrive): 
https://1drv.ms/u/s!AnUMrIQNnHORgZkenIYTH9pFjdfu2Q?e=I05Sol

Please check the source-code for transparency and peace of mind.

Tested only on my Windows 10

How to use:
 - "exit" to exit the program
 - "follow"
 - "hold","position","wait" - hold position
 - "charge", "attack" - charge
 - "advance", "forward", "go" - forward
 - "fall", "back", "return" - return
 - "stop", "halt" - stop
 - "run", "retreat", "run motherfuckers", "gold please" - retreat
 - "face", "meet" - face enemy
 - "look" - face direction
 - "line", "single" - form line
 - "shield", "wall" - form shield wall
 - "loose", "spread" - spread out
 - "circle" - form circle
 - "square" - form square
 - "skein", "arrow", "screen" - form skein
 - "column", "rank" - form column
 - "fire at" - hold fire/fire at will
 - "mounty", "horses" - dismount and mount
 - "simon", "lars" - delegate control
 
 - "everybody", "guys", "soldiers" - select all troops
 - "1" - infantry
 ...
 ...
 - "8" - heavy_cavalry
 

To run: 
- Download the .exe file
- Virus scan the file
- Compare SHA1/MD5/SHA-256 hash
- Open cmd
- voice1.exe
 - Your anti-virus might check it over, this is fine, once it confirms the program is safe, it will reassign control to the main CMD window
- The program stores your voice commands in a local file in the same directory "out.log" (If you have a strong accent like myself you may need to adapt the source code to accomodate for your needs.)


Hash checksum:

C:\Users\Danny\dist>certUtil -hashfile voice1.exe
SHA1 hash of voice1.exe:
bb24c95dbe33e0f3c900439f1d8c51fca4881c47
CertUtil: -hashfile command completed successfully.

MD5 Hash (generated on onlinemd5):
6318875E9E6533A2E4A9401A4B0DA306

SHA-256 Hash (generated on onlinemd5):
06FC963AB8785D10062023BEE739518FA296B29A5F011B3258CD22DE2A0492AC

