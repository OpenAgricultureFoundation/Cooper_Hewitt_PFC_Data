import sys, getopt

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:", ["ifile=","ofile="])
  except getopt.GetoptError:
    print("pull_urls.py -i <inputfile> -o <outputfile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print("pull_urls.py -i <inputfile> -o <outputfile>")
      sys.exit()
    elif opt in ("-i","--ifile"):
      inputfile = arg
    elif opt in ("-o","--ofile"):
      outputfile = arg

  urls = []
  with open(inputfile) as inf:
    print("reading input file")
    for line in inf.readlines():
      if "http" in line:
        urls.append(line.split(",")[3])
  print("found " + str(len(urls)) + " urls")
  with open(outputfile,"w") as outf:
    print("writing output file")
    outf.write("\n".join(urls))
    outf.flush()

if __name__ == "__main__":
  main(sys.argv[1:])
