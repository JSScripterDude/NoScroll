import ctypes

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

ENABLE_QUICK_EDIT_MODE = 0x0040
ENABLE_EXTENDED_FLAGS = 0x0080

kernel32 = ctypes.windll.kernel32
hStdOut = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

mode = ctypes.c_ulong()
kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
mode.value &= ~ENABLE_QUICK_EDIT_MODE
mode.value &= ~ENABLE_EXTENDED_FLAGS
kernel32.SetConsoleMode(hStdOut, mode)
