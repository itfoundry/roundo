#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    trademark = 'Roundel',
    script = 'Gurmukhi',
)
family.info.openTypeNameDesigner = "Namrata Goyal (Gurmukhi); Shiva Nallaperumal (Latin)"

family.set_masters()
family.set_styles(
    style_scheme = [
        ('ExtraLight', 0, 250),
        ('Light',      9, 300),
        ('Regular',   26, 400),
        ('Medium',    49, 500),
        ('SemiBold',  76, 600),
        ('Bold',     100, 700),
    ],
)

def prepare_master(self, master):
    master.import_glyphs_from(
        source_dir = 'masters/Latin/',
        target_dir = 'masters/Gurmukhi/',
        excluding_names = 'space NULL CR'.split(),
    )
    master.derive_glyphs('NULL CR'.split())

kit.Builder.prepare_master = prepare_master

builder = kit.Builder(
    family,
    fontrevision = '1.000',
    vertical_metrics = {
        'Ascender': 1050,
        'Descender': -450,
        'TypoAscender': 800,
        'TypoDescender': -200,
    },
    options = {
        'prepare_master': True,
        # 'prep_mark_positioning': True,
        'do_style_linking': True,
        'build_ttf': True,
    },
)
builder.build()
