#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    trademark = 'Roundel',
    script = 'Gurmukhi',
    hide_script_name = True,
)
family.set_styles(
    style_scheme = [
        ('Light',       0, 300),
        ('Regular',     9, 400),
        ('Medium',     26, 500),
        ('SemiBold',   49, 600),
        ('Bold',       76, 700),
        ('ExtraBold', 100, 800),
    ],
)

builder = kit.Builder(
    family,
    fontrevision = '0.201',
    vertical_metrics = {
        'Ascender': 750,
        'Descender': -250,
        'LineGap': 200,
    },
    options = {
        'prep_mark_positioning': True,
        'override_GDEF': True,
        'do_style_linking': True,
    },
)
builder.import_glyphs(
    from_masters = [
        'masters/latin/RoundelLatin-Light.ufo',
        'masters/latin/RoundelLatin-Bold.ufo',
    ],
    to_masters = [
        'masters/gurmukhi/Roundel Gurmukhi-Light.ufo',
        'masters/gurmukhi/Roundel Gurmukhi-Bold.ufo',
    ],
    save_to_masters = [
        'masters/Roundel-Light.ufo',
        'masters/Roundel-Bold.ufo',
    ],
    excluding_names = 'space CR NULL'.split(),
    deriving_names = 'CR NULL'.split(),
)
builder.build()
