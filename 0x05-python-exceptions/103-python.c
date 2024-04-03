#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Print information about PyFloatObject
 * @p: Pointer to PyObject
 */
void print_python_float(PyObject *p)
{
    double value = 0;

    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %f\n", value);
}

/**
 * print_python_bytes - Print information about PyBytesObject
 * @p: Pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    char *string = NULL;

    printf("[.] bytes object info\n");

    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);

    string = PyBytes_AsString(p);
    printf("  trying string: %s\n", string);

    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    while (i < size + 1 && i < 10)
    {
        printf(" %02hhx", string[i]);
        i++;
    }
    printf("\n");
}

/**
 * print_python_list - Print information about PyListObject
 * @p: Pointer to PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_CheckExact(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}
