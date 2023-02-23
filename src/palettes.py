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
    'solid': {
        '024': [0xfe, 0xc4, 0x01],
        '106': [0xe7, 0x64, 0x19],
        '021': [0xde, 0x01, 0x0e],
        '221': [0xde, 0x38, 0x8b],
        '023': [0x01, 0x58, 0xa8],
        '028': [0x01, 0x7c, 0x29],
        '119': [0x95, 0xb9, 0x0c],
        '192': [0x5c, 0x1d, 0x0d],
        '018': [0xd6, 0x73, 0x41],
        '001': [0xf4, 0xf4, 0xf4],
        '026': [0x02, 0x02, 0x02],
        '226': [0xff, 0xff, 0x99],
        '222': [0xee, 0x9d, 0xc3],
        '212': [0x87, 0xc0, 0xea],
        '037': [0x01, 0x96, 0x25],
        '005': [0xd9, 0xbb, 0x7c],
        '283': [0xf5, 0xc1, 0x89],
        '208': [0xe4, 0xe4, 0xda],
        '191': [0xf4, 0x9b, 0x01],
        '124': [0x9c, 0x01, 0xc6],
        '102': [0x48, 0x8c, 0xc6],
        '135': [0x5f, 0x75, 0x8c],
        '151': [0x60, 0x82, 0x66],
        '138': [0x8d, 0x75, 0x53],
        '038': [0xa8, 0x3e, 0x16],
        '194': [0x9c, 0x92, 0x91],
        '154': [0x80, 0x09, 0x1c],
        '268': [0x2d, 0x16, 0x78],
        '140': [0x01, 0x26, 0x42],
        '141': [0x01, 0x35, 0x17],
        '312': [0xaa, 0x7e, 0x56],
        '199': [0x4d, 0x5e, 0x57],
        '308': [0x31, 0x10, 0x07]
    },

    'transparent': {
        '044': [0xf9, 0xef, 0x69],
        '182': [0xec, 0x76, 0x0e],
        '047': [0xe7, 0x66, 0x48],
        '041': [0xe0, 0x2a, 0x29],
        '113': [0xee, 0x9d, 0xc3],
        '126': [0x9c, 0x95, 0xc7],
        '042': [0xb6, 0xe0, 0xea],
        '043': [0x50, 0xb1, 0xe8],
        '143': [0xce, 0xe3, 0xf6],
        '048': [0x63, 0xb2, 0x6e],
        '311': [0x99, 0xff, 0x66],
        '049': [0xf1, 0xed, 0x5b],
        '111': [0xa6, 0x91, 0x82],
        '040': [0xee, 0xee, 0xee]
    },

    'effects': {
        '131': [0x8d, 0x94, 0x96],
        '297': [0xaa, 0x7f, 0x2e],
        '148': [0x49, 0x3f, 0x3b],
        '294': [0xfe, 0xfc, 0xd5]
    },

    'mono': {
        '001': [0xf4, 0xf4, 0xf4],
        '026': [0x02, 0x02, 0x02]
    },

    'temp': {
        '001': [0xf4, 0xf4, 0xf4],
        '002': [0x02, 0x02, 0x02],
        '003': [0xf4, 0x02, 0x02],
        '004': [0x02, 0xf4, 0x02],
        '005': [0x02, 0x02, 0xf4]
    },

    'px-master': {
        '001': [0xff, 0xff, 0xff],
        '176': [0xb0, 0xb5, 0xc5],
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
