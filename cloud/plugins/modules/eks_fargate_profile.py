#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by amazon_cloud_code_generator.
# See: https://github.com/ansible-collections/amazon_cloud_code_generator

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
module: eks_fargate_profile
short_description: Creates and manage AWS Fargate profiles
description:
- Creates and manage AWS Fargate profiles for your Amazon EKS cluster.
- You must have at least one Fargate profile in a cluster to be able to run pods on
    Fargate.
options:
    cluster_name:
        description:
        - Name of the Cluster.
        type: str
    fargate_profile_name:
        description:
        - Name of FargateProfile.
        type: str
    force:
        default: false
        description:
        - Cancel IN_PROGRESS and PENDING resource requestes.
        - Because you can only perform a single operation on a given resource at a
            time, there might be cases where you need to cancel the current resource
            operation to make the resource available so that another operation may
            be performed on it.
        type: bool
    identifier:
        description:
        - For compound primary identifiers, to specify the primary identifier as a
            string, list each in the order that they are specified in the identifier
            list definition, separated by '|'.
        - For more details, visit U(https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html).
        type: str
    pod_execution_role_arn:
        description:
        - The IAM policy arn for pods.
        type: str
    purge_tags:
        default: true
        description:
        - Remove tags not listed in I(tags).
        type: bool
    selectors:
        description:
        - Not Provived.
        elements: dict
        suboptions:
            labels:
                description:
                - A key-value pair to associate with a pod.
                elements: dict
                suboptions:
                    key:
                        description:
                        - The key name of the label.
                        type: str
                    value:
                        description:
                        - The value for the label.
                        type: str
                type: list
            namespace:
                description:
                - Not Provived.
                type: str
        type: list
    state:
        choices:
        - present
        - absent
        - list
        - describe
        - get
        default: present
        description:
        - Goal state for resource.
        - I(state=present) creates the resource if it doesn't exist, or updates to
            the provided state if the resource already exists.
        - I(state=absent) ensures an existing instance is deleted.
        - I(state=list) get all the existing resources.
        - I(state=describe) or I(state=get) retrieves information on an existing resource.
        type: str
    subnets:
        description:
        - Not Provived.
        elements: str
        type: list
    tags:
        aliases:
        - resource_tags
        description:
        - A dict of tags to apply to the resource.
        - To remove all tags set I(tags={}) and I(purge_tags=true).
        type: dict
    wait:
        default: false
        description:
        - Wait for operation to complete before returning.
        type: bool
    wait_timeout:
        default: 320
        description:
        - How many seconds to wait for an operation to complete before timing out.
        type: int
author: Ansible Cloud Team (@ansible-collections)
version_added: TODO
extends_documentation_fragment:
- amazon.aws.aws
- amazon.aws.ec2
'''

EXAMPLES = r'''
'''

RETURN = r'''
result:
    description:
        - When I(state=list), it is a list containing dictionaries of resource information.
        - Otherwise, it is a dictionary of resource information.
        - When I(state=absent), it is an empty dictionary.
    returned: always
    type: complex
    contains:
        identifier:
            description: The unique identifier of the resource.
            type: str
        properties:
            description: The resource properties.
            type: dict
'''

import json

from ansible_collections.amazon.aws.plugins.module_utils.core import AnsibleAWSModule
from ansible_collections.amazon.cloud.plugins.module_utils.core import CloudControlResource
from ansible_collections.amazon.cloud.plugins.module_utils.core import snake_dict_to_camel_dict
from ansible_collections.amazon.cloud.plugins.module_utils.core import ansible_dict_to_boto3_tag_list


def main():

    argument_spec = dict(
       state=dict(type='str', choices=['present', 'absent', 'list', 'describe', 'get'], default='present'),
    )
        
    argument_spec['cluster_name'] = {'type': 'str'}
    argument_spec['fargate_profile_name'] = {'type': 'str'}
    argument_spec['pod_execution_role_arn'] = {'type': 'str'}
    argument_spec['subnets'] = {'type': 'list', 'elements': 'str'}
    argument_spec['selectors'] = {'type': 'list', 'elements': 'dict', 'options': {'namespace': {'type': 'str'}, 'labels': {'type': 'list', 'elements': 'dict', 'options': {'key': {'type': 'str'}, 'value': {'type': 'str'}}}}}
    argument_spec['tags'] = {'type': 'dict', 'aliases': ['resource_tags']}
    argument_spec['state'] = {'type': 'str', 'choices': ['present', 'absent', 'list', 'describe', 'get'], 'default': 'present'}
    argument_spec['wait'] = {'type': 'bool', 'default': False}
    argument_spec['wait_timeout'] = {'type': 'int', 'default': 320}
    argument_spec['force'] = {'type': 'bool', 'default': False}
    argument_spec['purge_tags'] = {'type': 'bool', 'default': True}
    argument_spec['identifier'] = {'type': 'str'}


    required_if = [
        ['state', 'list', ['cluster_name'], True],['state', 'present', ['cluster_name', 'fargate_profile_name', 'identifier', 'pod_execution_role_arn', 'selectors'], True],['state', 'absent', ['cluster_name', 'fargate_profile_name', 'identifier'], True],['state', 'get', ['cluster_name', 'fargate_profile_name', 'identifier'], True]
    ]
    mutually_exclusive = [
        [('cluster_name', 'fargate_profile_name'), 'identifier']
    ]

    module = AnsibleAWSModule(argument_spec=argument_spec, required_if=required_if, mutually_exclusive=mutually_exclusive, supports_check_mode=True)
    cloud = CloudControlResource(module)

    type_name = 'AWS::EKS::FargateProfile'

    params = {}
        
    params['cluster_name'] = module.params.get('cluster_name')
    params['fargate_profile_name'] = module.params.get('fargate_profile_name')
    params['identifier'] = module.params.get('identifier')
    params['pod_execution_role_arn'] = module.params.get('pod_execution_role_arn')
    params['selectors'] = module.params.get('selectors')
    params['subnets'] = module.params.get('subnets')
    params['tags'] = module.params.get('tags')

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags") is not None:
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(
            module.params["tags"]
        )

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = ['cluster_name', 'fargate_profile_name', 'pod_execution_role_arn', 'subnets', 'selectors']

    # Necessary to handle when module does not support all the states
    handlers = ['create', 'read', 'delete', 'list', 'update']

    state = module.params.get('state')
    identifier = ['cluster_name', 'fargate_profile_name']
    if state in ('present', 'absent', 'get', 'describe') and module.params.get('identifier') is None:
        if not  module.params.get('cluster_name') or not module.params.get('fargate_profile_name'):
            module.fail_json(f'You must specify both {*identifier, } identifiers.')

    results = {"changed": False, "result": {}}

    if state == "list":
        if "list" not in handlers:
            module.exit_json(**results, msg=f"Resource type {type_name} cannot be listed.")
        results["result"] = cloud.list_resources(type_name, identifier)

    if state in ("describe", "get"):
        if "read" not in handlers:
            module.exit_json(**results, msg=f"Resource type {type_name} cannot be read.")
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "present":
        results = cloud.present(type_name, identifier, params_to_set, create_only_params)

    if state == "absent":
        results["changed"] |= cloud.absent(type_name, identifier)

    module.exit_json(**results)


if __name__ == '__main__':
    main()