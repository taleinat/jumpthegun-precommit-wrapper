#!/bin/sh
script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
export PATH="$script_dir":"$PATH"
exec jumpthegun run jumpthegun-precommit-wrapper-main "$@"
