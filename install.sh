#!/bin/sh

pip3 install --upgrade pip3

pip3 uninstall antlr4-tools
pip3 install antlr4-tools

pip3 uninstall antlr4-python3-runtime
pip3 install antlr4-python3-runtime
