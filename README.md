# Ansible Role: Ansible network facts collection

Ansible role for testing open network ports and collecting hardware and interface facts on network devices

## Overview

This role tests for open network ports (TELNET, SSH, NETCONF) on target hosts and collects facts about device hardware and interfaces using the respective network operating systems' ```*_facts``` modules (i.e., ```ios_facts```) with custom templating

By default, the output is stored in the ```output/ansible_network_facts``` folder that is automatically created at the root from where you are executing the corresponding playbook. If you also want to send an e-mail of the output, ensure that ```send_email``` is ```true``` and provide the necessary mail credentials in [defaults/main.yml](defaults/main.yml). All variables that can be overridden can be found under [Role Variables](#role-variables).

## Prerequisites

* Ansible >= 2.9.1
* Properly setup network inventory per the [Ansible for Network Automation](https://docs.ansible.com/ansible/latest/network/index.html).

## Supported Network Operating Systems

* [ios](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_facts_module.html#ansible-collections-cisco-ios-ios-facts-module)
* [ios-xr](https://docs.ansible.com/ansible/latest/collections/cisco/iosxr/iosxr_facts_module.html#ansible-collections-cisco-iosxr-iosxr-facts-module)
* [nxos](https://docs.ansible.com/ansible/latest/collections/cisco/nxos/nxos_facts_module.html#ansible-collections-cisco-nxos-nxos-facts-module)
* [junos](https://docs.ansible.com/ansible/latest/collections/junipernetworks/junos/junos_facts_module.html#ansible-collections-junipernetworks-junos-junos-facts-module)

## Port Checking

A custom Ansible module - [network_port_check.py](library/network_port_check.py) - is used for running the check for the open ports.

## Role Variables

All variables which can be overridden are stored within [defaults/main.yml](defaults/main.yml)

| Name | Default | Description |
| ---- | ------- | ----------- |
|      |         |             |

## Sample Inventory

[Network Host Sample Inventory](sample_inventory)

## Sample Playbook

```yaml
---
- name: Assemble facts for network devices
  hosts: all
  gather_facts: false
  tasks:
    - name: Check for open ports and gather facts
      ansible.builtin.include_role:
        name: ansible-network-facts
      tags:
        - "always"
```

## Sample Execution

Test for open ports and collect all facts

```ansible-playbook [playbook name] -i [inventory location]```

Test only for open ports

```ansible-playbook [playbook name] -i [inventory location] --tags=ports```

Test for open ports and collect hardware facts

```ansible-playbook [playbook name] -i [inventory location] --tags=ports,hardware```

## Additional Resources

[Ansible Network Automation](https://docs.ansible.com/ansible/latest/network/index.html)

## Authors

* Darren Bono - [darren.bono@att.net](mailto://dbono215@gmail.com)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE.md) for details
