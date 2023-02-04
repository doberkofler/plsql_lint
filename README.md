# The pluggable linting utility for PL/SQL

## Development

### install

pip3 install --upgrade pip3

pip3 uninstall antlr4-tools
pip3 install antlr4-tools

pip3 uninstall antlr4-python3-runtime
pip3 install antlr4-python3-runtime

### download pl/sql gramma

curl --output PlSqlLexer.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlLexer.g4
curl --output PlSqlParser.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlParser.g4

curl --output out/PlSqlLexerBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlLexerBase.py
curl --output out/PlSqlParserBase.py https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/Python3/PlSqlParserBase.py

### convert gramma

antlr4 -Dlanguage=Python3 -o out PlSqlLexer.g4
antlr4 -Dlanguage=Python3 -o out PlSqlParser.g4
chmod 777 out/*.py

### test gramma

./test.py

### links

https://www.antlr.org
https://pypi.org/project/antlr-plsql
https://github.com/antlr/grammars-v4/blob/master/sql/plsql/Python3/PlSqlParserBase.py
https://alanhohn.com/posts/2016/antlr-python
https://faun.pub/introduction-to-antlr-python-af8a3c603d23
https://cucurbit.dev/posts/code-formatting-with-antlr-python
