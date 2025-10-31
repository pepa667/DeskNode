# The Idea

In this project we are gonna use [https://www.rodsbooks.com/refind/](rEFInd) as a boot manager, but first, we will create a fake boot manager using the tool [https://github.com/tianocore/edk2/blob/UDK2018/ShellBinPkg/UefiShell/X64/Shell.efi](shell.efi) and renaming it to bootx64.efi and create another folder in the EFI volume you have installed rEFInd as if a new bootloader, there you will also have to copy the startup.nsh found here.
