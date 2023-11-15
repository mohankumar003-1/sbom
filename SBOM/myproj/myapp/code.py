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
    elif(val == '.c'):
        print('C')
        return "c"
    
def findLanguage(filename):
    
    
    pos = filename.find('.')
    result = filename[pos :]
    language = findLanguagefromExtension(result)
    return language
    
def pydependencies(path):
    subprocess.run(["pipreqs", "--force",path])
def pyvulnerability(path):
    result = subprocess.run(["bandit", "-r",path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("Bandit found no issues.")
    else:
        print("Bandit found issues. Here's the report:")
        print(result.stdout)    
def javavulnerability(path):
    result = subprocess.run(["spotbugs_commands", "-textui", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def cppvulnerability(path):
    result = subprocess.run(["bandit", "-r", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def cvulnerability(path):
    result = subprocess.run(["bandit", "-r", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def jsvulnerability(path):
    result = subprocess.run(["eslint", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def folderaccess():
    path1  =  os.path.join(path,assist(path))
    if os.path.isdir(path1):
        files = os.listdir(path1)
        print(files)
        for file in files:
            language = findLanguage(os.path.join(path1,file))
            if(language == "python"):
                pyvulnerability(path1)
                pydependencies(path1)
            elif(language == "java"):
                print("gu")
                javavulnerability(path1)
            #javadependencies(path)
            elif(language == "cpp"):
                cppvulnerability(path1)
            #cppdependencies(path)
            elif(language == "js"):
                jsvulnerability(path1)
            #jsdependencies(path)
            elif(language == "c"):
                cvulnerability(path1)
            #cdependencies(path)   

    else:
        print(f"{path} is not a valid directory.")   


def assist(path):
    
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for a in directories:
        print(a)
        return a

path = r'C:\Users\JEEVIKA\SBOM 3\myproj\media\extracted_zips'



