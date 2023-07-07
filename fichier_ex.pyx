from libc.stdio cimport printf

cdef void func_ex_cy(const char *text_print):
    printf(text_print)

def func_ex(text: str) -> None:
    func_ex_cy(text.encode('UTF-8'))
