#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals
import hindkit as kit

family = kit.Family(
    client = 'Google Fonts',
    script = 'Gurmukhi',
    trademark = 'Roundel',
    designers = 'Namrata Goyal (Gurmukhi); Shiva Nallaperumal (Latin)',
)
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

builder = kit.Builder(
    family,
    fontrevision = '0.900',
    vertical_metrics = {
        'Ascender': 750,
        'Descender': -250,
        'LineGap': 200,
    },
    options = {
        # 'prep_mark_positioning': True,
        'override_GDEF': True,
        'do_style_linking': True,
    },
)

kit.tools.import_glyphs(
    source_paths = [
        'masters/latin/Roundel Latin-Light.ufo',
        'masters/latin/Roundel Latin-Bold.ufo',
    ],
    target_paths = [
        'masters/gurmukhi/Roundel Gurmukhi-Light.ufo',
        'masters/gurmukhi/Roundel Gurmukhi-Bold.ufo',
    ],
    save_as_paths = [
        'masters/Roundel-Light.ufo',
        'masters/Roundel-Bold.ufo',
    ],
    excluding_names = 'space CR NULL'.split(),
    deriving_names = 'CR NULL'.split(),
)

builder.build()
