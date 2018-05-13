#!/usr/bin/env python

#
# Author : Mohamed Amine TAMDY
# Email  : amine.tamdy@gmail.com
# Github : https://github.com/atam84
# story  : modification of sample script used in ifaceinfo, modified to manage containers interconnexion informations
#


import sys
sys.path.append('../')
from ifaceinfo import InterfacesInfos
from dockerifaces import DockerInterfaces
from pprint import pprint

class COLOR:
    class fg:
        BLACK   = '\033[30m'
        RED     = '\033[31m'
        GREEN   = '\033[32m'
        YELLOW  = '\033[33m'
        BLUE    = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN    = '\033[36m'
        WHITE   = '\033[37m'
        RESET   = '\033[39m'

    class bg:
        BLACK   = '\033[40m'
        RED     = '\033[41m'
        GREEN   = '\033[42m'
        YELLOW  = '\033[43m'
        BLUE    = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN    = '\033[46m'
        WHITE   = '\033[47m'
        RESET   = '\033[49m'

    class style:
        BOLD    = '\033[1m'
        DIM       = '\033[2m'
        NORMAL    = '\033[22m'
        RESET_ALL = '\033[0m'
        UNDERLINE = '\033[4m'

cl = COLOR

def color_string(__tite_string, __color=COLOR.fg.WHITE, __style=COLOR.style.NORMAL):
    '''
    retun json that have two keys string and colored, by default it return white with normal style
    '''
    return {
        'string': __tite_string,
        'colored': __style + __color + __tite_string + COLOR.style.RESET_ALL
    }

def warning_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.YELLOW, COLOR.style.NORMAL)
def error_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.RED, COLOR.style.NORMAL)
def success_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.GREEN, COLOR.style.NORMAL)
def info_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.BLUE, COLOR.style.NORMAL)
def important_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.CYAN, COLOR.style.NORMAL)
def message_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.MAGENTA, COLOR.style.NORMAL)
def white_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.WHITE, COLOR.style.NORMAL)


def warning_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.YELLOW, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def error_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.RED, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def success_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.GREEN, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def info_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.BLUE, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def important_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.CYAN, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def message_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.MAGENTA, COLOR.style.NORMAL + COLOR.style.UNDERLINE)
def white_u_normal_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.WHITE, COLOR.style.NORMAL + COLOR.style.UNDERLINE)


def warning_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.YELLOW, COLOR.style.BOLD)
def error_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.RED, COLOR.style.BOLD)
def success_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.GREEN, COLOR.style.BOLD)
def info_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.BLUE, COLOR.style.BOLD)
def important_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.CYAN, COLOR.style.BOLD)
def message_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.MAGENTA, COLOR.style.BOLD)
def white_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.WHITE, COLOR.style.BOLD)


def warning_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.YELLOW, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def error_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.RED, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def success_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.GREEN, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def info_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.BLUE, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def important_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.CYAN, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def message_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as '''
    return color_string(__str, COLOR.fg.MAGENTA, COLOR.style.BOLD + COLOR.style.UNDERLINE)
def white_u_bold_string(__str):
    ''' return formated object string that can be displayed in therminal as bold underline white string '''
    return color_string(__str, COLOR.fg.WHITE, COLOR.style.BOLD + COLOR.style.UNDERLINE)

def get_network_interfaces():
    ifaces = InterfacesInfos().ifaces_as_dict()
    containers = DockerInterfaces().local_ifaces_to_containers()
    _report = {
        'n_iface': 0,
        'iface_oper_up': 0,
        'iface_oper_down': 0,
        'iface_oper_unknown': 0,
        'br_count': 0,
    }
    for interface in ifaces:
        #_ifacename =  cl.style.BOLD + interface + cl.style.RESET_ALL
        _ifacename = white_bold_string(interface)
        _report['n_iface'] += 1
        _operstate = ifaces[interface]['operstate']
        if _operstate == 'up':
            _report['iface_oper_up'] += 1
            _operstate = cl.fg.GREEN + _operstate + cl.fg.RESET
        elif _operstate == 'down':
            _report['iface_oper_down'] += 1
            _operstate = cl.fg.RED + _operstate + cl.fg.RESET
        else:
            _report['iface_oper_unknown'] += 1
            _operstate = cl.fg.YELLOW + _operstate + cl.fg.RESET
        
        _collisions = ifaces[interface]['statistics']['collisions']
        if _collisions == 0:
            _collisions = cl.fg.GREEN + str(_collisions) + cl.fg.RESET
        else:
            _collisions = cl.fg.RED + str(_collisions) + cl.fg.RESET
        _multicast = str(ifaces[interface]['statistics']['multicast'])
        _tx_errors = ifaces[interface]['statistics']['tx_errors']
        if _tx_errors == 0:
            _tx_errors = cl.fg.GREEN + str(_tx_errors) + cl.fg.RESET
        elif _tx_errors <= 100:
            _tx_errors = cl.fg.YELLOW + str(_tx_errors) + cl.fg.RESET
        else:
            _tx_errors = cl.fg.RED + str(_tx_errors) + cl.fg.RESET
        _rx_errors = ifaces[interface]['statistics']['rx_errors']
        if _rx_errors == 0:
            _rx_errors = cl.fg.GREEN + str(_rx_errors) + cl.fg.RESET
        elif _rx_errors <= 100:
            _rx_errors = cl.fg.YELLOW + str(_rx_errors) + cl.fg.RESET
        else:
            _rx_errors = cl.fg.RED + str(_rx_errors) + cl.fg.RESET
        _devtype = ifaces[interface]['uevent']['devtype']
        if _devtype == 'bridge':
            _report['br_count'] += 1
            _devtype = cl.style.BOLD + _devtype + cl.style.RESET_ALL
        elif _devtype == 'wlan':
            _devtype = cl.style.BOLD + cl.fg.MAGENTA + _devtype + cl.style.RESET_ALL
        elif _devtype == 'unknown':
            _devtype = cl.style.BOLD + cl.fg.BLUE + _devtype + cl.style.RESET_ALL
        else:
            _devtype = cl.style.BOLD + cl.fg.YELLOW + _devtype + cl.style.RESET_ALL
        _marker = warning_bold_string('**') # cl.fg.YELLOW + '**' + cl.fg.RESET
        print('{} interface name: {}    id: {}     type: {}'.format(_marker['colored'], _ifacename['colored'], ifaces[interface]['dev_id'], ifaces[interface]['type']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('dev type', _devtype, 'operstate', _operstate))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('address', ifaces[interface]['address'], 'iface alias', ifaces[interface]['ifalias']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('iface link', str(ifaces[interface]['iflink']), 'iface index', str(ifaces[interface]['ifindex'])))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('ip', ifaces[interface]['ip'], 'mask', ifaces[interface]['mask']))
        print('      {:14s} : {:22s} {:14s} : {:22s}'.format('network', ifaces[interface]['network_address'],'mtu', str(ifaces[interface]['mtu'])))
        #ifaces[interface]['timestamp']
        #ifaces[interface]['name_assign_type']
        print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'interface statistics:' + cl.style.RESET_ALL))
        print('        {:20s} {:10s} {:14s}  {:10s}'.format('multicast       :', _multicast, 'collisions      :', _collisions))
        print('        {:20s} {}/{}'.format('bytes (tx/rx)   :', str(ifaces[interface]['statistics']['tx_bytes']), str(ifaces[interface]['statistics']['rx_bytes'])))
        print('        {:20s} {}/{}'.format('packets (tx/rx) :', str(ifaces[interface]['statistics']['tx_packets']), str(ifaces[interface]['statistics']['rx_packets'])))
        print('        {:20s} {}/{}'.format('errors (tx/rx)  :', _tx_errors, _rx_errors))
        if ifaces[interface]['uevent']['devtype'] == 'bridge':
            if 'lower' in ifaces[interface]:
                print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'bridge connected interfaces:' + cl.style.RESET_ALL))
                for key in ifaces[interface]['lower']:
                    #if key.startswith('lower_'):
                    __ifaceconnected = ifaces[interface]['lower'][key]['uevent']['interface']
                    __havecontainerconnected = ''
                    if __ifaceconnected in containers:
                        __havecontainerconnected = '<-> container id: {:s}  {:s}  {:s}'.format(containers[__ifaceconnected]['container']['short_id'], containers[__ifaceconnected]['container']['address'], containers[__ifaceconnected]['container']['operstate'])
                    print('        {:20s} {:20s} {:s} {:s} '.format(ifaces[interface]['lower'][key]['uevent']['interface'], ifaces[interface]['lower'][key]['address'], ifaces[interface]['lower'][key]['operstate'], __havecontainerconnected))

        else:
            if 'upper' in ifaces[interface]:
                print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'device connected on bridge:' + cl.style.RESET_ALL))
                for key in ifaces[interface]['upper']:
                    #if key.startswith('upper_'):
                    print('        {:20s} {:20s} {:s}'.format(ifaces[interface]['upper'][key]['uevent']['interface'], ifaces[interface]['upper'][key]['address'], ifaces[interface]['upper'][key]['operstate']))
        if interface in containers:
            print('        connected to container id: {}    addr: {}     state: {}'.format(containers[interface]['container']['short_id'], containers[interface]['container']['address'], containers[interface]['container']['operstate']))
        
        print('\n')
    print('---------------')
    #print('{}{} network interfaces that include {} bridge listed where {} up, {} down and {} with unknown status.{}'.format(cl.fg.WHITE, _report['n_iface'], _report['br_count'], _report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown'], cl.fg.RESET))
    print('{}{}'.format(cl.style.BOLD, cl.fg.WHITE))
    print('{} network interfaces that include {} bridge listed'.format(_report['n_iface'],_report['br_count']))
    print('{} up, {} down and {} with unknown status.'.format(_report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown']))
    print('{}'.format(cl.style.RESET_ALL))
    print('---------------')
'''
ifacename : {
    'ifindex': __localifaces['ifindex'],
    'iflink': __localifaces['iflink'],
    'ip': __localifaces['ip'],
    'mask': __localifaces['mask'],
    'name': __localifaces['name'],
    'network_address': __localifaces['network_address'],
    'operstate': __localifaces['operstate'],
    'container': {
        'short_id':__c_shortid,
        'address': __c_ifaceaddr,
        'ifindex': __c_ifindex,
        'iflink': __c_iflink,
        'ifacename': __c_ifacename,
        'id': __c_id,
        'name': __iface,
        'operstate': __c_ifoperstate
    }
}


{'veth5a7105e': {'container': {'address': u'02:42:ac:11:00:02',
                               'id': u'4240c1a56ce64ca500e7bea4f5d9f31516134c095a2aedafeeb5999477b3c352',
                               'ifacename': u'eth0',
                               'ifindex': 15,
                               'iflink': 16,
                               'name': u'eth0',
                               'operstate': u'up',
                               'short_id': u'4240c1a56c'},
                 'ifindex': 16,
                 'iflink': 15,
                 'ip': '169.254.54.26',
                 'mask': '255.255.0.0',
                 'name': 'veth5a7105e',
                 'network_address': '169.254.0.0',
                 'operstate': 'up'},
'''

if __name__ == '__main__':
    get_network_interfaces()

