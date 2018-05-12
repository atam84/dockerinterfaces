import docker
from ifaceinfo import InterfacesInfos
from pprint import pprint


def __convert_value(valuetoconvert):
    """
    private methode that convert from string to int or float or keep string if tye is not detected
    """
    _value = ''
    try:
        _value = int(valuetoconvert)
    except ValueError:
        try:
            _value = float(valuetoconvert)
        except ValueError:
            _value = valuetoconvert
    return _value


def __containers_collect_data():
    __dockerClient = docker.from_env()
    _containers = __dockerClient.containers.list()
    _containersinfos = {}
    for _container in _containers:
        _containersinfos[_container.short_id] = {
            'id': _container.id,
            'name': _container.name
        }
        # iface networks for this container
        _ifnetworks = _container.exec_run('ls /sys/class/net')
        if _ifnetworks.exit_code == 0:
            _ifnetworks = _ifnetworks.output.split('\n')
            # now for every interface located except lo and empty string in the list
            _ifnetworks = [_iface for _iface in _ifnetworks if _iface and _iface != 'lo']
            # now get ifindex, iflink and interface physical address for every interface
            for iface in _ifnetworks:
                _ifindex = _container.exec_run('cat /sys/class/net/' + iface + '/ifindex')
                _iflink = _container.exec_run('cat /sys/class/net/' + iface + '/iflink')
                _ifaddr = _container.exec_run('cat /sys/class/net/' + iface + '/address')
                _containersinfos[_container.short_id][iface] = {
                    'name': iface,
                    'ifindex': __convert_value(_ifindex.output) if _ifindex.exit_code == 0 else -1,
                    'iflink': __convert_value(_iflink.output) if _iflink.exit_code == 0 else -1,
                    'address': __convert_value(_ifaddr.output.replace('\n', '')) if _ifaddr.exit_code == 0 else 'unknown',
                }
    return _containersinfos

pprint(__containers_collect_data())