#!/bin/sh
script_path="$0"
# If this is a symlink, read it.
if [ -L "$script_path" ]; then
  script_path="$(readlink "$script_path")"
fi
script_dir="$(CDPATH= cd -- "$(dirname -- "$script_path")" && pwd)"
export PATH="$script_dir":"$PATH"
exec jumpthegun run jumpthegun-precommit-wrapper-main "$@"
