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
        BOLD      = '\033[1m'
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

def eval_string(__str, is_Green, is_Yellow, is_Red, is_Other):
    __nstr = ''
    if __str == is_Green:
        __nstr = success_bold_string(__str)
    elif __str == is_Yellow:
        __nstr = warning_bold_string(__str)
    elif __str == is_Red:
        __nstr = error_bold_string(__str)
    else:
        __nstr = important_bold_string(__str)
    return __nstr



def get_network_interfaces():
    ifaces     = InterfacesInfos().ifaces_as_dict()
    containers = DockerInterfaces().local_ifaces_to_containers()
    _report = {
        'n_iface'           : 0,
        'iface_oper_up'     : 0,
        'iface_oper_down'   : 0,
        'iface_oper_unknown': 0,
        'br_count'          : 0
    }
    for interface in ifaces:
        #_ifacename =  cl.style.BOLD + interface + cl.style.RESET_ALL
        _ifacename = white_bold_string(interface)
        _report['n_iface'] += 1
        _operstate = eval_string(ifaces[interface]['operstate'], 'up', 'unknown', 'down', '')
        if _operstate['string'] == 'up':
            _report['iface_oper_up'] += 1
        elif _operstate['string'] == 'down':
            _report['iface_oper_down'] += 1
        else:
            _report['iface_oper_unknown'] += 1

        _collisions = str(ifaces[interface]['statistics']['collisions'])
        _multicast  = str(ifaces[interface]['statistics']['multicast'])
        _tx_errors  = str(ifaces[interface]['statistics']['tx_errors'])
        _rx_errors  = str(ifaces[interface]['statistics']['rx_errors'])

        _devtype = eval_string(ifaces[interface]['uevent']['devtype'], 'bridge', 'wlan', '', 'unknown')
        if _devtype['string'] == 'bridge':
            _report['br_count'] += 1

        _marker = warning_bold_string('**') # cl.fg.YELLOW + '**' + cl.fg.RESET
        print('{} interface name: {}    id: {}     type: {}'.format(_marker['colored'], _ifacename['colored'], ifaces[interface]['dev_id'], ifaces[interface]['type']))
        print('        {:14s} : {:22s} {:14s} : {:22s}'.format('dev type', _devtype['colored'], 'operstate', _operstate['colored']))
        print('        {:14s} : {:22s} {:14s} : {:22s}'.format('address', ifaces[interface]['address'], 'iface alias', ifaces[interface]['ifalias']))
        print('        {:14s} : {:22s} {:14s} : {:22s}'.format('iface link', str(ifaces[interface]['iflink']), 'iface index', str(ifaces[interface]['ifindex'])))
        print('        {:14s} : {:22s} {:14s} : {:22s}'.format('ip', ifaces[interface]['ip'], 'mask', ifaces[interface]['mask']))
        print('        {:14s} : {:22s} {:14s} : {:22s}'.format('network', ifaces[interface]['network_address'],'mtu', str(ifaces[interface]['mtu'])))
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
                        interface_state = eval_string(containers[__ifaceconnected]['container']['operstate'], 'up', 'unknown', 'down', '')
                        containershortid = white_normal_string(containers[__ifaceconnected]['container']['short_id'])
                        __havecontainerconnected = '<-> container id: {:s}  {:s}  {:s}'.format(containershortid['colored'], containers[__ifaceconnected]['container']['address'], interface_state['colored'])
                    vinterface_state = eval_string(ifaces[interface]['lower'][key]['operstate'], 'up', 'unknown', 'down', '')
                    print('        {:20s} {:20s} {:s} {:s} '.format(ifaces[interface]['lower'][key]['uevent']['interface'], ifaces[interface]['lower'][key]['address'], vinterface_state['colored'], __havecontainerconnected))
        else:
            if 'upper' in ifaces[interface]:
                print('    {}'.format(cl.style.DIM + cl.style.UNDERLINE + 'device connected on bridge:' + cl.style.RESET_ALL))
                for key in ifaces[interface]['upper']:
                    #if key.startswith('upper_'):
                    upper_iface = eval_string(ifaces[interface]['upper'][key]['operstate'], 'up', 'unknown', 'down', '')
                    print('        {:20s} {:20s} {:s}'.format(ifaces[interface]['upper'][key]['uevent']['interface'], ifaces[interface]['upper'][key]['address'], upper_iface['colored']))
        if interface in containers:
            container_iface = eval_string(containers[interface]['container']['operstate'], 'up', 'unknown', 'down', '')
            print('        connected to container id: {}    addr: {}     state: {}'.format(containers[interface]['container']['short_id'], containers[interface]['container']['address'], container_iface['colored']))

        print('\n')
    print('---------------')
    #print('{}{} network interfaces that include {} bridge listed where {} up, {} down and {} with unknown status.{}'.format(cl.fg.WHITE, _report['n_iface'], _report['br_count'], _report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown'], cl.fg.RESET))
    print('{}{}'.format(cl.style.BOLD, cl.fg.WHITE))
    print('{} network interfaces that include {} bridge listed'.format(_report['n_iface'],_report['br_count']))
    print('{} up, {} down and {} with unknown status.'.format(_report['iface_oper_up'], _report['iface_oper_down'], _report['iface_oper_unknown']))
    print('{}'.format(cl.style.RESET_ALL))
    print('---------------')


if __name__ == '__main__':
    get_network_interfaces()

