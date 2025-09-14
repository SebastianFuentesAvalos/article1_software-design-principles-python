# Software Design Principles: Building Robust Applications in Python

Este repositorio acompaña al artículo sobre principios de diseño de software en Python. Aquí encontrarás ejemplos de código, ejercicios prácticos y sus soluciones para que puedas aprender y practicar SRP, OCP y otros principios fundamentales.

---

## ¿Cómo usar este repositorio?

1. Lee el artículo y revisa los ejemplos en `notification.py` y en el README.
2. Entra a la carpeta `exercises/` y abre los archivos de ejercicios.
3. Resuelve los ejercicios siguiendo las instrucciones en cada archivo.
4. Compara tus soluciones con los archivos de la carpeta `solutions/`.
5. (Opcional) Ejecuta los tests para verificar tus soluciones:

```bash
python test_exercises.py
```

---

## Ejercicios incluidos

- **SRP**: Refactoriza para que cada clase tenga una sola responsabilidad.
- **OCP**: Refactoriza para permitir agregar nuevas funcionalidades sin modificar el código existente.

---

## Estructura del proyecto

```
article1_software-design-principles-python/
│
├── LICENSE
├── .gitignore
├── README.md
├── notification.py
├── exercises/
│   ├── srp_exercise.py
│   └── ocp_exercise.py
├── solutions/
│   ├── srp_solution.py
│   └── ocp_solution.py
└── test_exercises.py
```

---

## Referencias

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Python Official Docs](https://docs.python.org/3/library/abc.html)

---

*Written by Sebastian Fuentes Avalos*