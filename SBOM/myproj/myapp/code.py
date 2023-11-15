import re
import os
from pipreqs import pipreqs
import subprocess
rule = []
vul =[]
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
def pyvulnerability(path,i):
    result = subprocess.run(["bandit", "-r",path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("Bandit found no issues.")
        rule.append(0)

    else:
        print("Bandit found issues. Here's the report:")
        rule.append(1)
        output_folder = path
        output_file_path = os.path.join(output_folder, "bandit_report"+str(i)+".txt")
        with open(output_file_path, "w") as output_file:
            output_file.write(result.stdout) 
        print(f"Bandit report saved to {output_file_path}")
        with open(output_file_path, "r") as report_file:
            report_content = report_file.read()
        high_counts = re.findall(r'\bHigh:\s*(\d+)\b', report_content)
        low_counts = re.findall(r'\bLow:\s*(\d+)\b', report_content)
        medium_counts = re.findall(r'\bMedium:\s*(\d+)\b', report_content)
        high_count = [int(x) for x in high_counts]
        medium_count = [int(x) for x in medium_counts]
        low_count = [int(x) for x in low_counts]
        high_val = sum(high_count)/len(high_count)
        medium_val = sum(medium_count)/len(medium_count)
        low_val = sum(low_count)/len(low_count)
        if high_val > medium_val and high_val > low_val :
            vul.append(2)
            print("HIGH!!!")
        elif medium_val>high_val and medium_val>low_val:
            vul.append(1)
            print("Medium!!")
        else:
            vul.append(0)
            print("LOW!!")
        print(f"High severity counts: {high_counts}")
        print(f"medium severity counts: {medium_counts}")
        print(f"low severity counts: {low_counts}")
        return vul

# def javavulnerability(path):
#     result = subprocess.run(["spotbugs_commands", "-textui", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# def cppvulnerability(path):
#     result = subprocess.run(["bandit", "-r", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# def cvulnerability(path):
#     result = subprocess.run(["bandit", "-r", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# def jsvulnerability(path):
#     result = subprocess.run(["eslint", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def folderaccess():
    sol = []
    path1  =  os.path.join(path,assist(path))
    if os.path.isdir(path1):
        files = os.listdir(path1)
        print(files)
        i=0
        for file in files:
            language = findLanguage(os.path.join(path1,file))
            if(language == "python"):
                a = pyvulnerability(path1,i)
                pydependencies(path1)
                i = i+1
                
            # elif(language == "java"):
            #     print("gu")
            #     javavulnerability(path1)
            # #javadependencies(path)
            # elif(language == "cpp"):
            #     cppvulnerability(path1)
            # #cppdependencies(path)
            # elif(language == "js"):
            #     jsvulnerability(path1)
            # #jsdependencies(path)
            # elif(language == "c"):
            #     cvulnerability(path1)
            #cdependencies(path) 
        ans = sum(a)/len(a)
        if ans>1.0 :
            sol.append(2)
            print("HIGH")

        elif ans>0.5 and ans<=1 :
            sol.append(1)
            print("MEDIUM")
        else:
            sol.append(0)
            print("LOW")
        print(ans)
        sol.append(rules())
        print(sol)
        return sol
    else:
        print(f"{path} is not a valid directory.")   
def rules():
    ans =0
    for i in rule:
        ans += i
    print(ans)
    return (ans/len(rule))*100
def assist(path):
    
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for a in directories:
        print(a)
        return a


path = r'C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\sbom\SBOM\myproj\media\extracted_zips'



