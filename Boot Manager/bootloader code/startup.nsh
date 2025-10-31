echo =========================================
echo Pico Boot Bridge - EFI Shell
echo =========================================

echo Atualizando lista de volumes...
map -r

echo Procurando Pico (bootchoice.conf)...

cp fs0:\bootchoice.conf fs1:\EFI\refind\bootchoice.conf


# Executa rEFInd (testa fs0…fs5)

fs1:\EFI\refind\refind_x64.efi fs1:\EFI\refind\refind_x64.efi

pause

