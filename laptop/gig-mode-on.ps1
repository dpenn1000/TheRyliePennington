#Requires -RunAsAdministrator
# Gig mode for the Ableton show laptop (Lenovo Yoga C940-15).
# Closes background apps, pauses indexing/updates, and switches to a no-throttle power plan.
# Nothing here is permanent: run gig-mode-off.ps1 or reboot to undo.

Write-Host "Closing background apps..."
$apps = 'HD-Player','BlueStacks*','Grammarly*','MuseHub','ms-teams','Teams','Microsoft.Lists',
        'PhoneExperienceHost','CrossDeviceService','logioptionsplus*','OneDrive','OneDrive.Sync.Service'
foreach ($a in $apps) { Get-Process $a -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue }

Write-Host "Pausing search indexing, prefetch, telemetry and Windows Update for this session..."
foreach ($s in 'WSearch','SysMain','DiagTrack','wuauserv','UsoSvc','MuseAuthService') {
    Stop-Service $s -Force -ErrorAction SilentlyContinue
}

Write-Host "Setting up the 'Gig Mode' power plan..."
$existing = powercfg /list | Select-String 'Gig Mode'
if ($existing) {
    $guid = ([regex]'[0-9a-f-]{36}').Match($existing.Line).Value
} else {
    # Ultimate Performance; fall back to High Performance if this edition hides it
    $out = powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 2>$null
    if (-not $out) { $out = powercfg /duplicatescheme 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c }
    $guid = ([regex]'[0-9a-f-]{36}').Match("$out").Value
    powercfg /changename $guid 'Gig Mode' 'Ableton live show: no throttling, no sleep, no USB suspend'
}
powercfg /setacvalueindex $guid SUB_PROCESSOR PROCTHROTTLEMIN 100
powercfg /setacvalueindex $guid SUB_PROCESSOR PROCTHROTTLEMAX 100
powercfg /setacvalueindex $guid 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0  # USB selective suspend off
powercfg /setacvalueindex $guid SUB_PCIEXPRESS ASPM 0                                                          # PCIe power saving off
powercfg /setacvalueindex $guid SUB_SLEEP STANDBYIDLE 0
powercfg /setacvalueindex $guid SUB_SLEEP HIBERNATEIDLE 0
powercfg /setacvalueindex $guid SUB_VIDEO VIDEOIDLE 0
powercfg /setactive $guid

Write-Host ""
Write-Host "Gig mode on. Still do by hand:" -ForegroundColor Green
Write-Host "  - Lenovo Vantage > Power: set Intelligent Cooling to Extreme Performance"
Write-Host "  - Do Not Disturb on (Win+N, bell icon)"
Write-Host "  - Bluetooth off unless something on stage needs it"
Write-Host "  - Close Chrome and Claude before opening Ableton"
