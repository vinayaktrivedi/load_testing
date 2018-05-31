from dateutil import parser
string="2017-10-07 08:24:34"
string2="2017-10-08 08:24:34"
print(parser.parse(string2)-parser.parse(string))