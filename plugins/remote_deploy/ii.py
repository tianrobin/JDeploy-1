import paramiko

result = ""

try:
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect("192.168.101.237", 22, "barry", "123456", timeout=3)

    # stdin, stdout, stderr = ssh.exec_command("ls")
    # result = stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("echo 123456 | sudo -S ls")
    # print stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("")
    # print stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("echo 123456 | sudo -S ls")
    # print stdout.read()


    a = '''
        pwd;

        echo 123456 | sudo -S ls > /dev/null

        sudo ls



        sudo ls -al


        ls /;
        rm -rf fabric;
        rm -rf fabricd;
        rm -rf tests;
        ls

        pwd;
        sudo touch kkkk;
        ls | grep kkkk;

        # sudo -k

        echo 123456 | sudo -S ls > /dev/null

        sudo ps
        '''


    print repr(a)

    stdin, stdout, stderr = ssh.exec_command(
        a
    )
    # print stdout.read()
    # print stderr.read()

    stdin, stdout, stderr = ssh.exec_command(
        '''
        pwd
        rm -rf insight
        rm -rf dimension_report

        ls insight
        ls dimension_report

        git clone -b productionD_master http://barry:12345678@192.168.200.19/AnalysisTeam/insight.git --depth=1
        ls insight

        mv ./insight/new_report/code/dimension_report .
        cp ./dimension_report/cfg/config_www_productionD.py ./dimension_report/cfg/config.py

        echo 123456 | sudo -S ls > /dev/null
        sudo ls
        pwd
        '''
    )
    print stdout.read()
    print stderr.read()

    ssh.close()

except:

    print("ssh_cmd err.")

print  result