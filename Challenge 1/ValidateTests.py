import re, glob, subprocess
from subprocess import STDOUT,PIPE

input_files = sorted(glob.glob('../Testcases/input/*.txt'))

NUMBER_FINDER = re.compile(r'\d+')

class validateTests:

    def __init__(self, language = 'python'):
        self.language = language
        
        if language == "c":
            self.compile_c('CSolution.c')
        elif language == "cpp":
            self.compile_cpp('CppSolution.cpp')
        elif language == "java":
            self.compile_java('JavaSolution.java')

        self.run_tests()

    def run_tests(self):
        print("\n\n-------------------------")
        print("Running Tests...")
        print("-------------------------")

        for tc_count, input_file in enumerate(input_files, 1):
            # Read input file
            with open(input_file) as f:
                input_data_lines = f.readlines()
                input_data = "".join(input_data_lines)
            
            # Get expected output file's name
            output_file = self.get_output_filename(input_file)

            # Read expected output file
            with open(output_file) as f:
                expected_output = f.readline().split()

            # Execute code with given input and retrieve code's output
            code_output = self.execute_code(input = input_data, lang = self.language)

            # Compare code's output with expected output and print verdict
            self.show_result(tc_count, code_output, expected_output)
    
    def show_result(self, tc_count, code_output, expected_output):
        print("-------------------------")
        print("Testcase #" + str(tc_count) + "...: ", end = "")
        if code_output == expected_output:
            print("PASS!")
        else:
            print("FAIL!")
            print("\nYour code output = " + " ".join(code_output))
            print("Expected output = " + " ".join(expected_output))
        print()

    def get_output_filename(self, input_filename):
        return '../Testcases/output/output%s.txt' % NUMBER_FINDER.findall(input_filename)[0]

    def compile_c(self, c_file):
        print("-------------------------")
        print("Compiling C Program...")
        print("-------------------------")
        subprocess.check_call(['gcc', c_file, '-o', 'CSolution'])

    def compile_cpp(self, cpp_file):
        print("-------------------------")
        print("Compiling C++ Program...")
        print("-------------------------")
        subprocess.check_call(['g++', cpp_file, '-o', 'CppSolution'])

    def compile_java(self, java_file):
        print("-------------------------")
        print("Compiling Java Program...")
        print("-------------------------")
        subprocess.check_call(['javac', java_file])

    def execute_code(self, input, lang):
        if lang == "c":
            cmd = ['./CSolution']

        elif lang == "cpp":
            cmd = ['./CppSolution']
 
        elif lang == "java":
            cmd = ['java', 'JavaSolution']

        elif lang == "python":
            cmd = ['python3', 'PythonSolution.py']

        else:
            raise Exception("Unsupported language!")  
        
        proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stdout,stderr = proc.communicate(bytes(input, "utf-8"))

        return stdout.decode("utf-8", errors='ignore').split()