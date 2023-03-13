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

    printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocat);

    for (i = 0; i < size; i++)
    {
        
    }
}
