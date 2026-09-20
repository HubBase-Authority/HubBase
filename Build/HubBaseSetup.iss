// HubBase Installer
// Inno Setup 7

#define MyAppName = "HubBase"
#define MyAppVersion = "0.0.3.0.00b2.dev2"

[Setup]
AppName = {#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}_v{#MyAppVersion}
DefaultGroupName={#MyAppName}_v{#MyAppVersion}
AllowNoIcons=yes
OutputDir=exe
OutputBaseFilename={#MyAppName}_Setup
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
Source: "..\Programs\*"; DestDir: "{app}\Programs"; Components: core; Flags: ignoreversion
Source: "..\Docs\*"; DestDir: "{app}\Docs"; Components: core; Flags: ignoreversion
Source: "..\Data\*"; DestDir: "{app}\Data"; Components: core; Flags: ignoreversion
Source: "..\Changelog.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
