#!/usr/bin/env bash
# bootstrap.sh -- chain the PUBLISHED installers for the OccupySaaS collective.
#
# Dry run by default: prints the plan and runs NOTHING. Pass --yes to
# execute. Every step is a published installer or an `adk` command.
set -euo pipefail

COLLECTIVE='occupysaas'
LANE='embed,bonsai'
RELAY_CHANNEL='#occupysaas'
AWNIX='https://raw.githubusercontent.com/Aitherium/awnix/main/install.sh'
YES=0
SKIP_AWNIX=0

while [ $# -gt 0 ]; do
  case "$1" in
    --yes|-y) YES=1 ;;
    --collective) COLLECTIVE="$2"; shift ;;
    --lane) LANE="$2"; shift ;;
    --relay-channel) RELAY_CHANNEL="$2"; shift ;;
    --skip-awnix) SKIP_AWNIX=1 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

relay_flag=''
[ -n "$RELAY_CHANNEL" ] && relay_flag="--relay-channel $RELAY_CHANNEL"

cat <<EOF
Plan:
  1. $( [ "$SKIP_AWNIX" = 1 ] && echo 'skip awnix (already installed)' || echo "install awnix: curl -fsSL $AWNIX | sudo sh" )
  2. adk login
  3. adk volunteer enroll --lane $LANE --collective $COLLECTIVE $relay_flag
  4. adk volunteer serve --lane bonsai
  5. adk volunteer start --lane embed
  6. adk volunteer status
EOF

if [ "$YES" != 1 ]; then
  echo
  echo 'Dry run. Nothing has run. Pass --yes to execute this plan.'
  exit 0
fi

if [ "$SKIP_AWNIX" != 1 ]; then
  echo 'Installing awnix...'
  curl -fsSL "$AWNIX" | sudo sh
fi
command -v adk >/dev/null 2>&1 || {
  echo 'adk is not on PATH. Install awdk (pip install awdk) and re-run.' >&2
  exit 1
}
adk login
adk volunteer enroll --lane "$LANE" --collective "$COLLECTIVE" $relay_flag
adk volunteer serve --lane bonsai
adk volunteer start --lane embed
adk volunteer status
