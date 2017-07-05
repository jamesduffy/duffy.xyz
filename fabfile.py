"""Deploy duffy.xyz"""
import time

from fabric.api import cd, env, sudo, task, run


env.user = 'james'
env.key_filename = '~/.ssh/id_rsa'
env.hosts = [
    '138.197.239.70',
]

project = dict(
    name='duffy.xyz',
    repository='git@bitbucket.org:dffy/duffy.xyz_flask.git',
    release='release_%s' % int(time.time() * 1000),
    settings='duffyxyz.config.prod',
)


@task
def deploy(branch='master'):
    # Create project directories if they do not exist
    run('[ -d /webapps/%(name)s ] || mkdir /webapps/%(name)s' % project)
    run('[ -d /webapps/%(name)s/releases ] || mkdir /webapps/%(name)s/releases' % project)
    run('[ -d /webapps/%(name)s/storage ] || mkdir /webapps/%(name)s/storage' % project)

    # Fetch repository
    with cd('/webapps/%s/releases' % (project['name'])):
        run('git clone --depth 1 -b %s %s %s' % (branch, project['repository'], project['release']))

    with cd('/webapps/%(name)s/releases/%(release)s' % project):
        # Setup Virtualenv
        run('virtualenv .')

        # Install PIP dependencies
        run('bin/pip install -r requirements.txt')

        # Link storage directory into release
        run('ln -snf "/webapps/%(name)s/storage" "/webapps/%(name)s/releases/%(release)s/storage"' % project)

    # Bring online
    sudo('ln -snf /webapps/%(name)s/releases/%(release)s /webapps/%(name)s/current' % project)
    sudo('service nginx reload')
    sudo('service uwsgi restart')

    # Cleanup release artifacts
    sudo('rm -rf `ls -dt /webapps/%(name)s/releases/* | tail -n +6`' % project)
