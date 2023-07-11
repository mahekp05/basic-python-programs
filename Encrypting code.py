#Mahek Patel
#U10206053
#Encrypting code -- create an encryption for an existing file in an new file
    


def encrypt_file(text):
    Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
             'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
             'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
             'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
             'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
             'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
             'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
             'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
             'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
             '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
             '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
             '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
             ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
             "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
             '{':'[','[':'{','}':']',']':'}'}

    outfile = input('Enter output file name: ')
    etext = open(outfile,'w')
    
    for n in text:
        for x in n:
            encryption = (Encrypt_Code.get(x,x))
            etext.write(encryption)

    etext.close()


infile = input('Enter input file name (specify .txt at end): ')
file = open(infile,'r')
text = file.read()
print(text)
encrypt_file(text)

    


