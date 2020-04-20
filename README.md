# Bannerlord_voice_commander
Simple Python project to control troops via voice
I've compiled it with PyInstaller to ensure the dependencies are included in the executable to remove the need for you to download any crap, faff, etc. If you have Python3 with the dependencies, feel free just to download the source code and run via that.

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
- The program stores your voice commands in a local file in the same directory "out.log" (If you have a strong accent like myself you may need to adapt the source code to accomodate for your needs.


Hash checksum:
C:\Users\Danny\dist>certUtil -hashfile voice1.exe
SHA1 hash of voice1.exe:
f3c84c7cb3faf560f2cbb70aceee4db04b1cb028
CertUtil: -hashfile command completed successfully.

MD5 Hash (generated on onlinemd5):
7A54AB9D480487984B2325123C1CF9B3

SHA-256 Hash (generated on onlinemd5):
6F7D142196456684FFF42A03A3DABB870B30F0CD8BE71141F87319B5C0C03597

