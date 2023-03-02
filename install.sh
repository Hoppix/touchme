#!/usr/bin/env bash


# switch to script directory
cd "$(dirname "$0")"

main() {
    pushd
    git clone https://github.com/Hoppix/touchme/
    cd touchme
    pip install -r requirements.txt
    python3 setup.py install
    touchme --help
    popd
}

# call function with all given parameters
main "$@"
