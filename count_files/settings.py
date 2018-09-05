#!/usr/bin/env python3
# encoding: utf-8
import shutil
import platform

BUG_REPORT_URL = 'https://github.com/victordomingos/Count-files/issues'

TERM_WIDTH = shutil.get_terminal_size((80, 24)).columns
DEFAULT_PREVIEW_SIZE = 5 * TERM_WIDTH  # 5 lines of text preview
START_TEXT_WIDTH = min(TERM_WIDTH, 100)
DEFAULT_EXTENSION_COL_WIDTH = 9
DEFAULT_FREQ_COL_WIDTH = 5
MAX_TABLE_WIDTH = 80

# ====================[ iOS/Pythonista specific settings ]====================
IPAD_FONT_SIZE = 15
IPHONE_FONT_SIZE = 10
IOS_WORKERS = 2
IOS_FONT = "Menlo"


if platform.system() == 'Darwin':
        if platform.machine().startswith('iPad'):
            device = "iPad"
        elif platform.machine().startswith('iP'):
            device = "iPhone"
        else:
            device = "mac"
else:
    device = "other"

if device in ("iPad", "iPhone"):
    # Adapt for smaller screen sizes in iPhone and iPod touch
    import ui
    import console
    if device == 'iPad':
        font_size = IPAD_FONT_SIZE
    else:
        font_size = IPHONE_FONT_SIZE
    console.set_font(IOS_FONT, font_size)
    screen_width = ui.get_screen_size().width
    char_width = ui.measure_string('.', font=(IOS_FONT, font_size)).width
    TERM_WIDTH = int(screen_width / char_width - 1.5) - 1


SUPPORTED_TYPES = {
    'all_extensions': ['..'],
    'no_extension': ['.'],
    'text': ['py', 'txt', 'html', 'css', 'js', 'c', 'md', 'json'],
}


def simple_columns(text_input, num_columns=4):
    max_extension_width = max(map(len, text_input))
    text_table = " "
    for count, item in enumerate(sorted(text_input), 1):
        text_table += item.ljust(max_extension_width+3)
        if count % num_columns == 0 or count == len(text_input):
            text_table += "\n "
    return text_table


supported_type_info_message = f'\nThis is the list of currently supported file types for preview:\n\n' \
                              f'{simple_columns(SUPPORTED_TYPES["text"], num_columns=4)}\n' \
                              f'Previewing files without extension is not supported. ' \
                              f'You can use the "--preview" argument together with the search ' \
                              f'for all files regardless of the extension ("--file-extension .."). ' \
                              f'In this case, the preview will only be displayed for files with a supported extension.\n\n'

not_supported_type_message = f'\nSorry, there is no preview available for this file type. ' \
                             f'You may want to try again without preview. ' \
                             f'This is the list of currently supported file types for preview:\n\n' \
                             f'{simple_columns(SUPPORTED_TYPES["text"], num_columns=4)}\n'
