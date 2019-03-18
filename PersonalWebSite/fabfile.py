from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "git@github.com:carl-3070/MyWebSite.git"

#env.user = 'ubuntu'
#env.password = ''
env.use_ssh_config = True
env.hosts = ['www.xiequanquan.com.cn'] 


env.port = '22'

def deploy():
  source_folder = '/home/ubuntu/sites/xiequanquan.com/MyWebSite'

  run('cd %s && git pull' % source_folder)
  run("""
      cd {} &&
      ../env/bin/pip install -r requirements.txt &&
      ../env/bin/python3 manage.py collectstatic --noinput &&
      ../env/bin/python3 manage.py migrate
      """.format(source_folder))
  sudo('systemctl restart gunicorn-xiequanquan.service')
  sudo('service nginx reload')
