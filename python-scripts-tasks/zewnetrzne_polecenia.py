import subprocess

# subprocess.call('ls -al *.py', shell=True)
subprocess.call(['ls', '-al'])  # gwiazdkę obsługuje shell

# try:
#     subprocess.check_call(['ls', 'nieistniejacy_plik.txt'])
# except subprocess.CalledProcessError as e:
#     print(e)

print()
print(
    "Program zwrócił:",
    subprocess.check_output(['cat', 'hello_pl.txt']).decode('utf-8')
)

print(subprocess.check_output("wc -l", input=b"aaa\nbbb\n\c\n", shell=True))  # liczy linijki

print("Popen:")
proc = subprocess.Popen(['wc', '-l'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
out, err = proc.communicate(b"aaa\nbbb\n\c\n")
print(out.decode('utf-8'))

# można też subprocess.Popen( ..., encoding='utf-8')
# wtedy dostajemy str

# przydatna funkcja:

def cmd(command, output, ignore_errorcode):
    if output == 'all':
        # join the two streams in stdout
        stdout, stderr = subprocess.PIPE, subprocess.STDOUT
    elif output == 'none':
        stdout, stderr = subprocess.DEVNULL, subprocess.DEVNULL
    elif output == 'stdout':
        stdout, stderr = subprocess.PIPE, subprocess.DEVNULL
    elif output == 'stderr':
        stdout, stderr = subprocess.DEVNULL, subprocess.PIPE
    else:
        raise Exception("Unexpected output description %r" % output)

    completed = subprocess.run(command, capture_output=False, encoding='utf-8', stdout=stdout, stderr=stderr)

    if not ignore_errorcode:
        # If returncode is non-zero, raise a CalledProcessError.
        completed.check_returncode()

    return completed.stderr if completed.stderr is not None else completed.stdout


# Konsola cmd Windows
# spr. encoding na cmd: chcp --> 852
# encoding='cp852'