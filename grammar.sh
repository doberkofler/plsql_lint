#!/bin/sh

# clean
rm -rf grammar
mkdir grammar

# download gramma
curl --output grammar/PlSqlLexer.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlLexer.g4
curl --output grammar/PlSqlParser.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlParser.g4

# download helper
curl --output grammar/PlSqlLexerBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlLexerBase.py
curl --output grammar/PlSqlParserBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlParserBase.py

### convert gramma
antlr4 -Dlanguage=Python3 grammar/PlSqlLexer.g4
antlr4 -Dlanguage=Python3 grammar/PlSqlParser.g4

# chmod
chmod 777 grammar/*.py
