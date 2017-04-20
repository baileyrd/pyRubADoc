@ECHO OFF
IF NOT "%~f0" == "~f0" GOTO :WinNT
@"C:\Users\BaileyRD\a\cmder\lang\ruby\bin\ruby.exe" "C:/Users/BaileyRD/Documents/GitHub/adoc/gemEnv/bin/asciidoctor" %1 %2 %3 %4 %5 %6 %7 %8 %9
GOTO :EOF
:WinNT
@"C:\Users\BaileyRD\a\cmder\lang\ruby\bin\ruby.exe" "%~dpn0" %*
