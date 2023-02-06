#!/usr/bin/env python3

import sys

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, ParserRuleContext

from grammar.PlSqlLexer import PlSqlLexer
from grammar.PlSqlParserListener import PlSqlParserListener
from grammar.PlSqlParser import PlSqlParser

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
		id = ''
		if ruleName in ('regular_id', 'native_datatype_element'):
			id = 'id="{}"'.format(ctx.getText())
		print('{}{} {}'.format(' ' * self.indent, ruleName, id))

	def enterEveryRule(self, ctx: ParserRuleContext):
		self.debugRule(ctx)
		self.indent += 1

	def exitEveryRule(self, ctx: ParserRuleContext):
		self.indent -= 1

class PlSqlParserListenerCustom(PlSqlParserListener):
	def __init__(self):
		self.parser: PlSqlParser | None = None
		self.indent: int = 0

	def print(self, text: str):
		print(' ' * self.indent + text)

	def enterSql_script(self, ctx: PlSqlParser.Sql_scriptContext):
		self.print('enterSql_script')
		self.indent += 1

	def exitSql_script(self, ctx: PlSqlParser.Sql_scriptContext):
		self.indent -= 1

	def enterUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
		self.print('enterUnit_statement')
		self.indent += 1

	def exitUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
		self.indent -= 1

	def enterDrop_function(self, ctx: PlSqlParser.Drop_functionContext):
		self.print('enterDrop_function')
		self.indent += 1

	def exitDrop_function(self, ctx: PlSqlParser.Drop_functionContext):
		self.indent -= 1

	def enterCreate_function_body(self, ctx: PlSqlParser.Create_function_bodyContext):
		self.print('enterCreate_function_body')
		self.indent += 1

	def exitCreate_function_body(self, ctx: PlSqlParser.Create_function_bodyContext):
		self.indent -= 1

	def enterFunction_name(self, ctx:PlSqlParser.Function_nameContext):
		self.print('enterFunction_name')
		self.indent += 1

	def exitFunction_name(self, ctx:PlSqlParser.Function_nameContext):
		self.indent -= 1

	def enterIdentifier(self, ctx:PlSqlParser.IdentifierContext):
		self.print('enterIdentifier')
		self.indent += 1

	def exitIdentifier(self, ctx:PlSqlParser.IdentifierContext):
		self.indent -= 1

	def enterId_expression(self, ctx:PlSqlParser.Id_expressionContext):
		self.print('enterId_expression')
		self.indent += 1
	
	def exitId_expression(self, ctx:PlSqlParser.Id_expressionContext):
		self.indent -= 1

	def enterNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
		self.print('enterNative_datatype_element: "{}"'.format(ctx.getText()))
		self.indent += 1

	def exitNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
		self.indent -= 1

	def enterRegular_id(self, ctx:PlSqlParser.Regular_idContext):
		self.print('enterRegular_id: "{}"'.format(ctx.getText()))
		self.indent += 1

	def exitRegular_id(self, ctx:PlSqlParser.Regular_idContext):
		self.indent -= 1

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
