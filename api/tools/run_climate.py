import os
import subprocess

def run_codeclimate(file_path, engine_name):
    dir_path = os.path.dirname(file_path) # 由文件绝对路径返回绝对目录
    command = "docker run --rm "
    command += "--env CODECLIMATE_CODE={} ".format(dir_path)
    command += "--volume {}:/code ".format(dir_path)
    command += "--volume /var/run/docker.sock:/var/run/docker.sock "
    command += "--volume /tmp/cc:/tmp/cc "
    command += "codeclimate/codeclimate analyze -f json -e {}".format(engine_name)
   # print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode('utf-8')
    #print(output)