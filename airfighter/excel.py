__author__ = 'fahadadeel'
import jpype
import os.path


class PdfToExcel:
    
   def __init__(self, dataDir):
       print ("init func")
       self.dataDir = dataDir
       self.Document = jpype.JClass("com.aspose.pdf.Document")
       self.ExcelSaveOptions=jpype.JClass("com.aspose.pdf.ExcelSaveOptions")

   def main(self):

        # Open the target document
       doc=self.Document()
       pdf = self.Document()
       pdf=self.dataDir +'input1.pdf'

       # Instantiate ExcelSave Option object
       excelsave=self.ExcelSaveOptions();

       # Save the output to XLS format
       doc.save(self.dataDir + "Converted_Excel.xls", excelsave);

       print ("Document has been converted successfully")


asposeapispath = os.path.join(os.path.abspath("../../../"), "lib")

print ("You need to put your Aspose.Words for Java APIs .jars in this folder:\n"+asposeapispath)

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.ext.dirs=%s" % asposeapispath)

testObject = PdfToExcel('data/')
testObject.main()



doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'C-4 2002.pdf'
 
# Instantiate ExcelSave Option object
excelsave=self.ExcelSaveOptions();
 
# Save the output to XLS format
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
 
print ("Document has been converted successfully")