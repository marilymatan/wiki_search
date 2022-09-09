import unittest
import requests


class TestApi(unittest.TestCase):
    URL = "http://localhost:5000/v1/api/search"
    res = [
        {
            "title": "CMU Common Lisp",
            "summary": "CMUCL is a free Common Lisp implementation, originally developed at Carnegie Mellon "
                       "University.\nCMUCL runs on most Unix-like platforms, including Linux and BSD; there is an "
                       "experimental Windows port as well. Steel Bank Common Lisp is derived from CMUCL. The Scieneer "
                       "Common Lisp is a commercial derivative from CMUCL."
        },
        {
            "title": "Colt Python",
            "summary": "The Colt Python is a .357 Magnum caliber revolver manufactured by Colt's Manufacturing "
                       "Company of "
                       "Hartford, Connecticut. It was first introduced in 1955, the same year as Smith & Wesson's M29 .44 "
                       "Magnum. The Colt Python is intended for the premium revolver market segment. Some firearm collectors "
                       "and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy Thompson, Scott Wolber, Renee Smeets "
                       "and Martin Dougherty have described the Python as \"the finest production revolver ever made\".In "
                       "2020, Colt reintroduced the Python in a 4.25″ and a 6″ barrel configuration, followed by a 3\" barrel "
                       "version in 2022. The reintroduced Python has been technically revised and reinforced compared "
                       "to the "
                       "original revolver."
        },
        {
            "title": "Cython",
            "summary": "Cython () is a programming language that aims to be a superset of the Python programming "
                       "language, designed to give C-like performance with code that is written mostly in Python with "
                       "optional additional C-inspired syntax.Cython is a compiled language that is typically used to "
                       "generate CPython extension modules. Annotated Python-like code is compiled to C or C++ then "
                       "automatically wrapped in interface code, producing extension modules that can be loaded and "
                       "used by regular Python code using the import statement, but with significantly less "
                       "computational overhead at run time. Cython also facilitates wrapping independent C or C++ "
                       "code into python-importable modules.\nCython is written in Python and C and works on Windows, "
                       "macOS, and Linux, producing source files compatible with CPython 2.6, 2.7, and 3.3 and later "
                       "versions.\nCython 3.0.0 is in development."
        }
    ]

    def test_true(self):
        resp = requests.get(url=self.URL, params="search_phrase=python&k=3")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), self.res)
        print('Test 1 was completed')

        resp = requests.get(url=self.URL, params="search_phrase=searchIsNotExist&k=3")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {'result': 'Page does not exist'})
        print('Test 2 was completed')

        resp = requests.get(url=self.URL, params="search_phrase=Python_(programming_language)&k=3")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), [
                                          {
                                            "title": "Python (programming language)",
                                            "summary": "Python is a high-level, general-purpose programming language. "
                                                       "Its design philosophy emphasizes code readability with the "
                                                       "use of significant indentation.Python is dynamically-typed "
                                                       "and garbage-collected. It supports multiple programming "
                                                       "paradigms, including structured (particularly procedural), "
                                                       "object-oriented and functional programming. It is often "
                                                       "described as a \"batteries included\" language due to its "
                                                       "comprehensive standard library.Guido van Rossum began working "
                                                       "on Python in the late 1980s as a successor to the ABC "
                                                       "programming language and first released it in 1991 as Python "
                                                       "0.9.0. Python 2.0 was released in 2000 and introduced new "
                                                       "features such as list comprehensions, cycle-detecting garbage "
                                                       "collection, reference counting, and Unicode support. Python "
                                                       "3.0, released in 2008, was a major revision that is not "
                                                       "completely backward-compatible with earlier versions. Python "
                                                       "2 was discontinued with version 2.7.18 in 2020.Python "
                                                       "consistently ranks as one of the most popular programming "
                                                       "languages."
                                          }
                                      ])
        print('Test 3 was completed')

    def test_false(self):
        resp = requests.get(url=self.URL, params="search_phrase=python&k=1")
        self.assertEqual(resp.status_code, 500)
        self.assertEqual(resp.json(), self.res)

        resp = requests.get(url=self.URL, params="search_phrase=Python_(programming_language)&k=3")
        self.assertEqual(resp.json(), self.res)


if __name__ == "__main__":
    tester = TestApi()
    tester.test_true()
    tester.test_false()
