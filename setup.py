#!/usr/bin/env python3
# coding=utf-8

#
# Copyright (c) 2020 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup

INSTALL_REQUIRES = []


def main():
    setup(name='xdevice',
          description='xdevice test framework',
          url='',
          package_dir={'': 'src', 'adapter': 'adapter'},
          packages=['xdevice',
                    'xdevice._core',
                    'xdevice._core.build',
                    'xdevice._core.command',
                    'xdevice._core.config',
                    'xdevice._core.driver',
                    'xdevice._core.environment',
                    'xdevice._core.executor',
                    'xdevice._core.report',
                    'xdevice._core.testkit',
                    'adapter.xdevice_adapter',
                    ],
          package_data={
              'xdevice._core': [
                  'resource/*.txt',
                  'resource/config/*.xml',
                  'resource/template/*.html'
              ]
          },
          entry_points={
              'console_scripts': [
                  'xdevice=xdevice.__main__:main_process',
                  'xdevice_report=xdevice._core.report.__main__:main_report'
              ]
          },
          zip_safe=False,
          install_requires=INSTALL_REQUIRES,
          )


if __name__ == "__main__":
    main()
