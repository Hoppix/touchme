#!/usr/bin/env bash


# switch to script directory
cd "$(dirname "$0")"

main() {
    pushd
    git clone https://github.com/Hoppix/touchme/
    cd touchme
    python3 -m pip install --user virtualenv
    source venv/bin/activate
    pip -r requirements.txt
    python3 setup.py install
    touchme --help
}

# call function with all given parameters
main "$@"