// HubBase Installer
// Inno Setup 7

#define MyAppName = "HubBase"
#define MyAppVersion = "0.0.3.0.00rc1"
#define MyAppSecureVersion = "0_0_3_0_00rc1"

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
Name: "Test_suite"; Description: "Test/* - Beta test suite"; Types: full custom
Name: "Extras"; Description: "Test/legacy/*, .gitignore"; Types: full custom

[Files]
Source: "..\__main__.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\__init__.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\Database.py"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\requirements.txt"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\LICENSE"; DestDir: "{app}"; Components: core; Flags: ignoreversion
Source: "..\Programs\*"; DestDir: "{app}\Programs"; Components: core; Flags: ignoreversion recursesubdirs; Excludes: "__pycache__\*";
Source: "..\Docs\*"; DestDir: "{app}\Docs"; Components: Documentation; Flags: ignoreversion; Excludes: "__pycache__\*";
Source: "..\Data\*"; DestDir: "{app}\Data"; Components: Documentation; Flags: ignoreversion; Excludes: "__pycache__\*";
Source: "..\Changelog.py"; DestDir: "{app}"; Components: Documentation; Flags: ignoreversion
Source: "..\Test\*"; DestDir: "{app}\Test"; Components: Test_suite; Flags: ignoreversion recursesubdirs; Excludes: "legacy\*, __pycache__\*";
Source: "..\Test\legacy\*"; DestDir: "{app}\Test\legacy"; Components: Extras; Flags: ignoreversion; Excludes: "__pycache__\*";
Source: "..\.gitignore"; DestDir: "{app}"; Components: Extras; Flags: ignoreversion
