import os
from uuid import uuid4
from pathlib import Path

path = Path.cwd().parent
RELATIVE_PATH = 's3-box-overlay/bin/Release'
dst_path = path / RELATIVE_PATH
STR_FORMAT= """      <Component Id="ProductComponent%03d" Guid="%s" >
        <File Id="OverlayFile%03d" Source="..\\%s\\%s" />
      </Component>"""

i = 1
lst_x86 = []
lst_x64 = []
print('    <ComponentGroup Id="OverlayComponents" Directory="INSTALLFOLDER">')
for root, dirs, files in os.walk(dst_path):
    for name in files:
        s = STR_FORMAT % (i, uuid4(), i, Path(root).relative_to(path), name)
        if Path(root).name == 'x86':
            lst_x86.append(s)
        elif Path(root).name == 'x64':
            lst_x64.append(s)
        else:
            print(s)
        i += 1
print('    </ComponentGroup>')
print('    <ComponentGroup Id="OverlayX86Components" Directory="SUBFOLDERx86">')
for s in lst_x86:
    print(s)
print('    </ComponentGroup>')
print('    <ComponentGroup Id="OverlayX64Components" Directory="SUBFOLDERx64">')
for s in lst_x64:
    print(s)
print('    </ComponentGroup>')
