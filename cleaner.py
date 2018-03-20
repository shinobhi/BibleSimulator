# helper program to properly insert verse opening and verse closing tags to corpora

inp = input("Please enter the name of the desired file to process: ")

with open(inp) as infile, open('corpus-' + inp, 'w') as outfile:
	for line in infile:
		if not line.strip(): # deal with empty line
			outfile.write("</verse>\n")
			outfile.write("<verse>")
		outfile.write(line)
	outfile.write("</verse>")

print("Done.")