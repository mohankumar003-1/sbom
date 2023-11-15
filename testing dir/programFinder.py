import re
import os
from pipreqs import pipreqs
import subprocess
def findLanguagefromExtension(val):
    if(val == '.py'):
        print("python")
        return "python"
    elif(val == '.java'):
        print('java')
        return "java"
    elif(val == '.cpp'):
        print('cpp')
        return "cpp"
    elif(val == '.js'):
        print('javascript')
        return "js"
def findLanguage(filename):
    with open(filename,'r') as file:
        text = file.read()
    match = re.findall('self',text)
    
    pos = filename.find('.')
    result = filename[pos :]
    language = findLanguagefromExtension(result)
    return language
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
def dependencies(path):
    subprocess.run(["pipreqs", "--force",path])
def vulnerability(path):
    result = subprocess.run(["bandit", "-r",path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("Bandit found no issues.")
    else:
        print("Bandit found issues. Here's the report:")
        print(result.stdout)

path = r'C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\sbom\test'

if os.path.isdir(path):
     files = os.listdir(path)
     for file in files:
        print(file)
        language = findLanguage(os.path.join(path,file))
        if(language == "python"):
            vulnerability(path)
            dependencies(path)
        if(language == "java"):
            print("hi")
        

        
else:
    print(f"{path} is not a valid directory.")

# import subprocess

# java_file = r"C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\sbom\test"
# result = subprocess.run(["pylint", java_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# if result.returncode != 0:
#     print("Vulnerabilities detected:")
#     print(result.stdout)
# else:
#     print("No vulnerabilities detected.")