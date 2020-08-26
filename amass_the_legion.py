#!/usr/bin/env python3

import argparse
import subprocess as SP

output_file = 'enum_result.txt'


def main():
    parser = argparse.ArgumentParser(
        description='Enumerating hosts and domains via OWASP AMASS')
    parser.add_argument('-t', '--target')
    parser.add_argument('--token')
    parser.add_argument('-n', '--name')
    args = parser.parse_args()

    target = args.target
    token = args.token
    name = args.name

    amass_command = ["amass", "enum", "-active",
                     "-d", target, "-p", "80,443,8080"]
    nexploit_cli_command = ["nexploit-cli", "scan:run", "--token", token,
                            "--name", f'"amass_scan_{name}"', "--crawler", f'"http://{target}"'
                           ]

    with open(output_file, "w+") as f:
        SP.call(amass_command, stdout=f)

    with open(output_file, "r") as f:
        for host in f:
            stripped = host.strip('\n')
            host = f'"{stripped}"'
            nexploit_cli_command.append("--host-filter")
            nexploit_cli_command.append(host)
    print(*nexploit_cli_command)
    nexploit_cli_command.append("--smart")
    try:
        SP.call(nexploit_cli_command)
    except:
        print("Error when trying to call nexploit_cli")


if __name__ == "__main__":
    main()
