#!/bin/bash

set -e

# Install dependencies
python3 -m pip install -r requirements.txt

bash setup/branch_1.sh
bash setup/branch_2.sh
bash setup/branch_3.sh
bash setup/branch_4.sh