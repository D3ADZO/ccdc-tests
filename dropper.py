from winrm.protocol import Protocol

def main():
    print("WinRM")
    username=input("USERNAME: ")
    passwd=input("PASSWORD: ")
    point=input("TARGET IP: ")
    command = input("CMD: ")
    p = Protocol(
        endpoint='https://' + point + ':5986/wsman',
        transport='ntlm',
        username=r'.\\' + username,
        password=passwd,
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, 'cmd.exe', ['/c ' + command + '])
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    print("OUTPUT: " + std_out)
    print("ERROR: " + std_err)
    print("STATUS CODE: " + status_code)
    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)

main()