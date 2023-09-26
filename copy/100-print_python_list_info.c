#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	PyObject *element;
	int size, mem_allocated, i = 0;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	mem_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", mem_allocated);

	while (i < size)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}