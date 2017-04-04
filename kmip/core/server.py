# Copyright (c) 2014 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class KMIP(object):

    def __init__(self):
        pass

    def create(self, object_type, template_attribute, credential=None):
        raise NotImplementedError()

    def create_key_pair(self, common_template_attribute,
                        private_key_template_attribute,
                        public_key_template_attribute):
        raise NotImplementedError()

    def register(self, object_type, template_attribute, secret,
                 credential=None):
        raise NotImplementedError()

    def rekey_key_pair(self, private_key_unique_identifier,
                       offset, common_template_attribute,
                       private_key_template_attribute,
                       public_key_template_attribute):
        raise NotImplementedError()

    def get(self, uuid=None, key_format_type=None, key_compression_type=None,
            key_wrapping_specification=None, credential=None):
        raise NotImplementedError()

    def destroy(self, uuid, credential=None):
        raise NotImplementedError()

    def locate(self, maximum_items=None, storate_status_mask=None,
               object_group_member=None, attributes=None,
               credential=None):
        raise NotImplementedError()

    def discover_versions(self, protocol_versions=None):
        raise NotImplementedError()
