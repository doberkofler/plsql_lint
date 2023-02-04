#!/usr/bin/env python3

import sys

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParserRuleContext

from gramma.PlSqlLexer import PlSqlLexer
from gramma.PlSqlParserListener import PlSqlParserListener
from gramma.PlSqlParser import PlSqlParser

class PlSqlParserListenerDebug(PlSqlParserListener):
	def __init__(self):
		self.parser: PlSqlParser | None = None
		self.indent: int = 0

	def debugRule(self, ctx: ParserRuleContext):
		ruleName = ''
		if self.parser is not None:
			ruleIndex = ctx.getRuleIndex()
			ruleNames = self.parser.ruleNames
			ruleName = ruleNames[ruleIndex]
		print(' ' * self.indent + ruleName)

	def enterEveryRule(self, ctx: ParserRuleContext):
		self.debugRule(ctx)
		self.indent += 1

	def exitEveryRule(self, ctx: ParserRuleContext):
		self.indent -= 1

class PlSqlParserListenerCustom(PlSqlParserListener):
	def __init__(self):
		self.parser: PlSqlParser | None = None

	def enterSql_script(self, ctx: PlSqlParser.Sql_scriptContext):
		print('enterSql_script')
	
	def enterUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
		print('enterUnit_statement')
	
	def enterDrop_function(self, ctx: PlSqlParser.Drop_functionContext):
		print('enterDrop_function')

	def enterCreate_function_body(self, ctx: PlSqlParser.Create_function_bodyContext):
		print('enterCreate_function_body')

	def enterFunction_name(self, ctx:PlSqlParser.Function_nameContext):
		print('enterFunction_name')

	def enterIdentifier(self, ctx:PlSqlParser.IdentifierContext):
		print('enterIdentifier')

	def enterId_expression(self, ctx:PlSqlParser.Id_expressionContext):
		print('enterId_expression')

	def enterRegular_id(self, ctx:PlSqlParser.Regular_idContext):
		print('enterRegular_id: "{}"'.format(ctx.getText()))

def main(file: str):
	# Open a PL/SQL source code file for parsing
	with open("test.sql", "r") as plsql_file:
		# Convert the file into a character stream
		input_stream = InputStream(plsql_file.read())
		
		# Create a lexer object
		lexer = PlSqlLexer(input_stream)
		
		# Convert the lexer output into a token stream
		token_stream = CommonTokenStream(lexer)
		
		# Create a parser object
		parser = PlSqlParser(token_stream)

		# Attach the custom listener to the walker
		listener = PlSqlParserListenerDebug()
		listener.parser = parser

		# Create a walker object
		walker = ParseTreeWalker()
		walker.walk(listener, parser.sql_script())

if __name__ == "__main__":
	filename = 'test.sql'
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	
	main(filename)
