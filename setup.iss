[Setup]
AppName=Tavaram
AppVersion=1.0
DefaultDirName={pf}\Tavaram
DefaultGroupName=Tavaram
UninstallDisplayIcon={app}\tavaram.exe
OutputDir=userdocs:Inno Setup Examples Output

[Files]
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\dist\tavaram.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\aae.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\abe.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\ace.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\ade.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\bae.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\bbe.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\bce.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\bde.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\labels.txt"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\keras_model.h5"; DestDir: "{app}"; Flags: recursesubdirs
Source: "C:\Users\SHANKARA\PycharmProjects\pythonProject\Latha (1).ttf"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{commondesktop}\Tavaram"; Filename: "{app}\tavaram.exe"; WorkingDir: "{app}"
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Tavaram"; Filename: "{app}\tavaram.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\tavaram.exe"; Description: "{cm:LaunchProgram,Tavaram}"; Flags: nowait postinstall skipifsilent
