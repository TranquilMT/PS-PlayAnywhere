"""Exercise native platform navigation on a running Android emulator using adb."""
from pathlib import Path
import re
import subprocess
import time
from xml.etree import ElementTree

PACKAGE = 'com.tranquil.ps5remoteplay'
OUTPUT = Path('platform-screens')
OUTPUT.mkdir(exist_ok=True)


def adb(*args):
    return subprocess.check_output(['adb', *args])


def wait_node(attribute, value):
    for _ in range(8):
        adb('shell', 'uiautomator', 'dump', '/sdcard/vynuvo-ui.xml')
        root = ElementTree.fromstring(adb('exec-out', 'cat', '/sdcard/vynuvo-ui.xml'))
        for node in root.iter('node'):
            if node.get(attribute) == value:
                return node
        time.sleep(0.25)
    raise AssertionError(f'Missing {attribute}={value}')


def button(name):
    return wait_node('resource-id', f'{PACKAGE}:id/{name}')


def tap(node):
    left, top, right, bottom = map(int, re.findall(r'\d+', node.attrib['bounds']))
    adb('shell', 'input', 'tap', str((left + right) // 2), str((top + bottom) // 2))


def screenshot(name):
    (OUTPUT / (name + '.png')).write_bytes(adb('exec-out', 'screencap', '-p'))


adb('shell', 'am', 'start', '-W', '-n', PACKAGE + '/com.metallic.chiaki.main.MainActivity')
for view_id in ('playPlatform', 'xboxPreview', 'pcPreview'):
    button(view_id)
screenshot('platform-hub')
for view_id, title in [('xboxPreview', 'Xbox Cloud Gaming'), ('pcPreview', 'PC / Steam')]:
    control = button(view_id)
    assert 'Coming soon' in control.get('text', '')
    tap(control)
    wait_node('text', title)
    adb('shell', 'input', 'keyevent', 'KEYCODE_BACK')
tap(button('playPlatform'))
wait_node('text', 'Your consoles')
button('floatingActionButton')
screenshot('console-picker')
adb('shell', 'input', 'keyevent', 'KEYCODE_BACK')
button('playPlatform')
print('Platform hub, both previews, console picker and Back navigation passed.')
