import re
from pipreqs import pipreqs
def findLanguagefromExtension(val):
    if(val == '.py'):
        print("python")
    elif(val == '.java'):
        print('java')
    elif(val == '.cpp'):
        print('cpp')
    elif(val == '.js'):
        print('javascript')
def findLanguage(filename):
    with open(filename,'r') as file:
        text = file.read()
    match = re.findall('self',text)
    
    pos = filename.find('.')
    result = filename[pos :]
    findLanguagefromExtension(result)
    # if(pos == -1):
    #     print("cant find")
    # elif(match[0]== 'self' or match[0]== 'None' or match[0]== 'as' or match[0]== 'lambda'or match[0]== 'pass'or match[0]== 'with'  ):
    #     print("python")
    # elif(match[0]== 'final' or match[0]== 'extends' or match[0]== 'implements' or match[0]== 'super'  or match[0]== 'synchronized'  ):
    #     print("java")
    # elif(match[0]== 'this' or match[0]== 'var' or match[0]== 'let' or match[0]== 'const' or match[0]== 'window' or match[0]== 'document' or match[0]== '=>' or match[0]== 'await' or match[0]== 'JSON.parse' or match[0]== 'JSON.stringify' or match[0]== 'Promise' or match[0]== 'NaN'  ):
    #     print("javascript")
    # elif(match[0]== 'namespace' or match[0]== 'constructor' or match[0]== 'destructor' or match[0]== 'friend' or match[0]== 'template' or match[0]== 'STL' or match[0]== 'virtual'  ):
    #     print("c++")
    
        
        
findLanguage('test.py')