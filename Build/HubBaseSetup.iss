// HubBase Installer
// Inno Setup 7

#define MyAppName = "HubBase"
#define MyAppVersion = "0.0.3.0.00b3"
#define MyAppSecureVersion = "0_0_3_0_00b3"

[Setup]
AppName = {#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}_v{#MyAppSecureVersion}
DefaultGroupName={#MyAppName}_v{#MyAppSecureVersion}
AllowNoIcons=yes
OutputDir=exe
OutputBaseFilename={#MyAppName}_v{#MyAppVersion}_Setup
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=admin
DisableDirPage=no
DisableProgramGroupPage=yes
ArchitecturesInstallIn64BitMode=x64compatible
UninstallDisplayName=Uninstall_{#MyAppName}_v{#MyAppVersion}
ChangesAssociations=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Components]
Name: "core"; Description: "LICENSE, requirements.txt, __main__.py, __init__.py, Database.py and Programs/*"; Types: full compact custom; Flags: fixed
Name: "Documentation"; Description: "Docs/*, Data/*, Changelog.py"; Types: full custom
Name: "Extras"; Description: "Test/*, .gitignore"; Types: full custom

[Files]
Source: "..\__main__.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\__init__.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\Database.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\requirements.txt"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\Programs\*"; DestDir: "{app}\Programs"; Components: core; Flags: ignoreversion recursesubdirs
Source: "..\Docs\*"; DestDir: "{app}\Docs"; Components: Documentation; Flags: ignoreversion
Source: "..\Data\*"; DestDir: "{app}\Data"; Components: Documentation; Flags: ignoreversion
Source: "..\Changelog.py"; DestDir: "{app}"; Components: Documentation; Flags: ignoreversion
Source: "..\Test\*"; DestDir: "{app}\Test"; Components: Extras; Flags: ignoreversion
Source: "..\.gitignore"; DestDir: "{app}"; Components: Extras; Flags: ignoreversion
