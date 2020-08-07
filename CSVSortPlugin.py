class CSVSortPlugin:
   def input(self, inputfile):
      filestuff = open(inputfile, 'r')
      self.firstline = filestuff.readline()
      self.lines = []
      for line in filestuff:
         self.lines.append(line.strip())

   def run(self):
      self.lines.sort()

   def output(self, outputfile):
      filestuff = open(outputfile, 'w')
      filestuff.write(self.firstline)
      for i in range(len(self.lines)):
      #for line in self.lines:
         filestuff.write(self.lines[i])
         if (i != len(self.lines)-1):
            filestuff.write("\n")
