#!/usr/bin/env bash

# So that when a command fails, bash exits instead of continuing with the rest of the script.
set -o errexit

# This will ensure that a pipeline command is treated as failed, even if one command in the pipeline fails.
set -o pipefail

# This will make the script fail, when accessing an unset variable.
# When you want to access a variable that may or may not have been set, use "${VARNAME-}" instead of "$VARNAME", and you’re good.
set -o nounset

# enter debug mode
# print all variables, outputs and the executed code
# People can now enable debug mode, by running your script as TRACE=1 ./script.sh
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

# add help message for -h or -help
# Use long options, where possible (like --silent instead of -s). These serve to document your commands explicitly.
if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./script.sh arg-one arg-two

This is an awesome bash script to make your life better.

'
    exit
fi

# switch to script directory
cd "$(dirname "$0")"

myvar="global"
# use functions to organize your code
main() {
    # use local variables
    local script_name="$0"
    local myvar="local"
    echo "$myvar"
    echo "do awesome stuff"
}

# call function with all given parameters
main "$@"

# use `shellcheck`

# sources
# - https://sharats.me/posts/shell-script-best-practices/
# - https://www.redhat.com/sysadmin/arguments-options-bash-scripts
# - https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script
