#define MyAppName "Falcon"
#define MyAppVersion "1.0"
#define MyAppPublisher "YourPublisherName"
#define MyAppURL "http://www.yourwebsite.com/"
#define MyAppExeName "main.exe"
#define MyIconPath "C:\Users\HP i5\PycharmProjects\Falcon\falcon.ico"

[Setup]
AppId={{YOUR-GUID-HERE}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputBaseFilename=Setup_{#MyAppName}_{#MyAppVersion}
SetupIconFile={#MyIconPath}
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\HP i5\PycharmProjects\Falcon\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
; Add other files and directories you want to include in the installation

[Dirs]
Name: "{userappdata}\Falcon\logs"; Permissions: everyone-modify
Name: "{userappdata}\Falcon\images"; Permissions: everyone-modify
Name: "{userappdata}\Falcon\files"; Permissions: everyone-modify

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Registry]
Root: HKCU; Subkey: "Software\{#MyAppName}"; Flags: uninsdeletekey
