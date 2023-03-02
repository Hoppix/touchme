#!/usr/bin/env bash


# switch to script directory
cd "$(dirname "$0")"

main() {
    git clone https://github.com/Hoppix/touchme/
    pushd touchme
    pip install -r requirements.txt
    pip install .
    popd
    touchme --help
}

# call function with all given parameters
main "$@"
