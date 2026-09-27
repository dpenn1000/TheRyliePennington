#Requires -RunAsAdministrator
# Undo gig-mode-on.ps1. A reboot does the same thing, except for the power plan.

powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e   # Balanced
foreach ($s in 'WSearch','SysMain','DiagTrack','wuauserv','UsoSvc','MuseAuthService','LenovoVantageService') {
    Start-Service $s -ErrorAction SilentlyContinue
}
$od = "$env:LOCALAPPDATA\Microsoft\OneDrive\OneDrive.exe"
if (-not (Test-Path $od)) { $od = "$env:ProgramFiles\Microsoft OneDrive\OneDrive.exe" }
if (Test-Path $od) { Start-Process $od -ArgumentList '/background' }
Write-Host "Back to normal. Balanced power plan, services and OneDrive restarted." -ForegroundColor Green
