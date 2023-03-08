# -*- coding: utf-8 -*-

"""
legofy.palettes
---------------

This module contains the `lego` palette mappings.

Color mapping source;
 - http://www.brickjournal.com/files/PDFs/2010LEGOcolorpalette.pdf


    USAGE:
    $ legofy.palettes.legos

See README for project details.
"""
from __future__ import division


LEGOS = {

    # 흑백
    'mono': {
        '001': [0xf4, 0xf4, 0xf4],
        '026': [0x02, 0x02, 0x02]
    },

    # taobao(px-master) 블록 리스트
    'px-master': {
        '1': [0xff, 0xff, 0xff],
        '194': [0xb0, 0xb5, 0xc5],
        '199': [0x5a, 0x5d, 0x60],
        'A29': [0x4b, 0x4c, 0x50],
        '26': [0x21, 0x21, 0x21],
        '297': [0xdb, 0x99, 0x35],
        '179': [0x89, 0x87, 0x88],
        '148': [0x66, 0x66, 0x61],
        '326': [0xe2, 0xee, 0xad],
        '119': [0xad, 0xc9, 0x66],
        '37': [0x5d, 0xc8, 0x4b],
        '28': [0x29, 0x62, 0x34],
        '141': [0x37, 0x54, 0x44],
        '330': [0x80, 0x8f, 0x58],
        '151': [0x7f, 0xa1, 0x91],
        '323': [0xd6, 0xfe, 0xfe],
        '107': [0x3c, 0x88, 0x80],
        '212': [0xa6, 0xc2, 0xe5],
        '135': [0x5f, 0x70, 0x82],
        '102': [0x74, 0xad, 0xf9],
        '322': [0x68, 0xbd, 0xf6],
        '321': [0x52, 0x97, 0xf7],
        '23': [0x23, 0x56, 0xa1],
        '140': [0x1b, 0x2f, 0x42],
        'A08': [0xf9, 0xd8, 0xc6],
        '283': [0xe4, 0xc2, 0xa8],
        'A24': [0xe8, 0xb8, 0x98],
        'A25': [0xe1, 0xa5, 0x80],
        '18': [0xd3, 0x93, 0x6c],
        '106': [0xef, 0x85, 0x37],
        '191': [0xee, 0xbc, 0x4f],
        '24': [0x71, 0xd2, 0x4b],
        '226': [0xf0, 0xe1, 0x6d],
        '5': [0xda, 0xc7, 0xa1],
        '138': [0x8c, 0x75, 0x55],
        '312': [0xab, 0x7e, 0x58],
        '38': [0xa7, 0x59, 0x22],
        '192': [0x7f, 0x3a, 0x24],
        '308': [0x2e, 0x04, 0x02],
        '268': [0x58, 0x29, 0x7e],
        'A13': [0x7a, 0x57, 0xa7],
        '324': [0x82, 0x60, 0x9a],
        '325': [0xab, 0x8d, 0xbc],
        '222': [0xf5, 0xbe, 0xfb],
        '221': [0xbc, 0x74, 0x81],
        '124': [0xa7, 0x36, 0x53],
        '220': [0xe9, 0x89, 0x7d],
        '21': [0xa4, 0x21, 0x18],
        '154': [0x61, 0x18, 0x19]
    }
}

''' RGB -> 블록 코드 변환 시 필요
pxmaster = {
    '1': [0xff, 0xff, 0xff],
    '194': [0xb0, 0xb5, 0xc5],
    '199': [0x5a, 0x5d, 0x60],
    'A29': [0x4b, 0x4c, 0x50],
    '26': [0x21, 0x21, 0x21],
    '297': [0xdb, 0x99, 0x35],
    '179': [0x89, 0x87, 0x88],
    '148': [0x66, 0x66, 0x61],
    '326': [0xe2, 0xee, 0xad],
    '119': [0xad, 0xc9, 0x66],
    '37': [0x5d, 0xc8, 0x4b],
    '28': [0x29, 0x62, 0x34],
    '141': [0x37, 0x54, 0x44],
    '330': [0x80, 0x8f, 0x58],
    '151': [0x7f, 0xa1, 0x91],
    '323': [0xd6, 0xfe, 0xfe],
    '107': [0x3c, 0x88, 0x80],
    '212': [0xa6, 0xc2, 0xe5],
    '135': [0x5f, 0x70, 0x82],
    '102': [0x74, 0xad, 0xf9],
    '322': [0x68, 0xbd, 0xf6],
    '321': [0x52, 0x97, 0xf7],
    '23': [0x23, 0x56, 0xa1],
    '140': [0x1b, 0x2f, 0x42],
    'A08': [0xf9, 0xd8, 0xc6],
    '283': [0xe4, 0xc2, 0xa8],
    'A24': [0xe8, 0xb8, 0x98],
    'A25': [0xe1, 0xa5, 0x80],
    '18': [0xd3, 0x93, 0x6c],
    '106': [0xef, 0x85, 0x37],
    '191': [0xee, 0xbc, 0x4f],
    '24': [0x71, 0xd2, 0x4b],
    '226': [0xf0, 0xe1, 0x6d],
    '5': [0xda, 0xc7, 0xa1],
    '138': [0x8c, 0x75, 0x55],
    '312': [0xab, 0x7e, 0x58],
    '38': [0xa7, 0x59, 0x22],
    '192': [0x7f, 0x3a, 0x24],
    '308': [0x2e, 0x04, 0x02],
    '268': [0x58, 0x29, 0x7e],
    'A13': [0x7a, 0x57, 0xa7],
    '324': [0x82, 0x60, 0x9a],
    '325': [0xab, 0x8d, 0xbc],
    '222': [0xf5, 0xbe, 0xfb],
    '221': [0xbc, 0x74, 0x81],
    '124': [0xa7, 0x36, 0x53],
    '220': [0xe9, 0x89, 0x7d],
    '21': [0xa4, 0x21, 0x18],
    '154': [0x61, 0x18, 0x19]
} '''

def extend_palette(palette, colors=256, rgb=3):
    """Extend palette colors to 256 rgb sets."""
    missing_colors = colors - len(palette)//rgb
    if missing_colors > 0:
        first_color = palette[:rgb]
        palette += first_color * missing_colors
    return palette[:colors*rgb]


def legos():
    """Build flattened lego palettes."""
    return _flatten_palettes(LEGOS.copy())


def _flatten_palettes(palettes):
    """Convert palette mappings into color list."""
    flattened = {}
    palettes = _merge_palettes(palettes)
    for palette in palettes:
        flat = [i for sub in palettes[palette].values() for i in sub]
        flattened.update({palette: flat})
    return flattened


def _merge_palettes(palettes):
    """Build unified palette using all colors."""
    unified = {}
    for palette in palettes:
        for item in palettes[palette]:
            unified.update({item: palettes[palette][item]})
    palettes.update({'all': unified})
    return palettes
