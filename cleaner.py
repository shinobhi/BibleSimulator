# helper program to properly insert verse opening and verse closing tags to corpora

inp = input("Please enter the name of the desired file to process: ")

with open('corpora-raw/' + inp) as infile, open('corpora/' + inp, 'w') as outfile:
	first = True
	for line in infile:
		if first == True and not line.strip():
			outfile.write("<verse>")
			first = False
		elif not line.strip(): # deal with empty line
			outfile.write("</verse>\n")
			outfile.write("<verse>")
		outfile.write(line)
	outfile.write("</verse>")

print("Done.")