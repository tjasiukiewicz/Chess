#include <Python.h>

static PyObject *method_fputs(PyObject *self, PyObject *args) {
    char *str, *filename = NULL;
    int bytes_copied = -1;

    /* Parsowanie argumentów */
    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    if (strlen(str) < 10) {
        PyErr_SetString(PyExc_ValueError, "Ciąg znaków powinien być dłuższy od 10");
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    return PyLong_FromLong(bytes_copied);
}

static PyMethodDef FputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Interfejs do funkcji fputs"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,
    "fputs",
    "Interfejs do funkcji fputs",
    -1,
    FputsMethods
};

PyMODINIT_FUNC PyInit_fputs(void) {
    /* Rejestrowanie modułu */
    PyObject *module = PyModule_Create(&fputsmodule);

    /* Stała dostępna przez nazwę */
    PyModule_AddIntConstant(module, "FPUTS_FLAG", 64);

    /* Stała dostępna przez makro */
    #define FPUTS_MACRO 256

    /* Dodanie makra do modułu */
    PyModule_AddIntMacro(module, FPUTS_MACRO);

    //return PyModule_Create(module);
    return module;
}
