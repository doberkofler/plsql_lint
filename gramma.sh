#!/bin/sh

# clean
rm -rf gramma
mkdir gramma

# download gramma
curl --output gramma/PlSqlLexer.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlLexer.g4
curl --output gramma/PlSqlParser.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlParser.g4

# download helper
curl --output gramma/PlSqlLexerBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlLexerBase.py
curl --output gramma/PlSqlParserBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlParserBase.py

### convert gramma
antlr4 -Dlanguage=Python3 gramma/PlSqlLexer.g4
antlr4 -Dlanguage=Python3 gramma/PlSqlParser.g4

# chmod
chmod 777 gramma/*.py
