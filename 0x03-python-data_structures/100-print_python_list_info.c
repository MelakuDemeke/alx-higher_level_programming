#include <Python.h>
/**
 * print_python_list_info - print information about python list
 * 
 * @p: a PyObject list
*/
void print_python_list_info(PyObject *p)
{
    int size, allocat;
    PyObject *obj;

    size = Py_SIZE(p);
    allocat = ((PyListObject *)p)->allocated;
}
