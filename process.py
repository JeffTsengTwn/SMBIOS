import ctypes as ct
from ctypes import wintypes as w

kernel32 = ct.WinDLL('kernel32')
user32 = ct.WinDLL('user32')

kernel32.GetSystemFirmwareTable.argtypes = w.DWORD, w.DWORD, w.LPVOID, w.DWORD
kernel32.GetSystemFirmwareTable.restype = w.UINT

smBiosDataSize = kernel32.GetSystemFirmwareTable( int.from_bytes(b'RSMB'), 0, None, 0)

print(f'smBiosDataSize = {smBiosDataSize}')