import ctypes as ct
from ctypes import wintypes as w

kernel32 = ct.WinDLL('kernel32')
user32 = ct.WinDLL('user32')

kernel32.GetSystemFirmwareTable.argtypes = w.DWORD, w.DWORD, w.LPVOID, w.DWORD
kernel32.GetSystemFirmwareTable.restype = w.UINT

user32.CreateWindowExA.argtypes = w.DWORD, w.LPCSTR, w.LPCSTR, w.DWORD, w.INT, w.INT, w.INT, w.INT, w.HWND, w.HMENU, w.HINSTANCE, w.LPVOID
user32.CreateWindowExA.restype = w.HWND

smBiosDataSize = kernel32.GetSystemFirmwareTable( int.from_bytes(b'RSMB'), 0, None, 0)

mHwnd = user32.CreateWindowExA('Win32 Class',               
                                "Win32 test",         
                                WS_OVERLAPPEDWINDOW, 
                                100,                   
                                200,                    
                                800,                    
                                600,                    
                                None,                   
                                None,                  
                                None,              
                                None);          

print(f'smBiosDataSize = {smBiosDataSize}')