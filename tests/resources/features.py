"""
Copyright 2022 SiriusXM-Pandora

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class ComplexFormattingTestFeature:
    unformatted = '\n'.join([
        'Feature: feature',
        'Single line description',
        'Background:',
        'description',
        'Given background',
        'Scenario: scenario 1',
        'Given step',
        'And step',
        'When step',
        '@tag1 @tag2',
        'Scenario: scenario 2',
        'Multiline',
        'Description',
        'Given step',
        'When step',
        'Then step',
        '* step',
        '* step',
        'Scenario Outline: outline 1',
        'Given <A>',
        'Then <B>',
        'Examples:',
        '|A|B|',
        '|1|2|',
        'Scenario Outline: outline 2',
        '    description',
        'Given <A>',
        '@example1 @example2',
        '@example3',
        'Examples:',
        '|A|',
        '|B|',
        '|C|',
        '|D|',
        'Examples:',
        '|A|',
        '|E|',
        '|F|',
        '|G|',
    ])

    formatted = '\n'.join([
        'Feature: feature',
        '  Single line description',
        '',
        '',
        '    Background:',
        '      description',
        '',
        '        Given background',
        '',
        '',
        '    Scenario: scenario 1',
        '',
        '        Given step',
        '        And step',
        '        When step',
        '',
        '',
        '    @tag1',
        '    @tag2',
        '    Scenario: scenario 2',
        '      Multiline',
        '      Description',
        '',
        '        Given step',
        '        When step',
        '        Then step',
        '        * step',
        '        * step',
        '',
        '',
        '    Scenario Outline: outline 1',
        '',
        '        Given <A>',
        '        Then <B>',
        '',
        '        Examples:',
        '          | A | B |',
        '          | 1 | 2 |',
        '',
        '',
        '    Scenario Outline: outline 2',
        '      description',
        '',
        '        Given <A>',
        '',
        '        @example1',
        '        @example2',
        '        @example3',
        '        Examples:',
        '          | A |',
        '          | B |',
        '          | C |',
        '          | D |',
        '',
        '        Examples:',
        '          | A |',
        '          | E |',
        '          | F |',
        '          | G |',
        '',
    ])
