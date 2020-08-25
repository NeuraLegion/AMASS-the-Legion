import sys
import subprocess as SP
import uuid
    # DEAISAWESOME PRINT READ COMMIT

def main():
    target = sys.argv[1]
    token = sys.argv[2]
    name = sys.argv[3]

    amass_command = ["amass", "enum", "-active", "-d", target, "-p", "80,443,8080"]
    nexploit_cli_command = ["nexploit-cli", "scan:run", "--token", token, "--name", f'"amass_scan_{name}"', "--crawler", target, "--smart", "--host-filter"]

    _file = open("enum_result.txt", "w+")
    SP.call(amass_command, stdout=_file)
    _file.close()

    f = open("enum_result.txt", "r")
    host_list = []
    for host in f:
        host_list.append(host.strip('\n'))
    nexploit_cli_command.append(host_list) 
    f.close()
    print(*nexploit_cli_command)
    try:
        SP.call(nexploit_cli_command)
    except:
        print("Error when trying to call nexploit_cli")
if __name__ == "__main__":
    main()
