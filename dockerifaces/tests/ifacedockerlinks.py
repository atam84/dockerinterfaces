import sys
sys.path.append('../')
import docker
from dockerifaces import DockerInterfaces
from pprint import pprint


def test_def():
    _containersNetworks = DockerInterfaces()
    print('** Local interfaces index and link: {}'.format(len(_containersNetworks.local_ifaces_index_link())))
    pprint(_containersNetworks.local_ifaces_index_link())
    print('\n')
    print('** Container interfaces informations: {}'.format(len(_containersNetworks.containers_ifaces())))
    pprint(_containersNetworks.containers_ifaces())
    print('\n****')
    pprint(_containersNetworks.local_ifaces_to_containers())
    print('****\n\n')
    pprint(_containersNetworks.containers_ifaces_to_local_ifaces())
    print('\n\n')
    pprint(_containersNetworks.containers_ifaces_index())
    pprint(_containersNetworks.containers_ifaces_addrs())
    pprint(_containersNetworks.containers_ifaces_link())
    pprint(_containersNetworks.containers_ifaces_statue())

if __name__ == '__main__':
    test_def()




