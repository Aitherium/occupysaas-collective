# bootstrap.ps1 -- chain the PUBLISHED installers for the OccupySaaS collective.
#
# Dry run by default: it prints the plan and runs NOTHING. Pass -Yes to
# execute. It never edits system configuration itself; every step is a
# published installer or an `adk` command.
param(
    [string]$Collective = 'occupysaas',
    [string[]]$Lane = @('embed'),
    [switch]$Yes,
    [switch]$SkipAwnix
)
$ErrorActionPreference = 'Stop'
$awnix = 'https://raw.githubusercontent.com/Aitherium/awnix/main/.DEPLOYMENT/standalone/bootc/install-awnix-wsl.ps1'
$laneArg = ($Lane -join ',')

$plan = @(
    "$(if ($SkipAwnix) { 'skip awnix (already installed)' } else { "install awnix: irm $awnix | iex" })",
    'adk login',
    "adk volunteer enroll --lane $laneArg --collective $Collective",
    "adk volunteer serve --lane $(if ($Lane -contains 'bonsai') { 'bonsai' } else { 'embed' })",
    'adk volunteer start --lane embed',
    'adk volunteer status'
)
Write-Host 'Plan:'
$i = 0
foreach ($step in $plan) { $i++; Write-Host ("  {0}. {1}" -f $i, $step) }

if (-not $Yes) {
    Write-Host ''
    Write-Host 'Dry run. Nothing has run. Pass -Yes to execute this plan.'
    exit 0
}

if (-not $SkipAwnix) {
    Write-Host 'Installing awnix...'
    irm $awnix | iex
}
if (-not (Get-Command adk -ErrorAction SilentlyContinue)) {
    throw 'adk is not on PATH. Install awdk (pip install awdk) and re-run.'
}
adk login
adk volunteer enroll --lane $laneArg --collective $Collective
adk volunteer serve --lane $(if ($Lane -contains 'bonsai') { 'bonsai' } else { 'embed' })
adk volunteer start --lane embed
adk volunteer status
