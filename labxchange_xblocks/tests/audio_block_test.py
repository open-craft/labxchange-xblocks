# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import ddt

from xblock.field_data import DictFieldData
from labxchange_xblocks.audio_block import AudioBlock
from utils import BlockTestCaseBase


@ddt.ddt
class AudioBlockTestCase(BlockTestCaseBase):

    block_type = 'lx_audio'
    block_class = AudioBlock
    maxDiff = None

    data = (
        (
            {},
            {
                'display_name': 'Audio',
                'embed_code': '',
                'options': [],
                'sequences': [],
                'transcripts': {},
                'user_state': { 'current_language': None },
            },
            (
                """<div class="audio-block-student-view unfolded">
    <div class="audio-block-embed-code-student-view">
        
    </div>
    <div class="audio-block-transcript-student-view">
        <div class="audio-block-transcript-title-student-view">
            <h2>Transcripts</h2>
            <select class="audio-block-transcript-select">
                
            </select>
            <button class="audio-block-transcript-toggle"></button>
        </div>
        <div class="audio-block-sequences-student-view"></div>
    </div>
</div>
"""
            ),
        ), (
            {
                'display_name': 'A very cool track',
                'embed_code': '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/794640376&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>',  # noqa: E501
                'options': [],
                'sequences': [],
                'transcripts': {},
                'user_state': { 'current_language': None },
            },
            {
                'display_name': 'A very cool track',
                'embed_code': '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/794640376&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>',  # noqa: E501
                'options': [],
                'sequences': [],
                'transcripts': {},
                'user_state': { 'current_language': None },
            },
            (
                """<div class="audio-block-student-view unfolded">
    <div class="audio-block-embed-code-student-view">
        <iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/794640376&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>
    </div>
    <div class="audio-block-transcript-student-view">
        <div class="audio-block-transcript-title-student-view">
            <h2>Transcripts</h2>
            <select class="audio-block-transcript-select">
                
            </select>
            <button class="audio-block-transcript-toggle"></button>
        </div>
        <div class="audio-block-sequences-student-view"></div>
    </div>
</div>
"""
            ),
        )
    )

    @ddt.data(*data)
    @ddt.unpack
    def test_student_view_data(self, field_data, expected_data, _expected_html):
        self._test_student_view_data(field_data, expected_data)

    @ddt.data(*data)
    @ddt.unpack
    def test_student_view(self, field_data, _expected_data, expected_html):
        block = self._construct_xblock_mock(self.block_class, self.keys, field_data=DictFieldData(field_data))

        fragment = block.student_view(None)
        self.assertEqual(fragment.content, expected_html)
        fragment = block.public_view(None)
        self.assertEqual(fragment.content, expected_html)
