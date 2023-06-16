#include <Python.h>

void print_python_list(PyObject *list_object);
void print_python_bytes(PyObject *bytes_object);

void print_python_list(PyObject *list_object) {
    int size, allocation, i;
    const char *element_type;
    PyListObject *list = (PyListObject *)list_object;
    PyVarObject *var = (PyVarObject *)list_object;

    size = var->ob_size;
    allocation = list->allocated;

    printf("[*] Python list information\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocation);

    for (i = 0; i < size; i++) {
        element_type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %d: %s\n", i, element_type);
        if (strcmp(element_type, "bytes") == 0) {
            print_python_bytes_v2(list->ob_item[i]);
        }
    }
}

void print_python_bytes(PyObject *bytes_object) {
    unsigned char i, size;
    PyBytesObject *bytes = (PyBytesObject *)bytes_object;

    printf("[.] Bytes object information\n");
    if (strcmp(bytes_object->ob_type->tp_name, "bytes") != 0) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)bytes_object)->ob_size;
    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", bytes->ob_sval);

    /* Use a different hashing algorithm for the bytes object.*/
    unsigned char hash[20];
    crypto_hash(hash, bytes->ob_sval, size);

    /*Print the bytes object in hexadecimal format instead of decimal format.*/
    for (i = 0; i < size; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}
